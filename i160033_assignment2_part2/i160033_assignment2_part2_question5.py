#question 5
def pattern1():
    count=1
    while count<=5:
        print " "+(" "*(5-count))+("/"*count)+"**"+("\\"*count)
        count+=1
def pattern2():
    dot=2
    slash=1
    while dot>=0:
        print "|"+("."*dot)+("/\\"*slash)+(".."*dot)+("/\\"*slash)+("."*dot)+"|"
        dot-=1
        slash+=1
def pattern3():
    dot=0
    slash=3
    while slash>0:
        print "|"+("."*dot)+("\\/"*slash)+(".."*dot)+("\\/"*slash)+("."*dot)+"|"
        slash-=1
        dot+=1

def finalPattern(length):
    pattern1()
    print "+"+("=*"*6)+"+"
    count=0
    while count<length:
        if count%2==0:
            pattern2()
            pattern3()
            print "+"+("=*"*6)+"+"
        if count%2!=0:
            pattern3()
            pattern2()
            print "+"+("=*"*6)+"+"
        count+=1
    pattern1()
finalPattern(input())
