#Check Whether or Not the Number is a Strong Number in Python
# Example
# Input : 145
# Output : It's a Strong Number
#A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.
num=int(input())
sum=0
fact=1
fac=[]
while(num>0):
    last=num%10
    for i in range(1,last):
        fact=fact*i
    fac.append(fact)
    fact=0
    num=num//10
print(fac)
