def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    map1 = {}
    map2 = {}
    for i in range(len(s)) :
        map1[s[i]] = 1+map1.get(s[i],0)
        map2[t[i]] = 1+map2.get(t[i],0)

    

    for i in map1:
        if map1[i] != map2[i]:
            return False
    return True




print(isAnagram("anagram","nagaram"))
