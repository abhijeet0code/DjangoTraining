num=int(input("Enter the number of factorial you want :"))
num1=num
f=1

i=1
while i<=num1:
    f=f*num
    num=num-1
    i=i+1
print(f"factorial of the number is {f}")