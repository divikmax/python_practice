#Find the Prime Factors of a Number in Python
# Example
# Input : 10
# Output : 2 5
num=int(input())
factors=[]
for i in range(2,num):
    if num%i==0:
        factors.append(i)
for j in factors:
    count=0
    for k in range(2,j):
        if j%k==0:
            count=count+1
    if count==0:
        print(j)


