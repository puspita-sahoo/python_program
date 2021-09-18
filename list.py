# 1.
# Take 10 integer inputs from user and store them in a list and print them on screen.
# ==================================qstn end

# lt = input("enter 10 number: ").split(",")
# print(lt)

# RIGHT ANSWER==================================================

# ls = []
# i = 10
# while i > 0:
#     u = int(input("enter a number: "))
#     ls.append(u)
#     i -= 1
# print(ls)

# ========================================================================================================================
# 2.
# Take 10 integer inputs from user and store them in a list. 
# Again ask user to give a number. Now, tell user 
# whether that number is present in list or not.
# ( Iterate over list using while loop ).
# ==================================qstn end
# ls = []
# i = 10
# while i > 0:
#     u = int(input("enter a number: "))
#     ls.append(u)
#     i -= 1
# print(ls)

# u = int(input("enter a number: "))
# i = 0
# count = 0
# while i <= 9:
#     if ls[i] == u:
#         print("yes ",u) 
#         count += 1
#     i += 1

# if count == 0:
#     print("No", u)

# # if present == True:
# #     print("yes ",u) 
# # else:
# #     print("No ",u) 

# ========================================================================================================================
# 3.
# Take 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.
# ==================================qstn end
# lst = [1,2,3,4,5,6,7,8,9,19,10,18]
# lst = []
# i = 0
# while i <= 13:
#     a = int(input("enter a number: "))
#     lst.append(a)
#     pove = 0
#     if a == 0:
#         print(a, "is zero")
#         pove += 1
#     if a > 0:
#         print(a, " +ve")
#     if a < 0:
#         print(a, " -ve")
#     if a % 2 == 0:
#         print(a, "even")
#     if a % 2 != 0:
#         print(a, "odd")
#     i +=1
# print(lst)

# ========================================================================================================================
# 4.
# Take 10 integer inputs from user and store them in a list.
#  Now, copy all the elements in another list but in reverse order.

# ==================================qstn end
# lst = []
# i = 1
# while i <= 4:
#     a = int(input("enter a number: "))
#     lst.append(a)
#     i += 1

# new_c = lst.copy()
# print(new_c)
# new_c.reverse()
# print(new_c)

# ========================================================================================================================
# 5.
# Write a program to find the sum of all elements of a list.
# ==================================qstn end
# ls = [1,2,3]
# print(sum(ls))

# ========================================================================================================================
# 6.
# Write a program to find the product of all elements of a list.

# ====================================

# ls = [2,3,4,5]
# pd = 1
# i = 0
# while i < len(ls):
#     pd = pd * ls[i]
#     i += 1

# print(pd)
# ====================================

# ls = [2,2,4,5]
# pd = 1
# for i in ls:
#     pd = pd *i 

# print(pd)

# ========================================================================================================================
# 7.
# Initialize and print each element in new line of a list inside list.

# ====================================

# ls = [[2, 3, 'a'], ['z', 9, 'l']]
# i = 0
# while i < len(ls):
#     j = 0
#     while j < len(ls[i]):
#         print(ls[i][j])
#         j += 1
#     i += 1
# ====================================
# ls = [[2, 3, 'a'], ['z', 9, 'l']]
# for i in ls:
#     for j in i:
#         print(j)
# ========================================================================================================================
# 8.
# Find largest and smallest elements of a list.

# ====================================

# a = [2,3,4,11,5,10]
# lar = a[0]
# sma = a [0]
# i = 1
# while i < len(a):
#     if a[i] > lar:
#         lar = a[i] 
#     if a[i] < sma:
#         sma = a[i] 
#     i += 1
# print(lar)
# print(sma)

# ========================================================================================================================
# 9.
# Write a program to print sum, average of all numbers, smallest and largest element of a list.
# ====================================

# a = [2,3,6,0,1,1]
# lar = a[0]
# sma = a[0]
# sum = 0
# i = 1
# while i < len(a):
#     sum += a[i]
#     if a[i] > lar:
#         lar = a[i]
#     if a[i] < sma:
#         sma = a[i]
#     i += 1
# avg = sum/len(a)
# print(a)
# print('largest: ',lar)
# print('smallest: ',sma)
# print('summation: ',sum)
# print('average: ',avg)
# ========================================================================================================================
# 10.
# Write a program to check if elements of a list are same or not it read from front or back. E.g.-
# 2	3	15	15	3	2

# ====================================
# a = [2,3,12,12,3,2]
# sm = True
# i = 0
# j = -1
# while i < len(a):
#     if a[i] != a[j]:                            #pr(a[i]), pr(a[j])
#         sm = False
#     i += 1
#     j = j-1
# print(sm)

# ========================================================================================================================
# 11.
# Make a list by taking 10 input from user. Now delete all repeated elements of the list.
# E.g.-
# INPUT : [1,2,3,2,1,3,12,12,32]
# OUTPUT : [1,2,3,12,32]
# ====================================
# a = [1,2,3,2,1,3,12,12]
# i = 0
# while i < len(a):
#     j = i+1
#     while j < len(a):
#         if a[i] == a[j]:
#             del a[j]
#         j += 1
#     i += 1

# print(a)

# ====================================
# PYTHON WAY=====
# a = [1,2,3,2,1,3,12,12]
# a =  set(a)
# print(list(a))

# ========================================================================================================================
# 12.
# Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
# INITIAL list :
# 58	24	13	15	63	9	8	81	1	78

# After spliting :
# 58	24	13	15	63
# 9	8	81	1	78

# ====================================
# a =  [58, 24, 13, 15, 63, 9, 8, 81, 1, 78]
# i = len(a)/2
# print(a[:i])
# print(a[i:])


# a = [58,24,13,15,63,9,8,81,1,78]
# print (a[:len(a)/2])
# print (a[len(a)/2:])
# ========================================================================================================================
# 13.
# Ask user to give integer inputs to make a list. Store only even values given and print the list.
# ====================================
# a = input("enter numbers: ").split(',')
# i = 0
# while i < len(a):
#     if a[i] % 2 != 0:
#         del a[i]
#     i+=1
# print(a)

# ========================================================================================================================
# 1. Take a list of length n where all the numbers are non-negative and unique. 
# Find the element in the list possessing the highest value. 
# Split the element into two parts where first part contains the next highest value in the list and
# second part hold the required additive entity to get the highest value. 
# Print the list where the highest value get splitted into those two parts.

# Sample input: 4 8 6 3 2
# Sample output: 4 6 2 6 3 2

# RIGHT ANSWER===================================

# a = [4,8,6,3,2]
# lar = a[0]
# i = 0
# while i < len(a):
#     if a[i] > lar:
#         lar = a[i]
#         lar_index = i
#     i += 1

# sec_lar = a[0]
# i = 0
# while i < len(a):
#     if a[i] != lar and a[i] > sec_lar:
#         sec_lar = a[i]
#     i += 1

# diff = lar - sec_lar
# print(a[:lar_index] + [sec_lar , diff] + a[lar_index+1:])

# ====================================

# a = [4,8,6,3,2]
# i = 0
# largest = a[0]
# while i<len(a):
#   if largest < a[i]:
#     largest = a[i]
#     largest_index = i
#   i = i+1
# print (largest_index)


# sec_largest =  a[0]
# i = 0
# while i<len(a):
#   if largest != a[i] and sec_largest < a[i]:
#     sec_largest = a[i]
#   i = i+1
# diff = largest - sec_largest
# print (a[:largest_index]+[sec_largest,diff]+a[largest_index+1:])

# ========================================================================================================================
# 2.Write a program to shift every element of a list to circularly right. E.g.-
# INPUT : 1 2 3 4 5
# OUTPUT : 5 1 2 3 4

# ====================================
# a = [1,2,3,4,5]
# b = [a[len(a)-1]] + a[:len(a)-1]
# a = b
# print(a)

# ========================================================================================================================
# 3.Write a program to add and multiply two 3x3 matrices.
# ====================================

# a = [[1,2,3], [4,3,5], [2,1,2]]
# print(a)
# b = [[2,4,2], [3,2,4], [2,4,5]]

# i = 0
# while i <= 2:
#     j = 0 
#     while j <= 2:
#         k = 0
#         while k <= 2:
#             add = a[i:j:k] + b[i][j][k]
#             mul = a[i][j][k] * b[i][j][k]
#             k += 1
#         j += 1
#     i += 1
# print(add)
# print(mul)

