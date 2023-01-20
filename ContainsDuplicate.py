class Solution:
    def containsDuplicate(self, nums):
        items=[]
        for i in nums:
            if i in items:
                return True
            else:
                items.append(i)
        return False

solution = Solution()
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(solution.containsDuplicate([1,2,3,4]))