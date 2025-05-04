# print("Hello, World!")

# variables 
# fullName = "Amr"

# lastName = "elsherbiny"

# age = 19

# gpa = "0.0001"

# IsStudent = True

# print(f"Hello {fullName} { lastName} your age is {age} and your gpa is {gpa} and is you are student ? {IsStudent}")



# typecasting 
# price = 30.5  # float variable

# price = int(price) # convert to int

# print(price) # 30



# input default type  is string

# name = input("Enter your name: ") # input function will return string

# age = int(input("Enter your age: ")) # input function will return string and we convert it to int

# print (f"Hello {name} your age is {age}") 




# if statement

# age = int(input("Enter your age: "))


# if age < 18 :
#     print("You are a child")
# else: 
#     print("You are an adult")




# logic operators
# and , or , not

# and => &&    or => ||    not => !

# age = int(input("Enter your age: "))
# isStudent = input("Are you a student? (yes/no): ").lower() == "yes"

# if age < 18 and isStudent:
#     print("You are a child and a student")
# elif age < 18 and not isStudent:
#     print("You are a child and not a student")



# while loop

# i = 0 

# while i < 10:
#     print(i)
#     i += 1 # i = i + 1



# for loop count downt timer example 

# for i in range(10, 0, -1):
#     print(i)



# lists , tuples , sets like arrays 

#  lists => [] , tuples => () , sets => {}

# lists mutable , tuples immutable , sets unordered and unique

# lists

# fruits = ["apple", "banana", "orange", "grape"]

# print(fruits[0]) # apple

# fruits[0] = "mango" # change the first element to mango
# print(fruits[0]) # mango

# fruits.append("kiwi") # add kiwi to the end of the list

# fruits.remove("banana") # remove banana from the list
# for fruit in fruits:
#     print(fruit) # mango , banana , orange , grape


# tuples

fruits = ("apple", "banana", "orange", "grape")

# print(fruits[0]) # apple

# fruits[0] = "mango" # error: 'tuple' object does not support item assignment

for fruit in fruits:
    print(fruit) # apple , banana , orange , grape