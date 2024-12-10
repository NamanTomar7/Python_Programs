import random
otp=random.randint(000000,100000)

send=int(input("Enter 1 to send otp else any key to exit: "))

if send==1:
    print("Your OTP for login is", otp)
else:
    exit()  

password=int(input("Enter OTP to login: "))

if password==otp:
    print("Welcome")
else:
    print("Login failed")