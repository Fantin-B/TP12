def product(a,b,i=0):

    if i == b :
        return 0
    return product(a,b,i+1) + a







print(product(5,2)) # 10
print(product(9,3)) # 27
