#question1
def secondLine(name):
    print "there was an old lady who swallowed a "+name
def thirdLine(name):
    print "i dont know why she swallowed that "+name
def firstLine():
    print "Perhaps she'll die"
def fourthLine(name1,name2):
    print "she swallowed that "+name1+" to catch that "+name2
    
secondLine("fly")
thirdLine("fly")
firstLine()
print "\n"
secondLine("spider")
print "that wriggled and iggled and jiggled inside her"
fourthLine("spider","fly")
thirdLine("fly")
firstLine()
print "\n"
secondLine("bird")
print "how absurd to swallow a bird"
fourthLine("bird","spider")
fourthLine("spider","fly")
thirdLine("fly")
firstLine()
secondLine("cat")
print "imagine that to swallow a cat"
fourthLine("cat","bird")
fourthLine("bird","spider")
fourthLine("spider","fly")
thirdLine("fly")
firstLine()
print "\n"
secondLine("dog")
print "what a hog to swallow a dog"
fourthLine("dog","cat")
fourthLine("cat","bird")
fourthLine("bird","spider")
fourthLine("spider","fly")
thirdLine("fly")
firstLine()
print "\n"
secondLine("horse")
print "she died of course"
