n=600851475143
lastFactor=1
if n%2==0:
    n=n/2
    lastFactor=2
    while n%2==0:
        n=n/2
factor=3
while n>1:
    if n%factor==0:
        n=n/factor
        lastFactory=factor
        while n%factor==0:
            n=n/factor
    factor=factor+2
print lastFactory
