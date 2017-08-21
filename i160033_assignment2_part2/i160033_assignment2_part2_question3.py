#question 3
def christmas(segments,height):
    stars=1
    #segments=5
    count=0
    out=""
    #height=7
    ps=height
    while count<segments:
        heigh=height
        stars=1+(2*count)
        out=""
        space=heigh
        while heigh>0:
            out+=ps*" "
            out+= (space*" ")+("*"*stars)+"\n"
            space-=1
            stars+=2
            heigh-=1
        print out,
        count+=1
        stars+=2
        ps-=1
christmas(input(),input())

