from random import *

print("This is an number prediction game between 1 to 100, enter a number and see : -")
num=int(input("Enter a number :"))
ran_num=randint(1,100)

print(f"The random number is 😁😁😁 {ran_num}")
if num==ran_num:
    print(" \U0001F389\U0001F38A \u092C\u0927\u093E\u0908 \u0939\u094B! \u0906\u092A \u091C\u0940\u0924 \u0917\u090F! \U0001F38A\U0001F389")
    print(f"{num} is same as the random number {ran_num}")
else:
    print("\U0001F614\u274C \u0915\u094D\u0937\u092E\u093E \u0915\u0930\u0947\u0902! \u0906\u092A \u0939\u093E\u0930 \u0917\u090F! \u274C\U0001F614")