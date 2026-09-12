# Check Whether or Not the Number is an Abundant Number 
#sum of the factor should be greater than the number itself
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.
from math import sqrt

num = int(input())
fact=[]
for i in range(1,num):
    if(num%i==0):
        fact.append(i)
print(fact)

sum = 0

for i in fact:
    sum = sum + i

if sum > num:
    print("It is an Abundant Number")
else:
    print("It is not an Abundant Number")