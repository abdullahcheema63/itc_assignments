#question_9
output=""
c_space=0
while c_space<2:
    space=9
    while space>0:
        output+=" "
        space-=1
    output+="|"
    c_space+=1
output+="\n"
n_count=0
while n_count<2:
    number=1
    while number<=9:
        output+=str(number)
        number+=1
    output+="0"
    n_count+=1
print output