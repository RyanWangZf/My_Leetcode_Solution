# -*- coding: utf-8 -*-
# Python 3.6.2 AMD 64
'''
Leetcode Primary Algorithm Practices (Array)
@url: https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/
'''

"1"
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

"2" 
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

"3"    
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

"4"    
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    set_num = set(nums)
    list_set_num = list(set_num)
    if len(list_set_num) == len(nums):
        return False
    else:
        return True 

"5"        
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]
    return xor        
    
"6"
def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    """
    # Pythonic:
    from collections import Counter
    nums_intersect = list((Counter(nums1)&Counter(nums2)).elements())

    return nums_intersect
    """
    # Normal:
    if len(nums1) < 1 or len(nums2) < 1:
        return []
    res = []
    counter = {}
    for num in nums1:
        counter[num] = counter.get(num,0) + 1        