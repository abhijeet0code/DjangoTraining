num=int(input("enter the number to check the armstrong number :- "))
num2=num
o=num
add=0
mul=1

if num>=10:
    while num > 0:
        last_num = num % 10
        mul = mul * last_num
        num = num // 10
    while num2 > 0:
        one_num = num2 % 10
        add = add + one_num
        num2 = num2 // 10
    if mul == add:
        print(f"The multiply of {o} is {mul}")
        print(f"The sum of {o} is {add}")
        print(f"The {add} is equal to {mul}  ")
        print(f"{o} is a magic number")
    else:
        print(f"The multiply of {o} is {mul}")
        print(f"The sum of {o} is {add}")
        print(f"The {add} is not equal to {mul}  ")
        print(f"{o} is not a magic number")
else:
    print("A single value integer can't be entered ")