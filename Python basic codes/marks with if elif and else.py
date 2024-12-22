#WAP to accept percentage from user and make a decision about his grade.

marks=int(input("Enter your Percentage :"))
if marks>100:
    print("Enter vaild Percentage")
elif marks>=70:
    print("Your grade is O")
elif marks>=60:
    print("Your grade is A")
elif marks>=40:
    print("Your grade is B")
else:
    print("Your fail")
