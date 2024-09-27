# #Enter a number from keyboard. Create a function to check weather that number is even or odd
# #n= int(input("Enter a number: "))
# def EvenOdd(n):
#     if n % 2 == 0:
#         return  "Even"
#     else:
#         return "Odd"
#
# print(EvenOdd(n))

#Take your name as input from the keyboard. Create a function which returns output in the following format--My name is (the name you have given as input)

# name = input("Enter a name: ")
# def printname(name):
#     return f'My name is {name}'
# print(printname("Rashmi"))
#
# #Take your name and age as input from the keyboard. Create a function which returns output in the following format--My name is (the name you have given as input) and I am (age) years old
#
# name1 = input("Enter a name: ")
# age = int(input("Enter age: "))
#
# def printname(name, age):
#     return f'My name is {name} and I am {age} old'
# print(printname("Rashmi", 25))

#You are writing a project in python for a hospital. Write a method which takes patient values.
#Below are conditions for passing values
#a)every patient gives name
#b)every patient gives blood group
#c)every patient gives what all the diseases suffering(may be suffering from multiple diseases).
#d)some patient gives email ids, some will not give
def patient(name, blood, *disease, email="defalut@gmail.com"):
    print(name, blood,disease, email)
patient("Rashmi","O-ve","no")

#Write a method which takes student values. Below are conditions for passing values
#a)every student has name
#b)some students may give 1 email id or 2 or more
#c)students will also give their house address in different formats.
def student(name, *email, **address):
    print(name,email, address)

student("Rashmi", "rashmi@gmail.com","house no= 123 ,Bangalore, karnataka")
