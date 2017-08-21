#question_19
output=""
space=0
cheers=input("please enter the number of cheers: ")
lines=input("please enter the number of lines: ")
while lines>0:
    #print ((space*" ")+"go"+(" buddy go "*(cheers-1)))
    print_space=space
    while print_space>0:
        output+=" "
        print_space-=1
    output+="go"
    print_cheers=cheers-1
    while print_cheers>0:
        output+= " buddy go "
        print_cheers-=1
    output+="\n"
    lines-=1
    space+=1
print output