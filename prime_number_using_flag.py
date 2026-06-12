num = int(input("Enter a number to check the prime number: "))
flag =0
i=2
while i<num:

    if num % i == 0:
        flag = 1
        break
    i=i+1
if flag==0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
