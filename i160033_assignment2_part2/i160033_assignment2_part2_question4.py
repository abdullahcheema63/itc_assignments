#question 4
def printStairs(stairs):
    count=0
    previous_space=stairs
    while count<stairs:
        print ("    "*(previous_space-1))+"  o  "+("*"*5)+("    "*count)+"*"
        print ("    "*(previous_space-1))+" /|\\ *"+("    "*(count+1))+"*"
        print ("    "*(previous_space-1))+" / \\ *"+("    "*(count+1))+"*"
        previous_space-=1
        count+=1
    print ((stairs*5)*"*")
printStairs(input())
