import mysql.connector as my

connection = my.connect(host="localhost", username="root", password="Naman@123", database="todo")

if connection.is_connected():
    print("\nConnection Established")
else:
    print("\nConnection failed")

#Create table for todo app named task
task="Create table if not exists task(taskname text, mobile text)"
#Create Cursor to execute mysql querry
mycursor = connection.cursor()
#To execute the create task table in databse todo
mycursor.execute(task)
#To commit or save the mysql  querry
connection.commit()

#To insert data in todo database
insertTask="Insert into task values('{}','{}')".format(input("Enter task name: "),input("Enter Mobile number: "))

#To execute the insert query
mycursor.execute(insertTask)

#To save the operation
connection.commit()

# #Update the task in DataBase
# #Here task is Table name
# updateTask="Update task set taskname= 'Do not Play on Xbox' where mobile='9680685948'"

# mycursor.execute(updateTask)
# connection.commit()

# #Delete the task in database
# deleteTask="delete from task where mobile= '8920xxxxxx'"
# mycursor.execute(deleteTask)
# connection.commit()

myTask="select * from task"

mycursor.execute(myTask)
print(mycursor.fetchall())
connection.commit()

# #Drop task in Database
# dropTask="drop table task"
# mycursor.execute(dropTask)
# connection.commit()