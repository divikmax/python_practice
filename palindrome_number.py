#palidrome_number
num=int(input())
original=num
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if(rev==original):
    print("it is palindrome")
else:
    print("it is not palindrome")