#question_21
output=""
input_number=input()
previous_dots=input_number-1
count=1
next_dots=0
while count<=input_number:
    print_previous_dots=previous_dots
    while print_previous_dots>0:
        output+="."
        #print ".",
        print_previous_dots-=1
    output+=str(count)
    #print count,
    print_next_dots=next_dots
    while print_next_dots>0:
        output+="."
        #print ".",
        print_next_dots-=1
    output+="\n"
    #print "\n",
    #print ("."*previous_dots)+str(count)+"."*next_dots
    count+=1
    previous_dots-=1
    next_dots+=1
print output