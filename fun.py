# 1.
# Write a function to calculate area and perimeter of a rectangle.
# ====================================

# def rectangle(l, b):
#     area = l * b
#     perimeter = 2*(l + b)
#     return area, perimeter

# a , b = rectangle(5, 3)
# print(a)
# print(b)

# ========================================================================================================================
# 2.
# Write a function to calculate area and circumference of a circle.
# ====================================

# def circle(r):
#     area = 3.141*(r**2)
#     circumference = 2*3.141*r
#     return area, circumference
# a, b = circle(4)
# print(a)
# print(b)

# ========================================================================================================================
# 3.
# Write a function to calculate power of a number raised to other. E.g.- ab
# ====================================
# def power(a, b):
#     return a ** b

# a = int(input("enter the base number: "))
# b = int(input("enter the exponent: "))    
# result = power(a, b)
# print(result)

# ========================================================================================================================
# 4.
# Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )
# ====================================

# def vote(age):
#     if age >= 18:
#         return "you can give vote"
#     else:
#         return "you are not allow to vote"
# a = int(input("enter your age: "))
# print(vote(a))

# ========================================================================================================================
# 5.
# Print multiplication table of 12 using recursion.
# RIGHT ANSWER===================================
# def table(num,multiple):
#     value = num*multiple
#     print(value)
#     multiple += 1
#     if multiple <= 10:
#         table(num,multiple)

# table(12, 1)

# ====================================
# def table(b):
#     a = 12
#     p = a*b
#     print(p, b)
#     b += 1
#     if b <= 10:
#         table(b)
# table(1)
# ========================================================================================================================
# 6.
# Write a function to calculate power of a number raised to other ( ab ) using recursion.
# ====================================doubttttttttttttttTTTTTTTTTTTTT

# def power(a, b):
#     p = a**b
#     print(p)

# a = int(input("enter 1: "))
# b = int(input("enter 2: "))
# power(a, b)
# ====================================
# def power(num, powe, prud, count):
#     prud *= num
#     count += 1
#     print(prud)
#     if count <= powe:
#         power(num, powe, prud, count)

# num = int(input("enter 1: "))
# powe = int(input("enter 2: "))
# power(num, powe, 1, 1)

# ========================================================================================================================
# 7.
# Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and
#  prints all the perfect numbers between 1 and 1000.
# [An integer number is said to be “perfect number” if its factors, 
# including 1(but not the number itself), sum to the number.
#  E.g., 6 is a perfect number because 6=1+2+3].

# ====================================
# i = 1
# while i <= 10000:
#     a = 1
#     sum = 0
#     while a < i:
#         if i % a == 0:
#             sum += a
#         a += 1
#     if sum == i:
#         print(i,'perfect')
#     # else:
#         # print('not perfect')
#     i += 1
# ========================================================================================================================
# 8.
# Write a function to check if a number is even or not.
# ====================================


# def check(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# a = int(input("enter :"))
# check(a)
# ========================================================================================================================
# 9.
# Write a function to check if a number is prime or not.
# ====================================  INCOMPLETE

# # prm = []
# def prime(a):
#     for i in range(2,a):
#         if a % i == 0:
#             break
#     else:
#         # prm.append(i)
#         print("prime")
#     # print(prm)
# a = int(input("enter :"))
# prime(a)
# ========================================================================================================================
# 10.
# Write a function to find factorial of a number but also store the factorials calculated in
# a dictionary as done in the Fibonacci series example.

























