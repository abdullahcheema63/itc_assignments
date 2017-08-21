#question 11
listA=[27,15,15,11,27,9,13,45,22,78,13,9]
index=0
smallest_element=0
largest_count=0
while index<=len(listA):
    index=0
    element=listA[index]
    count=listA.count(element)
    if count==largest_count and smallest_element>element:
        smallest_element=element
    if count>largest_count:
        smallest_element=element
        largest_count=count
    while element in listA:
        listA.remove(element)
    index+=1
print str(smallest_element)+" occurs "+str(largest_count)+" times"
