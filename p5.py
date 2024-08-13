num=int(input())
count=0
while num>0:
    num=num//10
    count=count+1
print("the no of digits",count)
num=int(input())
sum=0
while num!=0:
    rem=num%10
    sum=sum+rem
    num=num//10

print(sum)
