#armstrong number
number = int(input())

num = number
result = 0

while num > 0:
    rem = num % 10
    result = result + (rem ** 3)
    num = num // 10
if result == number:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")