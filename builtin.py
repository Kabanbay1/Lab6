import time #only for 4th one
#1
x=input().split()
print(eval("*".join(x)))
#2
y=input()
print("Amount of uppercases: ",len([i for i in y if i.isupper()]) )
#3
z=input()
print(z==z[::-1])
#4
t=int(input())
ms=int(input())
mis=ms/1000
time.sleep(mis)
print("Square root of "+str(t)+" after "+str(ms)+" miliseconds is "+str(t**0.5))
#5
u=(True, True, True)
print(all(u))