#question7
def line():
    count=0
    while count<4:
        print "            ||"
        count+=1
def pattern1():
    colon=0
    space=9
    while colon<=9:
        print (space*" ")+"__/"+(":"*colon)+"||"+(":"*colon)+"\__"
        colon+=3
        space-=3
    print "|"+("\""*24)+"|"

line()
pattern1()


pattern2=10
space_pattern2=0
while pattern2>=4:
    print (space_pattern2*" ")+"\_/"+("\/"*pattern2)+"\_/"
    pattern2-=2
    space_pattern2+=2
line()
pattern3=0
while pattern3<17:
    print (" "*9)+"|%%||%%|"
    pattern3+=1
pattern1()
