subject1=int(input("Enter marks of the first subject: "))
subject2=int(input("Enter marks of the second subject: "))
subject3=int(input("Enter marks of the third subject: "))
subject4=int(input("Enter marks of the fourth subject: "))
subject5=int(input("Enter marks of the fifth subject: "))

avg=(subject1+subject2+subject3+subject4+subject5)/5

if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")

else:
    print("Grade: F")