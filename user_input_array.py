from array import *
arr=array('i',[])
print(type(arr))

n=int(input("how many students in class"))
print("no of students=",n)

for i in range(n):
    marks=int(input("enter the marks"))
    arr.append(marks)

for i in arr:
    print(i)


sr=int(input("enter the number to search"))
for i in range(0,len(arr)):
    if arr[i]==sr:
        print(f"Value found {sr} at index {i}")
        break
else:
        print(f"Value is not found ")

max=arr[0]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]




print()
print(f"The minimum value of the array is {min}")
print(f"The maximum value of the array is {max}")