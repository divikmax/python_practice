#Check Whether or Not the Two Numbers are Friendly Pairs
# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# As the ratio of both the number match, they are considered as a friendly pair.
num1= int(input())
num2=int(input())
fact1=[]
fact2=[]
for i in range(1,num1):
    if num1%i==0:
        fact1.append(i)
for j in range(1,num2):
    if num2%j==0:
        fact2.append(j)
sum1=0
sum2=0
for x in fact1:
    sum1=sum1+x
for y in fact2:
    sum2=sum2+y
if (num1%sum1==num2%sum2):
    print("A Friendly Pair")
else:
    print(" Not a Friendly Pair")