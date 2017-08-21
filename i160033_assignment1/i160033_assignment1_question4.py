#question_4
s0=float(input("enter s0: "))
v0=float(input("enter v0: "))
t=float(input("enter t: "))
a=float(input("enter a: "))
acceleration_part=float((0.5*(a*(t**2))))
velocity_part=float(v0*t)
result=s0+velocity_part+acceleration_part
print result
