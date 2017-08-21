#question_2
originalList=[2,-16,2,0,-5,1]
index=0
filteredList=[]
while index<len(originalList):
    if originalList[index]>=0:
        filteredList.append(originalList[index])
    index+=1
print filteredList
