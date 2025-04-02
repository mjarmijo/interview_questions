"""
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m-1, n-1, m+n-1 # indexes of nums1 w/data, nums2, and all indicies in nums1

        while i >= 0 and j >=0:  # while i and j indicies
            if nums1[i] > nums2[j]:  # if nums 1 val > nums 2 val
                nums1[k] = nums1[i]  # set the last value equal to nums1 and deincrement i index
                i -= 1
            else:
                nums1[k] = nums2[j]  # else set the last value to nums2 and deincrement j
                j -=1
            k -=1

        while j >=0:
            nums1[k] = nums2[j]  # for remaining j,  set nums1 index k value equal to nums2 value, deincrement j/k counters --> matters when nums2 is longer than nums1 values
            j -=1
            k -=1
        

        # nums1[m:] = nums2
        # print(nums1)
        # for i in range(len(nums1)-1):
        #     print(i)
        #     if nums1[i] > nums1[i+1]:
        #         nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
        

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
print(s.merge(nums1, m, nums2, n))
print(nums1)

####################################################3


# """
# evaluate my submission in python for the following coding question. After you read the following question, prompt me and I will paste my submission.

# 88. Merge Sorted Array
# Easy
# Topics
# Companies
# Hint

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

# Constraints:

#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?
 
# ChatGPT said:

# Great! Please go ahead and paste your Python submission for the problem, and I'll be happy to evaluate it.
# You said:
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         # :type nums1: List[int]
#         # :type m: int
#         # :type nums2: List[int]
#         # :type n: int
#         # :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2
#         print(nums1)
#         for i in range(len(nums1)-1):
#             print(i)
#             if nums1[i] > nums1[i+1]:
#                 nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
        
# ChatGPT said:

# Your submission is a good starting point, but it has a few issues that need to be addressed to meet the problem's requirements efficiently. Let's go through the main points:
# Issues:

#     Inefficient Sorting Approach:

#         You're currently using a loop to swap adjacent elements (bubble sort) if they are out of order. This approach has a time complexity of O(n²), which is not optimal. The problem asks for an O(m + n) solution, which suggests you need to merge the arrays without performing a full sort.

#     Inefficient List Slicing:

#         nums1[m:] = nums2 copies nums2 into nums1 starting from index m, which works, but this results in unnecessary copying. While it simplifies some of the merging logic, it still creates inefficiencies.

#     Misuse of the "in-place" requirement:

#         You are modifying nums1 in-place, which is good, but the method still sorts the entire array after replacing the zeros with nums2, which is not the most efficient way.

# What Needs to be Done:

# You need to merge nums1 and nums2 in-place while maintaining the O(m + n) time complexity. The most efficient way to approach this is to start from the end of both nums1 and nums2, and merge them backwards. This way, you don't need to move elements multiple times, and you can avoid additional sorting.
# Suggested Solution:

# Here’s an optimized solution that performs the merge in O(m + n) time:

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         # :type nums1: List[int]
#         # :type m: int
#         # :type nums2: List[int]
#         # :type n: int
#         # :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         # Start filling nums1 from the end
#         i, j, k = m - 1, n - 1, m + n - 1
        
#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1
        
#         # If there are remaining elements in nums2, copy them over
#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

# Explanation:

#     Pointers:

#         i is the index for the last element of the initialized part of nums1.

#         j is the index for the last element of nums2.

#         k is the index for the last position in the nums1 array (which can accommodate all elements after merging).

#     Merging:

#         We compare the elements at nums1[i] and nums2[j]. The larger element is placed at nums1[k], and we move the corresponding pointer (i or j) backward.

#     Leftover Elements:

#         If there are still elements in nums2 (i.e., j >= 0), we directly copy them to nums1. No need to check nums1 because any remaining elements in nums1 are already in the correct place.

# Time Complexity:

#     The merging process runs in O(m + n) because we iterate through both arrays once, and there's no nested iteration like in your original approach.

# Space Complexity:

#     O(1), since we're modifying nums1 in place and not using any extra data structures (apart from a few variables).

# This solution efficiently merges nums1 and nums2 with the desired time and space complexity.