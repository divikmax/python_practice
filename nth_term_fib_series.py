#Find the Nth Term of a Fibonacci Series  in Python.
#input Nth term 
num=int(input("Enter The Nth Term: "))
f=[0,1]
for i in range(2,num):
    f.append(f[i-1]+f[i-2])
print("the Nth Term of a Fibonacci Series:",f[num-1])


    
    
    