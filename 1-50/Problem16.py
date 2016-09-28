import math
x=pow(2,1000)
print pow(2,10000)
print x
print str(x)
ss=0
for i in list(str(x)):
    print i, ord(i),eval(i)
    ss+=eval(i)
print ss
