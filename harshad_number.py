# Check Whether or Not a Number is a Harshad Number in Python
# Given an integer input the objective is to check whether or not the given number is a Harshad Number or not. 
# To do so we’ll check if the sum of the digits can perfectly divide the number or not. 
num=int(input())
nums=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
if(nums%sum==0):
    print("It is a Harshad Number")
else:
    print("It is not a Harshad Number")