#question_16
import random
#random.random()
count=3
while True:
    while count>0:
        guess_number=int(random.random()*10)
        input_guess=input("guess the number: ")
        if input_guess<0 or input_guess>10:
            print("please enter values between 0 and 10: ")
            continue
        if input_guess==guess_number:
            print "you win"
            break
        count-=1
        print ("you have "+str(count)+" tries remaining")
    prompt=raw_input("enter yes to play again: ")
    if prompt=="yes":
        count=3
        continue
    elif prompt=="no":
        break
    elif (prompt!="yes")or (prompt!="no"):
        print "please enter yes or no"
        continue
        
    