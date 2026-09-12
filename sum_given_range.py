# Find the Sum of Numbers in a given Range in Python
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
sums=0
for i in range(num1,num2+1):
    sums=sums+i
print(sums)