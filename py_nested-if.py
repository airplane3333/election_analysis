#what is your grade
score = int(input("What is your test score"))
#Determine the letter grade nest loop
if score >= 90:
    print("Your grade is an A")
else:
    if score >=80:
        print("your grade is a B")
    else:
        if score >=70:
            print ("your grade is a C")
        else:
            if score >=60:
                print("your grade is a D")
            else:
                print("your grade is an F")
#using the same logic to write an if-elif-else

score = int(input("What is your test score"))
#Determine the letter grade nest loop
if score >= 90:
    print("Your grade is an A")
elif score >= 80:
    print("your score is a B")
elif score >=70:
    print("your score is a C")
elif score >=60:
    print("your score is a D")
else:
    print("your grade is a F")