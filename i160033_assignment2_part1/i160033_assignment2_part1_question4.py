#question_4
def balance():
    even=0
    odd=0
    listA=[5,1,0,2,11]
    i=0
    if len(listA)==0:
        return True
    while i<len(listA):
        if listA[i]%2==0:
            even+=1
        if listA[i]%2!=0:
            odd+=1
        i+=1
    if even==odd:
        return True
    return False
balance()
