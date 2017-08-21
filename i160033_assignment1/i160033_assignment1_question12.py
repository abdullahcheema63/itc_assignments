#question_12
#first straight line string
print_hyphen=7
output="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
#print "+"
output+="+\n"

#pattern1
space=4
forwardslash=0
backslash=0
while space>0:
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        output+="/"
        #print"/",
        print_forwardslash-=1
    output+="*"
    #print "*",
    print_backslash=backslash
    while print_backslash>0:
        output+="\\"
        #print "\\",
        print_backslash-=1
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    #print ((" "*space)+("/"*forwardslash)+"*"+("\\"*backslash)+(" "*space))
    space-=1
    backslash+=1
    forwardslash+=1
    output+="\n"
    #print "\n",
#pattern2
space=1
forwardslash=3
backslash=3
while space<5:
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_backslash=backslash
    while print_backslash>0:
        output+="\\"
        #print "\\",
        print_backslash-=1
    output+="*"
    #print "*",
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        output+="/"
        #print"/",
        print_forwardslash-=1
    
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    #print ((" "*space)+("/"*forwardslash)+"*"+("\\"*backslash)+(" "*space))
    space+=1
    backslash-=1
    forwardslash-=1
    output+="\n"
    #print "\n",

#second straight line string
print_hyphen=7
output+="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
#print "+"
output+="+\n"
#pattern2
space=1
forwardslash=3
backslash=3
while space<5:
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_backslash=backslash
    while print_backslash>0:
        output+="\\"
        #print "\\",
        print_backslash-=1
    output+="*"
    #print "*",
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        output+="/"
        #print"/",
        print_forwardslash-=1
    
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    #print ((" "*space)+("/"*forwardslash)+"*"+("\\"*backslash)+(" "*space))
    space+=1
    backslash-=1
    forwardslash-=1
    output+="\n"
    #print "\n",

#pattern1
space=4
forwardslash=0
backslash=0
while space>0:
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        output+="/"
        #print"/",
        print_forwardslash-=1
    output+="*"
    #print "*",
    print_backslash=backslash
    while print_backslash>0:
        output+="\\"
        #print "\\",
        print_backslash-=1
    print_space=space
    while print_space>0:
        output+=" "
        #print " ",
        print_space-=1
    #print ((" "*space)+("/"*forwardslash)+"*"+("\\"*backslash)+(" "*space))
    space-=1
    backslash+=1
    forwardslash+=1
    output+="\n"
    #print "\n",


#third straight line string
print_hyphen=7
output+="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
#print "+"
output+="+\n"
#print all
print output