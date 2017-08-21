#question_3
exclaimation=22
backslash=0
forwardslash=0
while exclaimation>=2:
    print_backslash=backslash
    while print_backslash>0:
        print"\\",
        print_backslash-=1
    print_exclaimation=exclaimation
    while print_exclaimation>0:
        print "!",
        print_exclaimation-=1
    print_forwardslash=forwardslash
    while print_forwardslash>0:
        print"/",
        print_forwardslash-=1
    #print ((backslash*"\\")+(exclaimation*"!")+(forwardslash*"/"))
    exclaimation-=4
    backslash+=2
    forwardslash+=2
    print"\n",
