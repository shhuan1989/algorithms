# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/23/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        for line in source:
            print(line)
        print('#' * 40)
        
        def handleLine(line, multi):
            if multi:
                mi = line.find('*/')
                if mi < 0:
                    return '', True
                
                return handleLine(line[mi+2:], False)
                
            ci, mi = line.find('//'), line.find('/*')
            
            if mi >= 0 and (ci > mi or ci < 0):
                
                ei = line.find('*/', mi + 2)
                if ei > 0:
                    left = line[:mi]
                    right, nmul = handleLine(line[ei + 2:], False)
                    return left + right, nmul
                else:
                    return line[:mi], True
            elif ci >= 0:
                return line[:ci], False
            else:
                return line, False
        
        ans = []
        i = 0
        multi = False
        while i < len(source):
            line = source[i]
            line, nmulti = handleLine(line, multi)
            # if len(line) > 0:
            if multi and not nmulti:
                if ans:
                    last = ans.pop()
                    ans.append(last+line)
                else:
                    ans.append(line)
            else:
                if len(line) > 0:
                    ans.append(line)
            multi = nmulti
            i += 1
                
        return ans
    
    
s = Solution()
# x = s.removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
# for row in x:
#     print(row)
# print('#' * 40)
# x = s.removeComments(source = ["a/*comment", "line", "more_comment*/b"])
# for row in x:
#     print(row)
# print('#' * 40)

# x = s.removeComments(source = ["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"])
# for row in x:
#     print(row)
# print('#' * 40)
# for x in ["class test{","public: ","   int x = 1;","   ","   char c;","};"]:
#     print(x)

#
#
# x = s.removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
# for row in x:
#     print(row)
# print('#' * 40)
#
# for x in ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]:
#     print(x)
#


x = s.removeComments(source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])
for row in x:
    print(row)
print('#' * 40)
for x in ["struct Node{","    ","    int size;","    int val;","};"]:
    print(x)