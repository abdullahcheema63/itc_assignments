#question_3
listOriginal=[2,1,10,4,3,6,7,9,8,5]
listShiifted=[0,0,0,0,0,0,0,0,0,0]
i=0
while i<len(listOriginal):
    j=i+1
    if i==len(listOriginal)-1:
        j=0
    listShiifted[j]=listOriginal[i]
    i+=1
listOriginal=listShiifted
print listOriginal
