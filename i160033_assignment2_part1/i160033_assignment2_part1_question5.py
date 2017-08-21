#question5
listA=[2,3,7,45,55,22,8,2,5]
listB=listA
i=0
while i<len(listA):
    if listB.pop(i) in listA:
        out= "True"
    else:
        out= "false"
    i+=1
print out

