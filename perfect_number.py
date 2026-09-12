#perfect number
num=int(input())
number=num
div=[]
for i in range(1,num):
    if(num%i==0):
        div.append(i)
sum=0   
for i in range(len(div)):
    sum=sum+div[i]
print(sum)
if (number==sum):
    print("It's a Perfect Number")