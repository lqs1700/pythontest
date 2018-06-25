def maopao(aaa):
    for j in range(len(aaa)):
        for i in range(len(aaa)-j-1):
            if(aaa[i]>aaa[i+1]):
                aaa[i],aaa[i+1]=aaa[i+1],aaa[i]
    return aaa                     
bbb=[2,3,5,1,8,4,6,1,3,4,2]
sss=maopao(bbb)
print(sss)