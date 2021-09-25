# 1.
# Print all elements of a list using for loop.
# ====================================

# l = list(map(int, input("Enter a list: ").split(",")))
# print(l)
# for i in l:
#     print(i)

# ==================================================================================================================



# 2.
# Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element, if found.
# Iterate over list using for loop.
# ====================================


# data = input("Enter a list: ").split(",")
# item = input("Enter a item that you want to delete: ")

# for i in data:
#     if i == item:
#         data.remove(i)
# print(data)

# ==================================================================================================================


# 3.
# Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
# ====================================

# ls = [12, 24, 36, 48, 60, 72, 84, 96,108, 120]
# new_ls = []
# j = 1
# for i in ls:
#     k = 2*j
#     i += k
#     new_ls.append(i)
#     j += 1
# print(new_ls)

# ==================================================================================================================


# 4.
# You are given with a list of integer elements.
# Make a new list which will store square of elements of previous list.
# ====================================


# ls = [2, 3, 9, 7, 5]
# new_ls = []
# for i in ls:
#     j = i ** 2
#     new_ls.append(j)
#     # print(new_ls)
# print(new_ls)

# ==================================================================================================================


# 5.
# Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
# ====================================


# even = []
# odd = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print()
# print(odd)

# ==================================================================================================================


# 6.
# From the two list obtained in previous question, make new lists,
# containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
# # ====================================

# four = []
# six = []
# eight = []
# ten = []
# three = []
# five = []
# seven = []
# nine = []

# for i in even:
#     if i % 4 == 0:
#         four.append(i)
#     if i % 8 == 0:
#         eight.append(i)
#     if i % 6 == 0:
#         six.append(i)
#     if i % 10 == 0:
#         ten.append(i)

# for i in odd:
#     if i % 3 == 0:
#         three.append(i)
#     if i % 5 == 0:
#         five.append(i)
#     if i % 7 == 0:
#         seven.append(i)
#     if i % 9 == 0:
#         nine.append(i)

# print()
# print("four", four)
# print()

# print("six", six)
# print()

# print("eight", eight)
# print()

# print("ten", ten)
# print()

# print("three", three)
# print()

# print("five", five)
# print()

# print("seven", seven)
# print()

# print("nine", nine)

# ==================================================================================================================
# 7.
# From a list containing ints, strings and floats, make three lists to store them separately.
# ====================================
# RIGHT ANSWER==================================================
# mix = [10, 22, 34, "raj", 'puja', 12.999, 99.02]
# l_int = []
# l_str = []
# l_float = []

# for i in mix:
#     if type(i) == float:
#         l_float.append(i)
#     elif type(i) == str:
#         l_str.append(i)
#     else:
#         l_int.append(i)

# print(l_int)
# print(l_str)
# print(l_float)

# ====================================

# mix = [10, 22, 34, "raj", 'puja', 12.999, 99.02]
# l_int = []
# l_str = []
# l_float = []

# for i in mix:
#     print(l_int)


#     if i == float(i):
#         l_float.append(i)
#     elif i == str(i):
#         l_str.append(i)
#     else:
#         l_int.append(i)

# ==================================================================================================================
# 1.Using range(1,101), make a list containing only prime numbers.

# ===========================================questn finish

# RIGHT ANSWER==================================================
# prime = []
# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)

# print(prime)

# ===================

# prime = []
# composite = []

# for i in range(1, 101):
#     if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
#         prime.append(i)
#     elif i == 2 or i == 3:
#         prime.append(i)
#     else:
#         composite.append(i)
# print("Prime: ", len(prime))
# print()
# h = len(composite)
# print("Composite:", composite)
# print("Composite:",h)

# ==================================================================================================================
# 2.
# Initialize a 2D list of 3*3 matrix. E.g.-
# 1  2	3
# 4  5	6
# 7	 8	9
# Check if the matrix is symmetric or not.
# ===========================================questn finish

# RIGHT ANSWER==================================================

# ls = [[1,1,6], [2,8,4],[6,4,5]]
# sym = True
# for i in range(0, 3):
#     for j in range(0, 3):
#         if ls[i][j] != ls[j][i]:          # i,j=row,col and j,i=row,col
#             sym = False
#             print(sym)

# print(sym)
# ====================================

# ls = [[1, 2 ,3], [4 ,5, 6], [7,8,9]]
# print(ls)
# x = 2
# y = 3
# a_2d_list = [[99 for j in range(4)] for i in range(6)]
# print(a_2d_list)
# ===================

# ls = [[1,2,0], [2,8,4],[6,4,5]]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if ls[i][j] == ls[j][i]:
#             if i == 2 and j == 2:
#                 print("symetric")
#                 break
#         else:
#             print("non ")

#             break
#     else:
#         print("non symetric")




# ==================================================================================================================
# 3.
# Sorting refers to arranging data in a particular format.
# Sort a list of integers in ascending order(without using built-in sorted function).
# One of the algorithm is selection sort. Use below explanation of selection sort to do this.
# INITIAL LIST:
# 2	 3	1  45	15
# ===========================================qstn end

# RIGHT ANSWER==================================================

# ls = [2, 3, 1, 45, 15, 16]
# for i in range(0, len(ls)):
#     for j in range(i+1, len(ls)):
#         print(j)
#         if ls[i] > ls[j]:
#             ls[i], ls[j] = ls[j], ls[i]
# print(ls)
# ====================================

# ls = [2, 3, 1, 45, 15]
# for i in range(4):
#     if ls[i] > ls[i+1]:
#         ls[i], ls[i+1] = ls[i+1], ls[i]

# print(ls)
# print()

# =======================WRONG
# ls = [2, 3, 1, 45, 15]

# for i in range(0, 5):
#     for j in range(1, 5):
#         if ls[i] > ls[j]:
#             ls[i], ls[j] = ls[j], ls[i]
#             print(ls)

# print(ls)
# print()




















































































































