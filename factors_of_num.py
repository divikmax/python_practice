#factors of a number
num=int(input())
fact=[]
for i in range(2,num):
    if(num%i==0):
        fact.append(i)
print(fact)