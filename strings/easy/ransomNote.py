class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        magzine_dict = {}
        for i in magazine:
            if i in magzine_dict:
                magzine_dict[i]+=1
            else:
                magzine_dict[i]=1
        for char in ransomNote:
            if char not in magzine_dict:
                return False
            if magzine_dict[char]==0:
                return False
            magzine_dict[char]-=1
        return True
            
        