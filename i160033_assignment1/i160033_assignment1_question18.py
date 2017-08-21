#question_18
fee=7000
stationary_charges=10000
materials_cost=6000
final_payment=0
sibblings=""
while True:
    grade=input("please enter grade: ")-1
    if sibblings=="yes":
        fee-=0.1*fee
    while grade>0:
        fee+=0.15*fee
        materials_cost+=1000
        grade-=1
    sibblings=raw_input("do you have annother sibblings: ")
    if sibblings=="yes":
        final_payment+=stationary_charges+materials_cost+fee
        materials_cost=6000
        fee=7000
        continue
    else:
        break
print final_payment