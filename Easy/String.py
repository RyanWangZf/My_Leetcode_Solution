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

    
    
    

            
            
            