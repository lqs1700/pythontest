def insert(aaa):
    for i in range(len(aaa)-1):
        p = i
        for i+1 in range(len(aaa)):
            if(aaa[p]>aaa[i+1]):
                p = i+1
        if(p!=i):
            aaa[p],aaa[i] = aaa[i],aaa[p]
    return aaa        
aaa = [2,1,5,4,3,7,9,8,2,3]
sss = insert(aaa)
print(sss)