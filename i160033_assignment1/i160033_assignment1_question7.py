#question_7
count=4
number=1
output="";
while count>=0:
    space=count
    while space>0:
        #print " ",
        output+=" "
        space-=1
    number_multiple=number
    while number_multiple>0:
        output+=str(number)
        #print number,
        number_multiple-=1
    #print ((" "*count)+(str(number)*number)),
    count-=1
    number+=1
    #print "\n",
    output+="\n"
    
print output