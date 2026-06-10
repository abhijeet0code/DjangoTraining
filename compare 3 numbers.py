a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))

print("a=",a,"b=",b,"c=",c)

# Comparing without the logical operator
if a==b:
    print("a is equal to b")
    if b==c:
        print("a=",a,"b=",b,"c=",c,"are equal to each other")
    else:
        if(b>c):
            print("b=",b,"and a=",a,"is greater than c=",c)
        else:
            print("c is greater than b=",b,"and a=",a)
elif b==c:
    print("b=",b,"and c=",c,"are equal to each other")
    if b>a:
        print("b=",b,"and c=",c,"is greater than a=",a)
    else:
        print("a",a, "is greater than c=",c,"and b=",b)

else:
    if a > b:
        print("a =", a, " is greater than b =", b)
        if a > c:
            print("a =", a, " is greater than c =", c)
            print("a=", a, "is greatest number than the b=", b, "and c=", c)
        else:
            print("c=", c, "is greatest number than the b=", b, "and a=", a)
    else:
        print("b=", b, "is greater than a =", a)
        if b > c:
            print("b=", b, "is greater than c =", c)
            print("b=", b, "is greatest number than c=", c, "and a=", a)
        else:
            print("c=", c, "is greatest number than a =", a, "and b=", b)
