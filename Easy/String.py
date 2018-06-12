# -*- coding: utf-8 -*-
# Python 3.6.2 AMD 64
'''
Leetcode Primary Algorithm Practices (String)
@url: https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/
'''

class Solution:
    "1"
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s
    
    "2"
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            reverse_x = int(str(x)[::-1])
        else:
            reverse_x = int("-"+str(x)[::-1][:-1])

        if reverse_x <= 2**31-1 and reverse_x >=-2**31:
            return reverse_x
        else:
            return 0
    
    "3"
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_to_z = dict().fromkeys([chr(i) for i in range(97,123)],0)
        
        for ch in s:
            a_to_z[ch] += 1
        
        unique_char_dict = {k:s.find(k) for k,v in a_to_z.items() if v == 1}
        
        if len(unique_char_dict) <= 0:
            return -1
        else:
            return unique_char_dict[min(unique_char_dict, key=unique_char_dict.get)]
    
    "4"
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict().fromkeys([chr(i) for i in range(97,123)],0)
        t_dict = s_dict.copy()
        for ch in s:
            s_dict[ch] += 1
        for ch in t:
            t_dict[ch] += 1
        
        counter_ = {k:v for k,v in s_dict.items() if s_dict[k] != t_dict[k]}
        
        if len(counter_) > 0:
            return False
        else:
            return True 
    
    "5"
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s1 = re.sub("[^0-9a-zA-Z]","",s).lower()
        if s1 == s1[::-1]:
            return True
        else:
            return False
    
    "6"
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        import re
        s = s.strip()
        if len(s) <= 0:
            return 0
        elif s[0] not in [str(x) for x in range(10)]+["+","-"]:
            return 0
        try:
            if s[0] in ["+","-"]:
                num = int(float(re.findall("[\%s]+\d+"%(s[0]),s)[0]))
            else:
                num = int(float(re.findall("\d+",s)[0]))
        except:
            return 0
        num = min(num,2**31-1)
        num = max(num,-2**31)
        return num
    
    "7"
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # method: KMP algorithm
        if len(needle) == 0:
            return 0
        
        s,p = haystack,needle
        i,j,m,n = -1,0,len(s),len(p)
        next = [-1] * n
        # get array of next
        while j < n-1:
            if i == -1 or p[i] == p[j]:
                i,j = i+1,j+1
                next[j] = i
            else:
                i = next[i]
                
        # do matching
        i = j = 0
        while i < m and j < n:
            if j == -1 or s[i] == p[j]:
                i,j = i+1,j+1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1        

    
    
    

            
            
            