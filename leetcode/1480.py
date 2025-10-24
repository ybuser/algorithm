'''
1480. Running Sum of 1d Array
Easy

Topics
Array
Prefix Sum
Weekly Contest 193
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            newList[i] = (newList[i-1]+nums[i])
        return newList
