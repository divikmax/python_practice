#Check for Perfect Square 
#here square root 1/2 -->0.5
from math import sqrt
num = int(input())

root = int(num ** 0.5)
sqt=sqrt(25)
print(sqt)

if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")