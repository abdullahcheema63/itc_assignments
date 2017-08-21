#question_6
string=raw_input()
index=0
count=0
largest_count=0
last_count=0
string+="  "
while index<len(string):
    count+=1
    if largest_count<last_count:
        largest_count=last_count-1
        ending_index=index-1
    if string[index]==" ":
        last_count=count
        count=0
        index+=1
        continue
    index+=1
starting_index=ending_index-largest_count
print "largest substring is " +string[starting_index:ending_index]
