from icecream import ic


# ========================================================================================================
# first,second=0,1
# n = int(input("give a number for fibonacci series : "))
# for i in range(0,n):
#     if i<=1:
#         result=i
#     else:
#       result = first + second
#       first = second
#       second = result
#     print(result, end=",")
# print()

# 0, 1, 1, 2, 3, 5, 8, 13
# ========================================================================================================


# first,second=0,1
# n = int(input("give a number for fibonacci series : "))
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
# for i in range(0,n):
#     print(fibonacci(i), end= ',')
# print()
# ========================================================================================================

# n = int(input("give a number : "))
# reverse = 0
# while n!=0:
#     reverse = reverse*10 + n%10       
#     n = (n//10)
# print("After reverse : ", reverse) 

# ========================================================================================================

# n = int(input())
# order = len(str(n))
# sum = 0
# copy_n = n
# while n > 0:
#     digit = n%10
#     sum += pow(digit, order)
#     n = n//10

# if sum == copy_n:
#     ic('arm')
# else:
#     ic("not")
# ========================================================================================================

# n = int(input("give a number : "))
# reverse,temp = 0,n
# while temp!=0:
#     reverse = reverse*10 + temp%10        
#     temp=temp//10
# if reverse==n:
#     print("palindrom")
# else:
#     print("not palindrom")
# ========================================================================================================


# n = int(input("give a number : "))
# def reverse(num):
#     if num<10:
#       return num 
#     else:
#       return int(str(num%10) + str(reverse(num//10)))

# # def isPalindrome(num):
#     if num == reverse(num):
#         return 1
#     return 0
# if isPalindrome(n) == 1:
#     print("palindrome")
# else:
#     print("not palindrome") 
# ========================================================================================================
# def pal(n, t):
#     if n == 0:
#         return t
#     t = (t*10) + (n%10)
#     return pal(int(n/10), t)
# num = int(input("number: "))
# temp = 0
# p = pal(num, temp)
# if num == p:
#     print("yes")
# else:
#     print("no")

# ========================================================================================================
# def pal(n, t):
#     if n == 0:
#         return t
#     t = (t*10) + (n%10)
#     return pal(n//10, t)
# num = int(input("number: "))
# temp = 0
# p = pal(num, temp)
# if num == p:
#     print("yes")
# else:
#     print("no")
# ========================================================================================================

# a = 2
# b = 5

# c=a
# a=b
# b=c

# ic(a)
# ic(b) 
# ========================================================================================================
a = 2
b = 5

a=a-b
b=a+b
a=b-a

ic(a)
ic(b)




