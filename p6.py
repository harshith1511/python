str1=input()
str2=input()
l1=[]
for i in str1:
    for j in str2:
        if i==j:
            l1.append(i)
if len(str1)==len(l1):
    print("True")
else:
    print("False")
