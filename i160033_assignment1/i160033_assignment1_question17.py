#question_17
binary=raw_input()
index=0
result=0
power=len(binary)-1
while index<len(binary):
    result+=int(binary[index])*(2**power)
    index+=1
    power-=1
print result
