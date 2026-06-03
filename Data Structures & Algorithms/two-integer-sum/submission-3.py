class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            l = target - nums[i]
            for j in range(i,len(nums)):
                if i!=j and l == nums[j]:
                    ans = [i, j]
                    break
        return ans