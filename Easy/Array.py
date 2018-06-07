# -*- coding: utf-8 -*-
# Python 3.6.2 AMD 64
'''
Leetcode Primary Algorithm Practices (Array)
@url: https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/
'''
class Solution:
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
        for num in nums2:
            if counter.get(num) and num in counter:
                res.append(num)
                counter[num] -= 1
        return res        

    "7"
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        real_num = int("".join([str(n) for n in digits]))
        real_num += 1
        new_digits = [int(n) for n in str(real_num)]
        return new_digits
        
    "8"
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_all = len(nums)
        num_nonzero = len([n for n in nums if n!=0])
        num_zero = num_all - num_nonzero
        for i in range(num_zero):
            nums.remove(0)
            
        nums.extend([0]*num_zero)

    "9"
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = dict(zip(nums,list(range(len(nums)))))
        
        for i in range(len(nums)):
            diff_ = target - nums[i]
            if diff_ in hash_dict and hash_dict[diff_] != i:
                return [i,hash_dict[diff_]]
    
    "10"
    def isValidSudoku(self,board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flat = lambda x: [y for l in x for y in flat(l)] if isinstance(x,(list,tuple)) else [x]
        
        for i in range(9): # rows
            row = [r for r in board[i] if r != "."]
            if len(list(set(row))) - len(row) < 0 : # have duplicate numbers
                return False
                                
        for i in range(9): # cols
            col = [c[i] for c in board if c[i] != "."]
            if len(list(set(col))) - len(col) < 0 : # have duplicate numbers
                return False
                            
        for i in range(3): # 3 x 3 small cells
            cell = board[i*3:(i+1)*3]
            for j in range(3):
                small_cell = [cell[k][j*3:(j+1)*3] for k in range(3)]
                small_cell = [n for n in flat(small_cell) if n != "."]
                if len(list(set(small_cell))) < len(small_cell): # have duplicate numbers
                    return False
        return True
    
    "11"
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        # Normal method1:
        num_row = len(matrix)
        for i in range(len(matrix)):
            col = [matrix[j][i] for j in range(len(matrix[i]))][::-1]
            matrix.append(col)
        for n in range(num_row):
            matrix.pop(0)
        # Normal method2:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        """      
        
        # Pythonic method:
        matrix[:] = list(map(list,zip(*matrix[::-1])))
        
        
        