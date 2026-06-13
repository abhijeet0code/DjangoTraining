f=int(input("Enter the first number:"))
s=int(input("Enter the second number:"))
e=int(input("Enter the number of times you want to perform this :"))

t=0
i=1
while i<=e:
    t=f+s
    f=s
    s=t
    i=i+1
print(t)
