class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                del nums[i]
                nums.append(0)
        return nums
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0,0,1]))