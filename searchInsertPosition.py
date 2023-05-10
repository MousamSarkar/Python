class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #     vals = 0
        #     for index, value  in enumerate (nums):
        #         if target == value:
        #             vals = index
        #             break
        #     for i in range(0,len(nums)):
        #         if target > nums[len(nums)-1]:
        #             vals = len(nums)
        #             break
        #         elif i < len(nums)-1:
        #             if (target > nums[i]) & (target < nums[i+1]):
        #                 vals = i+1
        #                 break
        #     return vals

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r + l) // 2
            if target <= nums[mid]:
                r = mid - 1
            elif target >= nums[mid]:
                l = mid + 1
            else:
                return mid
        return l
