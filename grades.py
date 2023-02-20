print("FORM 4 GRADING SYSTEM")
print("this system allows numbers only")


grade=float(input("Enter your Grade"))
if grade >=90:
    print("You got an A")
elif grade<=89 and grade>=80:
    print("you have a B")
elif grade<=79 and grade>=70:
    print("you have a C")
elif grade <= 69 and grade >= 60:
    print("you have a D")
elif grade <= 59 and grade >= 50:
    print("you have an E")
elif grade <= 49 and grade >= 40:
    print("below average")

else:
    print("please retake the exerms")