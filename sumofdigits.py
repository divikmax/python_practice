#sum of digits
num=int(input())
sums=0
while(num>0):
    rem=num%10
    sums=sums+rem
    num=num//10
print(sums)
