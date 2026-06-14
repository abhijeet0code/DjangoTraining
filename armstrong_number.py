num=int(input("enter the number to check the armstrong number :- "))
original=num
mul=0

while num>0:
    last_num=num%10
    mul=mul+last_num**3
    num=num//10
if mul==original:
    print(f"The cube and sum of each number is {mul}")
    print(f"{original} is an armstrong number")
else:
    print(f"The cube amd sum of each number is {mul}")
    print(f"{original} is not an armstrong number")
