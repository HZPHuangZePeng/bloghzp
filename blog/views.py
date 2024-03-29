from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings


from django.db.models import Count

# Create your views here.
def get_blog_list_common_data(request,blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每十篇进行分页
    page_num = request.GET.get('page', 1)  # 字典，如果没有默认给1,获取页码参数
    page_of_blogs = paginator.get_page(page_num)  # 得到无效字符，自动返回1
    currentr_page_num = page_of_blogs.number  # 获取当前页码
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 获取当前页码以及前后各两页的页码范围
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:  # 3-1>=2 第5页开始
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")  # 15<=17-2
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}

    # 获取博客分类的对应博客数量
    blog_types = BlogType.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    context["blog_types"] = blog_types_list

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    context["blog_dates"] = blog_dates_dict

    # context = {}
    context["blogs"]=page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context["blogs_count"] = Blog.objects.all().count()
    context["blog_types"] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['page_range'] = page_range
    # context["blog_dates"] = Blog.objects.dates('created_time', 'month', order="DESC")
    context["blog_dates"] = blog_dates_dict


    return context
def blog_list(request):
    blogs_all_list=Blog.objects.all()
    context=get_blog_list_common_data(request,blogs_all_list)
    return render_to_response('blog/blog_list.html',context)
def blogs_with_type(request,blog_type_pk):
    blog_type=get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html',context)
def blogs_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context["blogs_with_date"]="%s年%s月" % (year,month)
    return render_to_response('blog/blogs_with_date.html',context)
def blog_detail(request,blog_pk):
    context={}
    blog=get_object_or_404(Blog,pk=blog_pk)
    context["previous_blog"]=Blog.objects.filter(created_time__gt=blog.created_time).last()
    context["next_blog"]=Blog.objects.filter(created_time__lt=blog.created_time).first()#[0]
    context["blog"]=blog
    #Blog.objects.all(pk=blog_pk)
    return render_to_response("blog/blog_detail.html",context)