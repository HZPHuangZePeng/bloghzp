from django.db import models

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return 'BlogType:{}'.format(self.type_name)


class Blog(models.Model):
    title = models.CharField(max_length=50)

    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)

    # blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, related_name="blog_blog")
    # content = models.TextField()
    content = RichTextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return 'Blog:{}'.format(self.blog_type)

    class Meta():
        ordering = ['-created_time']

# class Author(models.Model):
#     title = models.DateTimeField(auto_now_add=True)
#     created_time = models.DateTimeField(auto_now=True)
#     content = models.TextField(max_length=40)

