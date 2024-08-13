'''l1=list(map(int,input().split(" ")))
esum=0
osum=0
for i in l1:
    if i%2==0:
        esum+=i
    else:
        osum+=i
print(esum,osum)'''
n=int(input())
l1=[0]*n
for i in range(n):
    l1[i]=int(input())
    print(end=" ")
esum=0
osum=0
for i in l1:
    if i%2==0:
        esum+=i
    else:
        osum+=i
print(esum,osum)

    
