#question_8
output=""
top_underscore=0
while top_underscore<=40:
    output+="_"
    #print"_",
    top_underscore+=1
output+="\n"
#print"\n",
pattern=0
while pattern<=9:
    output+="_-^-"
    #print "_-^-",
    pattern+=1
output+="\n"
#print "\n"
numbers_count=0
while numbers_count<2:
    numbers=0
    while numbers<=9:
        output+=str(numbers)+str(numbers)
        #print str(numbers)+str(numbers),
        numbers+=1
    numbers_count+=1
output+="\n"
#print "\n",
bottom_underscore=0
while bottom_underscore<=40:
    output+="_"
    #print"_",
    bottom_underscore+=1
output+="\n"
print output
#print"\n",