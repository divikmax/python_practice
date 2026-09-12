#Find the Fibonacci Series up to Nth Term 
num=int(input())
term=int(input())
f=[0,1]
for i in range(0,num-2):
    f.append(f[i]+f[i+1])
print(*f)
print(f[term])