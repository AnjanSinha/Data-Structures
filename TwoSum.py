#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#One Solution must present in the array
class Solution:
    def twoSum(self, num, target) :
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j]==target:
                    indicesArr = [i,j]
                    return indicesArr

solution = Solution()
print(solution.twoSum([2,7,11,15],9))