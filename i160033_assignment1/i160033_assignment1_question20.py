#question_20
print "v"
output=""
overall_count=0
while overall_count<2:
    
    count=1
    while count<=5:
        print_v=count
        while print_v>0:
            output+="v"
            print_v-=1
        #print "v"*count
        count+=1
        output+= "\n"
    if count==5:
        count=4
    while count>0:
        print_v2=count
        while print_v2>0:
            output+= "v"
            print_v2-=1
        count-=1
        output+="\n"
    output+="v"
    overall_count+=1
print output