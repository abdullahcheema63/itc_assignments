#question_23
n=input("enter PAR: ")
if (n%20==0)or(n%6==0)or(n%9==0):
    print "convertible"
elif ((n%20)%6==0) or ((n%20)%9==0):
    print"convertible"
elif (((n%20)%6)%9==0) or (((n%20)%9)%6==0):
    print "convertible"
else:
    print "not convertible"
        
    