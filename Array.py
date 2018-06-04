# -*- coding: utf-8 -*-
# Python 3.6.2 AMD 64
'''
Leetcode Primary Algorithm Practices (Array)
@url: https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/
'''

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)
 
def maxProfit(self, prices):
    
    """
    :type prices: List[int]
    :rtype: int
    """
    max_prof,d = 0,0
    for i in range(len(prices)):
        if i > 0:
            d = prices[i]-prices[i-1]
        if d>0:
            max_prof += d
            
    return max_prof
    
def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:n-k] = nums[:n-k][::-1]
    nums[n-k:] = nums[n-k:][::-1]
    nums.reverse()    
    