#Print Prime Numbers In a Given Range
num1=int(input())
num2=int(input())
primes=[]
for i in range(num1,num2+1):
    flag=0
    if i<2:
        continue
    if i==2:
        primes.append(2)
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
        break
    if flag==0:
        primes.append(i)
print(primes)
