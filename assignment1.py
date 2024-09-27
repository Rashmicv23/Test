# #1.Generate first 100 numbers using range function
# print(list(range(1,101)))
#
# #2.Generate first 15 odd and even numbers using range function
# print(list(range(0,31,2)))
# print(list(range(1,31,2)))
#
# #3.Generate the following sequence 16,8,0,-8,-16,-24
# print(list(range(16,-25,-8)))
#
# #4.Generate the following sequence 1,5,9,13.....77
# print(list(range(1,78,4)))
#
# #1. store 100,200,300,400 in a list and print
# li = [100,200,300,400]
# print(li)
#
# #2. store 1, ramesh, 20000.50 in a tuple and print
# tp = (1, 'ramesh', 20000.5)
# print(tp)
#
# #store some email addresses in a set and print
# s = {"rashmi@hmail.com", "rcv@gamil.com"}
# print(s)
#
# x = {
#     'eno' : 1,
#     'ename' : 'srikrishna',
#     'esal': 30000
# }
#
# #1.print eno ,ename and esal values
# print(x)
#
# #2.update esal =50000 and print esal value
# x['esal'] = 50000
# print(x)
#
# #3.add one more data place=‘bangalore’
# x['place'] = 'Bangalore'
# print(x)
#
# #1,5,9,13,17..25
# num = 1
# while num<=25:
#     print(num)
#     num = num + 4
# print("--------------------")
# #1,5,25,125,625,3125
# num1 = 1
# while num1<=3125:
#     print(num1)
#     num1 =num1*5
# print("----------------")
# #128,32,8,4,1
# num2 = 128
# while num2>=1:
#     print(num2)
#     num2 = num2 // 4
# print("--------------")
# #36,30,24,18...0
# num3 = 36
# while num3>=0:
#     print(num3)
#     num3 = num3 - 6
#
# #1.Take a number as input from the keyboard and check weather that number is a palindrome number
# #num = int(input("Enter a number: "))
# original_num = num
# reversed_num = 0
# while num>0:
#     r = num % 10
#     reversed_num = (reversed_num * 10) + r
#     num = num //10
#
# if(original_num == reversed_num):
#     print("Number is palindrome")
# else:
#     print("Not palndrome")
#
# #2. 1,1,2,3,5,8,13,21,34,55,89 Fibonacci series
# nterms = 12
# n1, n2 = 0, 1
# count = 0
# while(count < nterms):
#     print(n1)
#     n3 = n1 + n2
#     n1=n2
#     n2=n3
#     count = count +1
#
# #3. Take a number as input from keyboard and check weather it's prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num//2):
        if(num % i) == 0:
            print("Not prime number")
            break
    else:
            print("Prime number")
else:
            print("Not prime number")
#
# #4. Take an year as input from keyboard and check weather it's a leap year or not
# #year = int(input("Enter a year: "))
# # if((year % 400 == 0) or (year % 100!=0) and (year % 4 == 0)):
# #     print("Leap year")
# # else:
# #     print("Not leap year")
#
# #Take a number from keyboard and check weather it's even or odd?
# #n = int(input("Enter a number: "))
# if(n%2==0):
#     print("even")
# else:
#     print("odd")

li=[1,3,2,10,5,6]
for i in range(len(li)-1,-1,-1):
    print(li[i])

print("-------------")

for i in range(len(li)-1,-1,-1):
    if(i%2==0):
        print(li[i])

#Read the 2 numbers from keyboard and find biggest number
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# if(num1>num2):
#     print(num1)
# else:
#     print(num2)

#Read a num from keyboard and print day name: if user enters 1 print Monday

day = int(input("Enter a number: "))
if(day == 1):
    print("Monady")
elif(day == 2):
    print("Tuesday")
elif(day == 3):
    print("Wednesday")
elif(day == 4):
    print("Thurday")
elif(day == 5):
    print("Friday")
elif(day == 6):
    print("Saturday")
elif(day == 7):
    print("Sunday")
else:
    print("Invalid")