#question7
string=raw_input()
index=0
vowels=0
while index<len(string):
    if string[index] in "aeiou":
        vowels+=1
    index+=1
print "number of vowels: "+str(vowels)
