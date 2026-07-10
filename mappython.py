a=list(map(int,input("Enter a number").split()))
b=a if len(a)<=4 else "The value is more than four digits"
print(b)