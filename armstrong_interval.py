#Find the Armstrong Numbers between Two Intervals
num1=int(input())
num2=int(input())
for i in range(num1,num2+1):
    temp=i
    num=i
    result = 0
    while num > 0:
        rem = num % 10
        result = result + (rem ** 3)
        num = num // 10
    if result == temp:
        print(result)