#Conditional statement checks the condition as its true or false using if/else

#WAP to check whether user is eligible for voting or not.

age= int(input("Enter you age: "))

if age>=18:
    print("You're eligible for voting")
else:
    print("You're not eligible for voting")

#WAP to check whether user can sit in first compartment or not based on gender
gender= input("Enter your gender: ") #only in small letters.

if gender=="male":
    print("You cannot sit in first compartment")
elif gender=="female":
    print("you can sit in first compartment")
else:
    print("Fyou can't sit anywhere")    


#method 2 to use if/else statement (in one line)
print("You can sit in first compartment ") if gender=="female" else print("You cannot sit in first compartment")

#WAP if gender is female and age is greater than 18 then she can apply for govt. job
#also if hes male and greater than 18 he can apply for private job
gender2= input("Enter your gender: ")
age2= int(input("Enter your age: "))

#METHOD 1
if gender2=="male":
    if age2>=18:
        print("you can apply for private job")
    else:
        print("you can not apply for job since you're underage")    
elif gender2=="female":
    if age2>=18:
        print("You can aply for govt. job")
    else:
        print("You can not apply for job since you're underage")            

#METHOD 2
if gender2=="male" and age2>18:
    print("You can apply for private job")
elif gender2=="female" and age2>18:
    print("you can apply for govt. job")
else:
    print("You can not apply for any job")        