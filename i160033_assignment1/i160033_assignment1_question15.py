#question_15

#seperating dd mm and yy
name1=raw_input("please enter first name: ")
name2=raw_input("please enter second name: ")
age1=input("please enter "+name1+"'s age in YYMMDD")
age2=input("please enter "+name2+"'s agein YYMMDD")
age1_yy=age1/10000
age1_mm=(age1/100)%100
age1_dd=age1%100
age2_yy=age2/10000
age2_mm=(age2/100)%100
age2_dd=age2%100

#printing age
print (name1+"'s age is "+str(age1_dd)+"/"+str(age1_mm)+"/"+str(age1_yy))
print (name2+"'s age is "+str(age2_dd)+"/"+str(age2_mm)+"/"+str(age2_yy))

#checking age
if age1_yy>age2_yy:
    print (name1+" is older then "+name2)
elif age2_yy>age1_yy:
    print (name2+" is older then "+name1)
elif age1_yy==age2_yy:
    if age1_mm>age2_mm:
        print (name1+" is older then "+name2)
    elif age2_mm>age2_mm:
        print (name2+" is older then "+name1)
    elif age1_mm==age2_mm:
        if age1_dd>age2_dd:
            print (name1+" is older then "+name2)
        elif age2_dd>age1_dd:
            print (name2+" is older then "+name1)
        elif age1_dd==age2_dd:
            print (name1+" and "+name2+" have the same age")