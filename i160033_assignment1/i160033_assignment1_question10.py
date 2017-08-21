#question_10
stars=6
space=1
backslash=0
forwardslash=12
output=""
while stars>0:
    print_stars=stars
    while print_stars>0:
        output+="*"
        #print"*",
        print_stars-=1
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        output+="/"
        #print "/",
        print_forwardslash-=1
    print_backslash=backslash
    while print_backslash>0:
        output+="\\"
        #print"\\",
        print_backslash-=1
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_stars=stars
    while print_stars>0:
        output+="*"
        #print"*",
        print_stars-=1
        
        
    #print (("*"*stars)+(" "*space)+(forwardslash*"/")+(backslash*"\\")+(" "*space)+("*"*stars))
    stars-=1
    space+=1
    backslash+=2
    forwardslash-=2
    #print "\n",
    output+="\n"
print output
