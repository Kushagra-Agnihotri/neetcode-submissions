class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {x:0 for x in s}

        set2 = {x:0 for x in t}
        n1 = len(s)
        n2 = len(t)
        for i in s:
            set1[i]+=1
        for i in t:
            set2[i]+=1
        if n1 != n2:
            return False
        else: 
            for x in set1:
                if set1.get(x,0) != set2.get(x,0):
                    return False
        return True