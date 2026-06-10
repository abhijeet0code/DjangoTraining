# Taking input from the user first.
maths=int(input("Enter the marks of the maths :"))
computer=int(input("Enter the marks of the computer :"))
science=int(input("Enter the marks of the science :"))
hindi=int(input("Enter the marks of the hindi :"))
english=int(input("Enter the marks of the english :"))


# Checking the condition for the value correction.
if maths<=100 and computer<=100 and science<=100 and hindi<=100 and english<=100:
    if maths>=0 and computer>=0 and science>=0 and hindi>=0 and english>=0:

        # Taking the sum of all the numbers.
        sum = maths + computer + science + hindi + english
        print("The sum of the all the subjects are :- ", sum)

        # Calculating the percentage obtained by the student.
        pc = round((sum / 500) * 100)
        print("The total percentage of the subject is :-", pc)

        # Comparing the percentage of the students for the grade evalution
        if pc <= 100 and pc >= 91:
            print("Topper of the class")
        elif pc <= 90 and pc >= 81:
            print("1st grade marks")
        elif pc <= 80 and pc >= 71:
            print("2nd grade marks")
        elif pc <= 70 and pc >= 61:
            print("3rd grade marks")
        elif pc <= 60 and pc >= 41:
            print("Pass")
        elif pc <= 40 and pc >= 33:
            print("Promoted")
        elif pc <= 32 and pc >= 0:
            print("Fail")

    else:
        print("Please cross-check your entered marks again its smaller than 0 itself:-")
else:
    print("Please cross-check your entered marks again its greater than 100 itself:")