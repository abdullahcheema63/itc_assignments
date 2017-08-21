#question_11 final
print_hyphen=6
output="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
#print "+"
output+="+\n"
#question_11 d
count1=0
while count1<2:
    #question_11 PART1
    space_sides=2
    space_between=0
    while space_sides>=0:
        output+="|"
        #print "|",
        print_space_sides=space_sides
        while print_space_sides>0:
            output+=" "
            #print " ",
            print_space_sides-=1
        output+="^"
        #print "^",
        print_space_between=space_between
        while print_space_between>0:
            output+=" "
            #print " ",
            print_space_between-=1
        output+="^"
        #print "^",
        print_space_sides=space_sides
        while print_space_sides>0:
            output+=" "
            #print " ",
            print_space_sides-=1
        output+="|"
        #print "|",
        #print ("|"+(" "*space_sides)+"^"+(space_between*" ")+"^"+(space_sides*" ")+"|")
        space_sides-=1
        space_between+=2
        output+="\n"
        #print "\n",

    count1+=1
print_hyphen=6
output+="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
output+="+\n"
#print "+"

#question_11 parte
count2=0
while count2<2:
    #question_11 PART2
    space_sides=0
    space_between=4
    while space_between>=0:
        output+="|"
        #print "|",
        print_space_sides=space_sides
        while print_space_sides>0:
            output+=" "
            #print " ",
            print_space_sides-=1
        output+="v"
        #print "v",
        print_space_between=space_between
        while print_space_between>0:
            output+=" "
            #print " ",
            print_space_between-=1
        output+="v"
        #print "v",
        print_space_sides=space_sides
        while print_space_sides>0:
            output+=" "
            #print " ",
            print_space_sides-=1
        output+="|"
        #print "|",


        #print ("|"+(" "*space_sides)+"v"+(space_between*" ")+"v"+(space_sides*" ")+"|"),
        space_sides+=1
        space_between-=2
        output+="\n"
        #print "\n",
    count2+=1
    

print_hyphen=6
output+="+"
#print "+",
while print_hyphen>0:
    output+="-"
    #print "-",
    print_hyphen-=1
output+="+"
#print "+"
print output