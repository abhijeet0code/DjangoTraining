num = int(input("Enter the starting number: "))

i=2
while i <= num:
    if num % i == 0:
        print(f"{num} is an even number")
        break
    i=i+1
else:
    print(f"{num} is an prime number")
