fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(6):
  print(x)

for x in range(2, 30, 3):
  print(x)  

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#WAP to print the table of number taken by user.
n= int(input("Enter the number to print it's  table: "))
#Method 1
for x in range(n, n*11, n):
    print(x)

#method 2
for x in range(1,11):
    print((x)*(n))

#WAP to print even numbers from 1 to 10
#METHOD 1
for x in range(2,11,2):
    print(x)
#METHOD 2
for x in range(1,11):
    if x%2==0:
        print(x)    

#WAP to print this pattern 1 4 7 10 13
#METHOD 1
for x in range(1,14,3):
    print(x)

#WAP to print this pattern 1,3,7,11,13,15
for x in range(1,14,2):
    if x==9 or x==5:
        continue
    print(x)
