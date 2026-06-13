wm= 1000
token=int(input("Enter your amount of token: "))
i=1
if token<=wm:
    while i<=token:
        print(f"toffe {i}")
        wm=wm-1
        i=i+1
    else:
        print("Thank you for visiting ")
    print(f"you have {wm} toffe left")
else:
    print(f"The amount of toffe {token} is not present in the stack")