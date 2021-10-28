# 1.
# Take 10 integers from keyboard using loop and print their average value on the screen.
# ===========================================qstn end
# ls = []
# i = 1
# while i <= 10:
#     a = int(input("Enter the number:"))
#     i += 1
#     ls.append(a)

# avg = sum(ls)/10
# print(avg)
# print(ls)

# RIGHT ANSWER============================================

# sum = 0
# i = 1
# while i <= 10:
#     a = int(input("Enter the number:"))
#     sum += a
#     i += 1
# print(sum/10)
# ==================================================================================================================
# 2.
# Print the following patterns using loop :
# a.
# *
# **
# ***
# ****
# b.
#   *
#  ***
# *****
#  ***
#   *
# c.
# 1010101
#  10101
#   101
#    1

# ===========================================qstn end

# ANSWERRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# # A:-=====================
# i = 1
# while i <= 4:
#     a = ("*" * i)
#     print(a)
#     i += 1

# B:-=========================================
# s = 2                           # s = space
# r = 1                           # r = star
# i = 1
# while i <= 3:
#     print(' '*s+ "*"*r+ ' '*s)
#     s -= 1
#     r += 2
#     i+=1
# ============
# s = 1                           # s = space
# r = 3                           # r = star
# i = 4
# while i <= 5:
#     print(' '*s+ "*"*r+ ' '*s)
#     s +=1
#     r -=2
#     i += 1
# ==================RIGHT ANSWER================

# i = 1
# j = 2
# while i >= 1:
#     print(" "*j+"*"*i+" "*j)
#     i = i+2
#     j = j-1
#     if i > 5:
#         break
# i = 3
# j = 1
# while i >= 1:
#     print(" "*j+"*"*i+" "*j)
#     i = i-2
#     j = j+1
# ===========================================================================================
# C:-=====================

# i = 7
# s = 0
# k=3
# while (i>=0 and k>=0):
#         a=(" "*s+"10"*k+"1"+" "*s)
#         print(a)
#         k=k-1
#         i=i-2
#         s=s+1


# ==================RIGHT ANSWER================


# j = 3                             #j = for '10'          
# i = 1                             #i = how many line to print          
# s = 0                             #s = for space 
# while i <= 4:
#     print(' '*s + '10'*j + '1'+ ' '*s)
#     j-=1
#     i +=1
#     s+=1


# ==================================================================================================================
# 3.
# Print multiplication table of 24, 50 and 29 using loop.


# a = 24=====================
# i =1
# while i <=10:
#     j = a*i
#     print(a,"x",i,'=',j)
#     i +=1


# 29 tavle=====================

# a = 29
# i =1
# while i<=10:
#     j = a*i
#     print(a,'X',i,'=',j)
#     i+=1

# 50 tavle=====================

# s = 50
# t = 1
# while t<=10:
#     m = s*t
#     print(s,'X',t,'=',m)
#     t+=1

# ==================================================================================================================

# 5.
# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1
# Write a program to calculate factorial of a number.

# ==========================================
# n = int(input("enter a number: "))
# i = 1
# j = 1
# if n == 0:
#     print("1")

# else:
#     while i <= n:
#         j = j*i
#         i+=1
#     print(j)

# ==================================================================================================================
# 6.
# Write a program to find greatest common divisor (GCD) or
#  highest common factor (HCF) of given two numbers.

# ==========================================
# num=int(input("enter: "))
# num_2=int(input("enter: "))
# ls=[]
# ts=[]
# i=1
# while i <= num:
#     if num%i == 0:
#         ls.append(i)


# i =1
# while i <= num_2:
#     if num_2% i== 0:
#         ts.append(i)

# j=0
# k=0
# while j <= len(ls):
#     if ls[j] == ts[k]:
#         print(ls[j],ls[k])
#         j+=1
#         k+=1


# a =90
# b = 18
# if a < b:
#     smaller = a
# elif b<a:
#     smaller = b

# ls=[]
# i = 1
# while i <= smaller:
#     if a%i == 0 and b%i==0:
#         ls.append(i)
#     i+=1
# print(ls)
# print(max(ls))


# ==================================================================================================================
# 7.
# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.


# p=1
# num = input("e:")
# ls = []
# press = input("q:")
# while True:

#     if press != 'q':
#         num = int(input("e:"))
#         press = input("Q:")
#         ls.append(num)
#         p*=num
#     elif press=='q':
#         break

# j = sum(ls)
# avg = j//(len(ls))
# print(avg)
# print(p)

# ==================================================================================================================
# 1.
# Calculate the sum of digits of a number given by user. E.g.-
# INUPT : 123        OUPUT : 6
# INUPT : 12345        OUPUT : 15


# # num = int(input("enter a number: "))
# num = int(input("enter a number: "))
# print(num)
# sum = 0
# i =1
# while i <= len(num):
#     for j in num:
#         sum+=j
#         i+=1
# print(sum)



# RIGHT ANSWER============================================

# num = int(input("enter the number: "))
# sum = 0
# while True:
#     r = num % 10
#     num = num//10
#     sum += r
#     if num < 10:
#         sum+=num
#         break

# print(sum)


# ==================================================================================================================
# 2.
# A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
# E.g.- 153 is an Armstrong number because (1**3)+(5**3)+(3**3) = 153.
# Write all Armstrong numbers between 100 to 500.


# n= int(input("Enter a number: "))
# # r = 1
# sum = 0
# while True:
#     r = n % 10
#     remain = n //10
#     cube = r**3
#     print(cube)
#     sum +=cube
#     if remain < 10:
#         cube = remain**3
#         sum +=cube
#         break
# print(sum)

# if sum == n:
#     print(sum)
#     print(n)
#     print("amstrong")
# else:
#     print(sum)
#     print("not amstrong")
#     print(n)




# num = int(input("Enter: "))
# temp = num
# sum = 0
# while temp>0:
#     r = temp% 10
#     sum += r**3
#     temp //=10

# if sum == num:
#     print("amstrong")
# else:
#     print("not amstrong")


# ==================================================================================================================

# 3.
# Write a program to print a number given by user but digits reversed. E.g.-
# INPUT : 123        OUTPUT : 321
# INPUT : 12345        OUTPUT : 54321


# num = int(input("enter a number: "))
# p = int(input("enter how many digit your number contains: "))
# temp = num
# while temp > 0:
#     digit = temp%10
#     temp = temp//10
#     new = (10*p)+digit + (10*p)+digit + (10*p)+digit +digit
# print(new)





# RIGHT ANSWER============================================

# num = int(input("enter a number: "))
# temp = num
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     temp = temp // 10
#     rev = rev*10 + digit

# print(rev)

# ==================================================================================================================

# 4.
# Write a program to find prime factor of a number.
# If a factor of a number is prime number then it is its prime factor.


# num = int(input("enter a number: "))
# i = 1
# while i <= num:
#     if num % i == 0:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i, "is prime factor of", num)
#     i+=1





# prime=[]
# num = int(input("enter a number: "))
# i = 1
# while i <= num:
#     if num % i == 0:
#         j = 2
#         while j < i:
#             if i%j != 0:
#                 prime.append(i)
#             j += 1    
#     i+=1

# print(prime, "is prime factor of", num)

# ==================================================================================================================

# num = int(input("enter a number: "))
# i = 2
# p = []
# while i <= num:
#     j = 2
#     while j < i:
#         if i%j != 0:
#             p.append(i)
#         j += 1
#     i += 1


# print(p)


# 


Number = 1

while(Number <= 100):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = ',')
    Number = Number  + 1





