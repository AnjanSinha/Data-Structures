class Solution:
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            del nums[len(nums)-1]
        return nums

solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7],3))
