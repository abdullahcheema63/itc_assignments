#question_22
while True:
    squares=input("enter the number of squares to draw: ")
    count=1
    area=0
    if squares<0:
        print ("please enter positive values")
        continue
    while count<=squares:
        square_output=""
        width=input("enter width "+str(count)+": ")
        height=input("enter height"+str(count)+": ")
        if height<0 or width<0:
            print("please enter positive values")
            continue
        area+=height*width
        while height>0:
            width_multiplication=width
            while width_multiplication>0:
                square_output+="*"
                width_multiplication-=1
            square_output+="\n"
            #print("*"*width)
            height-=1
        count+=1
        print square_output

    print ("the area of squares is "+str(area))
    break