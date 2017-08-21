#question_13
x=0
y=0
function=((1-x)**2)+(100*((y-(x**2))**2))

minimum=999999999
while y<1000:
    while x<1000:
        function=((1-x)**2)+(100*((y-(x**2))**2))
        if function<minimum:
            minimum=function
        x+=1
    y+=1
    x=0
print minimum