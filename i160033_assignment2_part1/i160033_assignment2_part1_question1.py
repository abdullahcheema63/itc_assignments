#question1
v1=[]
v2=[]
v3=[]
v4=[]
v1_count=0
while v1_count<3:
    v1.append(input("please enter v1: "))
    v1_count+=1
v2_count=0
while v2_count<3:
    v2.append(input("please enter v2: "))
    v2_count+=1
v3_count=0
while v3_count<3:
    v3.append(input("please enter v1"))
    v3_count+=1
v4_count=0
while v4_count<3:
    v4.append(input("please enter v1"))
    v4_count+=1

k1=-5000
k2=-5000
k3=-5000
k4=-5000
while k4<=5000:
    k3=5000
    while k3<=5000:
        k2=-5000
        while k2<=5000:
            k1=-5000
            while k1<=5000:
                if (k1*v1[0])+(k2**v2[0])+(k3*v3[0])+(k4*v4[0]==0):
                    if (k1*v1[1])+(k2**v2[1])+(k3*v3[1])+(k4*v4[1]==0):
                        if (k1*v1[2])+(k2*v2[2])+(k3*v3[2])+(k4*v4[2]==0):
                            out="span"
                            break
                    else:
                        out="does not span"
                        continue
                else:
                    out="doesnot span"
                    continue
                k1+=1
            k2+=1
        k3+=1
    k4+=1
print out
