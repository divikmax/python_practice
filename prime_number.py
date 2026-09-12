# Prime Number Program in Python
num=int(input())
flag=0
for i in range(2,num):
    if(num%2==0):
        flag=1
    break
if(flag==1):
    print("It is not a prime number")
else:
    print("It is a prime number")
    