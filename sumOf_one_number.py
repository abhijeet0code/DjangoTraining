num=int(input("Enter a multi-digit number -: "))
sum=0

while num>0:
    one_num=num%10
    sum=sum+one_num
    num=num//10

print(f"The sum is {sum}")