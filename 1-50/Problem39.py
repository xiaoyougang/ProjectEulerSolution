ans = 0
maxp = 0

for i in range(12, 1000):
    maxc=0
    for a in range(1, i):
        for b in range(1, a):
            c=i-a-b
            if c<0:
                break
            if (a*a+b*b==c*c):
                maxc+=1
    if maxc>ans:
        ans=maxc
        maxp=i
print ans, maxp

