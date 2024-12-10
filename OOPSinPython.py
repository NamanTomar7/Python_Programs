#Class -> A container that collects variables , functions

#Syntax- 
class ClassName:
    print("This is a class")

class Naman:
    age=19
    fullName="Naman Tomar"
    email="namantomar776@gmail.com"
    def pocketmoney(this, amount):
        print("My Pocket money=",amount)
    def salary(this):
        am=int(input("Enter your per day salary"))
        monthlysalary=am*30
        print("Monthly Salary=", monthlysalary)

#Declaring class objects- 
n:Naman = Naman()
print("My name is",n.fullName,"And my age is",n.age) 
n.pocketmoney(4500)
n.salary()     