start=int(input("Enter the starting number"))
end=int(input("Enter the ending number"))
even=0
odd=0
i=start
if start<=end:
    while i<=end:
        if i%2 == 0:
            print(f"{i} is an Even Number ")
            even = even + i
        else:
            print(f"{i} is an Odd Number ")
            odd = odd + i
        i=i+1
    print(f"The sum of all the even numbers is {even}")
    print(f"The sum of all the odd numbers is {odd}")
else:
    while i>=end:
        if i%2 == 0:
            print(f"{i} is an Even Number ")
            even = even + i
        else:
            print(f"{i} is an Odd Number ")
            odd = odd + i
        i=i-1
    print(f"The sum of all the even numbers is {even}")
    print(f"The sum of all the odd numbers is {odd}")