#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019-10-12 10:30
# @Author : jared
# @File : leecode.py
# @Software: PyCharm

class Node:
    def __init__(self,val,left,right,next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def numSquares(self,n):
        dp = [i for i in range(n+1)]
        for i in range(1,n+1):
            j = 1
            while i-j*j>=0:
                dp[i] = min(dp[i],dp[i-j*j]+1)
                j+=1
        print(dp)
        return dp[n]
    def letterCombinations(self,digits:str):
        m = {'2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits:return []
        lsl = ['']
        for i in digits:
            lsl = [x+y for x in lsl for y in m[i]]
        return lsl

    def letterCombinations2(self, digits: str):
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        res = [""]
        for num in digits:
            next_res = []
            for alp in lookup[num]:
                for tmp in res:
                    next_res.append(tmp + alp)
            res = next_res
            print(res)
        return res

    def canCompleteCircuit(self,gas,cost)->int:
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    def canFinish(self,numCourses:int,prerequisites)->bool:
        clen = len(prerequisites)
        if clen == 0:
            return True

        #统计每个顶点的入读
        in_degress = [0 for _ in range(numCourses)]
        #临街表
        adj = [set() for _ in range(numCourses)]

        for second,first in prerequisites:
            in_degress[second] += 1
            adj[first].add(second)

        queue=[]
        for i in range(numCourses):
            if in_degress[i]==0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.pop(0)
            counter+=1
            for successor in adj[top]:
                in_degress[successor]-=1
                if in_degress[successor]==0:
                    queue.append(successor)
        return counter==numCourses


    def connect(self,root:Node)->Node:
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def game(self,guess,answer):
        res=0
        for x,y in zip(guess,answer):
            if x==y:
                res+=1
        return res

s = Solution()
# print(s.canFinish(2, [[1, 0]]))
# print(s.letterCombinations2("23"))
# print(s.numSquares(12))