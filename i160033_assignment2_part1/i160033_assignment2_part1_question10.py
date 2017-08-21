#question10
listA=[27,15,15,11,27,9,13,45,22,78,13,9]
index=0
while index<=len(listA):
    index=0
    element=listA[index]
    count=listA.count(element)
    print str(element)+" occures "+str(count)+" times"
    while element in listA:
        listA.remove(element)
    index+=1
