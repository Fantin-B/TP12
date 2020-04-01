def listSum(l,i=0):

    if len(l) == i:
        return 0
    return listSum(l,i+1) + l[i-1]

    #r = l[i-1]                              # Méthode pour mieux comprendre comment ça fonctionne avec le débeuguage
    #return listSum(l,i+1) + r               # car dans le 1er tour, r = dernier élément de la liste, puis 2eme tour r = 1er élément
                                             # puis 3eme tour = 2eme élément , .....

def listSumHugo(l):
    if len(l)==0:
        return 0
    return listSumHugo(l[1:]) +l[0]




print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11

print(listSumHugo([])) # 0
print(listSumHugo([42])) # 42
print(listSumHugo([3,1,5,2])) # 11
