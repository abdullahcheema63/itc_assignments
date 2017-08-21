#question_8
string=raw_input()
bobs=0
index=0
while index<len(string):
    if string[index]=="b" and string[index-1]=="o" and string[index-2]=="b":
        bobs+=1
    index+=1
print bobs
