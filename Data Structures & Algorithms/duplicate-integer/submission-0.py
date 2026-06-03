class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d ={x:0 for x in nums}
        for i in nums:
            d[i]+=1
        for k,v in d.items():
            if v >1:
                return True
        return False