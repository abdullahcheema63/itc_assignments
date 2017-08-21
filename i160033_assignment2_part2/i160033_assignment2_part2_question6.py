#question 6
def output(wrongAttempts):
    line1and2="  +"+("-"*3)+"+  \n  |"+(" "*3)+"|  \n"
    if wrongAttempts<6:
        line3="  O"+" "*3+"|  \n"
    if wrongAttempts==6:
        line3="   "+" "*3+"|  \n"
    if wrongAttempts==5:
        line4=" "*6+"|  \n"
        line5=line4
    if wrongAttempts==4:
        line4="  |"+" "*3+"|  \n"
        line5=" "*6+"|  \n"
    if wrongAttempts==3:
        line4=" /|"+" "*3+"|  \n"
        line5=" "*6+"|  \n"
    if wrongAttempts==2:
        line4=" /|\\"+" "*2+"|  \n"
        line5=" "*6+"|  \n"
    if wrongAttempts==1:
        line4=" /|\\"+" "*2+"|  \n"
        line5=" /"+" "*4+"|  \n"
    if wrongAttempts==0:
        line4=" /|\\  |  \n"
        line5=" / \\  |  \n"
    line6and7=" "*6+"|  \n"+"="*9
    print line1and2+line3+line4+line5+line6and7
listOfWords=["Fast","programming","student","are","lazy","hangmen"]
otherList=[["F","_","s","_"],["_","_","_","g","_","_","m","m","_","_","g"],["_","_","u","d","_","_","t"],["a","_","e"],["l","_","_","y"],["_","_","n","g","_","_","n"]]
import random
wordSelector=random.randint(0,len(listOfWords)-1)
print "".join(otherList[wordSelector])
wrongAttempts=0
while wrongAttempts<7:
    
    if "_" not in otherList[wordSelector]:
        break
    guess=raw_input("enter any letter: ")
    if guess in listOfWords[wordSelector]:
        index=listOfWords[wordSelector].index(guess)
        otherList[wordSelector][index]=guess
        print "".join (otherList[wordSelector])
    else:
        output(wrongAttempts)
        wrongAttempts+=1
