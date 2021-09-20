# 1.
# Write a program to print every character of a string entered by user in a new line using loop.

# string = input("enter a  word: ")
# for i in string:
#     print(i)


# ========================================================================================================================


# 2.
# Write a program to find the length of the string "refrigerator" without using len function.

# a = 'ref'
# c = 0
# for i in a:
#     c+=1
# print(c)


# ========================================================================================================================


# 3.
# Write a program to check if the letter 'e' is present in the word 'Umbrella'.

# w = "Umbrella"
# if 'e' in "Umbralla":
#     print(True)
# else:
#     print(False)    



# ========================================================================================================================
# 4.
# Write a program to check if the word 'orange' is present in the "This is orange juice".

# ==============================

# w = "This is orange juice"
# if 'orange' in w.split():
#     print(True)
# else:
#     print(False)
# ==============================
# # for i in w.split():
# #     print(i)


# ========================================================================================================================
# 5.
# Write a program to find the 
# first and the last occurence of the letter 'o' and character ',' in "Hel,lo, World".

# RIGHT ANSWER==================================================

# txt = "Hel,lo, World"
# t = txt.find("o")
# print(t)
# t = txt.rfind("o")
# print(t)

# p = txt.find(",")
# print(p)
# p = txt.rfind(",")
# print(p)
# ====================================================

# txt = "Hel,lo, World"
# for i in txt:
#     print(i)

#     if i == "o":
#         print(txt.index(i))

# ========================================================================================================================

# 6.
# Write the string after the first occurrence of ',' and 
# the string after the last occurrence of ',' in the string "Hello, Good, Morning, World".

# RIGHT ANSWER==================================================

# txt = "Hello, Good, Morning, World"
# q = txt.find(',')
# # print(q)
# print(txt[q+1: ])

# q = txt.rfind(',')
# print(txt[q+1:])


# ========================================================================================================================

# 7.
# Write a program that takes your full name as input and 
# displays the abbreviations of the first and 
# middle names except the last name which is displayed as it is. 
# For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
# ==================================qstn end

# RIGHT ANSWER==================================================

# a = "Robert Brett Roser"
# b= a.split()
# print(b)
# c = b[0][0] + '.' + b[1][0] + '.' + b[2]

# print(c)

# ==========================================

# a = input("enter your name: ")
# b = a.split()
# print(b)
# c= len(b)
# print(c)
# d = 0
# for i in range(0, c-1):
#     d += b[i][0] + '.'


# #  + b[c-1]
# print(d)

# =========================================== 

# def abbrevate_name(name):

#    x=name.split()

#    return (x[0][0:1]+'.'+x[1][0:1]+'.'+x[2])

# fname=input("Enter Fullname: ")

# fname=abbrevate_name(fname)

# print(fname)

# ========================================================================================================================
# 8.
# Check the occurrence of the letter 'e' and the word 'is' in the sentence "This is umbrella".

# ==================================qstn end

# txt = "This is umbrella"
# a = txt.find('e')
# print(a)

# b = txt.find('is')
# print(b)

# ========================================================================================================================
# 9.
# Write a program to find the number of vowels, consonents, digits and white space characters in a string.
# ==================================qstn end


# st = input("enter a string: ")
# stl = st.lower()
# print(stl)
# vowels = "aeiou"
# digits = "123456789"
# v = 0
# d = 0
# s = 0
# for i in range(0, len(stl)):
#     if stl[i] in vowels:
#         v+=1
#     elif stl[i] in digits:
#         d+=1    
#     elif stl[i] == ' ':
#         s+=1

# print("vowel: ", v)
# print("digit: ", d)
# print("space: ", s)

# ========================================================================================================================
# 10.
# Write a program to make a new string with 
# all the consonents deleted from the string "Hello, have a good day".

# RIGHT ANSWER==================================================

# a = ['a','e','i','o','u','A','E','I','O','U',' ',',']
# b = "Hello, have a good day"
# for i in b:
#   if i not in a:
#     b = b[:b.index(i)] + b[b.index(i)+1:]
# print(b)

# ====================================

# st = "Hello, have a good day"
# new_st = ''
# constn = 'bcdfghjklmnpqrstvwxyz'

# for i in range(0, len(st)):
#     if st[i] in constn:
#         new_st += st[i]

# print(new_st)

# ====================================




# st = "jello, have a good dko"
# new = ''
# constn = 'bcdfghjklmnpqrstvwxyz'

# for i in st:
#     if i in constn:
#        new += st.replace(i, '')

# print(st)
# print(new)

# ====================================



# def removeCons(s):
#     lis=[]
#     for x in s:
#         if i in vowel:
#             lis.append(i)
#     s="".join(i for i in lis)
#     return s



# ========================================================================================================================
# 1.Write a program to find out the largest and smallest word in the string "This is an umbrella".

# RIGHT ANSWER==================================================

# st = "is This an umbrella"
# new = st.split()
# print(new)
# big_wd = new[0]
# max_len = len(new[0])

# for i in new:
#     if len(i) > max_len:
#         max_len = len(i)
#         big_wd = i
# print(big_wd)





# ====================================

# st = "This is an umbrella"
# new = st.split()
# print(new)
# for word in new:
#     print(word)

# ====================================

# ========================================================================================================================

# 2.Write a program to check if a given string is a Palindrome.
# A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

# RIGHT ANSWER==================================================

# a = input("enter a word: ")
# if a == a[::-1]:
#     print(a, 'is palindrome')
# else:
#     print(a, 'is not palindrome')


# ========================================================================================================================
# 3.Write down the names of 10 of your friends in a list and
#  then sort those in alphabetically ascending order.

# RIGHT ANSWER==================================================


# ls = input("enter 10 names: ").split()
# # ls = input("enter 10 names: ")
# ls.sort()
# print(ls)

# ========================================================================================================================
# 4.Write a program to make a new string 
# with the word "the" deleted in the sentence "This is the lion in the cage".
# ==================================qstn end

# RIGHT ANSWER==================================================

# a = "This is the lion in the cage"
# a = a.split()
# for i in a:
#   if i == "the":
#     del(a[a.index(i)])
# print (a)
# print (" ".join(a))

# ====================================

# ls = "This is the lion in the cage"
# n = ls.replace('the', "")
# print(n)

# ====================================

# ls = "This is the lion in the cage"
# ls = ls.split()
# for i in ls:
#     if i == 'the':
#         del ls[ls.index(i)]
# print(''.join(ls))
# print(ls)


# ========================================================================================================================

# 5.Write a program to check if the two strings entered by user are anagrams or not. 
# Two words are said to be anagrams if the letters of one word can be rearranged to form the other word. 
# For example, jaxa and ajax are anagrams of each other.

# ==================================qstn end


# st1 = input("enter a word: ")
# st2 = input("enter a word: ")

# if sorted(st1) == sorted(st2):
#     print("they are anagrams")
# else:
#     print("they are not anagrams")


# ========================================================================================================================































































