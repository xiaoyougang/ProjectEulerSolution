import time
def f(n):
    if n%2==1 and n>1:
        return f(3*n+1)+1
    elif n%2==0:
        return f(n/2)+1
    return 1
m,value=0,0
begin=time.time()
for i in range(1,1000000):
    tmp=f(i)
    if tmp>m:
        value=i
        m=tmp
print time.time()-begin
print m,value
