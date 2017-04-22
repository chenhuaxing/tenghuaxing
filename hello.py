#encoding:utf-8
a = 9
b = 2
a, b = b, a
print a, b



n = 4
if n >3:
    print "bigger"
    print "really bigger"
else : print "false bigger"
if n>7:
    print "smaller"
print "really smaller"

print [1,2,3] *2
numList=[8,2,1,5]
print sorted(numList)
print min(numList)
print max(numList)
for i in reversed(numList):
    print i
    print "你好"
aString="hello word"
bString="tomorrow"
listString=str(range(4))
print listString
print aString[1]
items=[('name','Mike'),('age','20')]
itemDict=dict(items)
list =([20,'age'],['Mike','name'])
ddict=dict(list)

dict={'name':'YingYing','password':233}
emptyDict={}
fDict={}.fromkeys(('id','score'))
print fDict
formDict={}.fromkeys(('x','y'),(-1,-2))
print formDict
firstSet=set([1,2,3])
secondSet=set([3,4,5])
print firstSet&secondSet




print cmp(1,2)
print int("123")
def my_abs(a,b):
    if a>b:
        return 1
    else:
        if a < b:
            return -1
        else:
            return 0
print my_abs(7,7)


class people ():
    def __init__(self,name,hair,height):
        self.name=name
        self.hair=hair
        self.height=height
    def printName(self):
        print 'my name is',self.name
    def printHair(self):
        print 'I have hair'
    def printHeight(self):
        print 'I have height'
NC=people('NC','black','tall')
NC.printName()

class boy(people):
    def printName(self):
        print 'i have a shabi name','it is',self.name
shabi=boy('mk','hair', 'ji')
shabi.printName()








with open('/home/chx/桌面/1.txt','r')as file:
    for line in file.read():
        print line
        print file.readline()