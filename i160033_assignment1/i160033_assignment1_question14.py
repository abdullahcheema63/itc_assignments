#question_14
series_1=2
series_2=1
count=1
out=""
while count<=10:
    out+=(str(series_1**2)+","+str(series_2**2)+",")
    count+=1
    series_1+=2
    series_2+=2
print out