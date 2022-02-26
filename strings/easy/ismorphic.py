def ismorphic(s,t):
    mapS = {}
    mapT = {}
    for i,j in zip(s,t):
        if((i in mapS and mapS[i]!=j) or (j in mapT and mapT[j]!=i)):
            return False
        mapS[i] = j
        mapT[j] = i
    return True
    


print(ismorphic("badc","baba"))