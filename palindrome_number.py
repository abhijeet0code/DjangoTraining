num=int(input("Enter a number to palindrome check"))
original=num
reverse=0
while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
if reverse==original:
    print(f"{original} is an palindrome number")
else:
    print(f"{original} is not a palindorme number")