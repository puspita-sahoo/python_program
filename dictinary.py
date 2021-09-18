# 1.
# Ask user to give name and marks of 10 different students. Store them in dictionary.
# ==================================qstn end

# RIGHT ANSWER==================================================

# d = {}
# i = 4
# while i > 0:
#     nm = input("enter your name: ")
#     mrk = int(input("enter your mark: "))
#     d[nm] = mrk
#     i -= 1
# print(d)

# ====================================

# d = {}
# i = 10
# while i > 0:
#     nm = input("enter your name: ")
#     mrk = input("enter your mark: ")
#     d["nm"] = "mrk"
#     i -= 1
# print(d)

# ====================================
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# a 
# thisdict["color"] = "red"
# print(thisdict)
# ====================================


# d = {}
# i = 2
# while i > 0:
#     nm = input("enter your name: ")
#     mrk = int(input("enter your mark: "))
#     d[int(input("enter your mark: "))] = input("enter your name: ")
#     i -= 1
# print(d)


# ========================================================================================================================

# 2.
# Sort the dictionary created in previous example according to marks.

# ===================================

# markdict = {"Tom":67, "Zina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist = sorted(markdict.values())
# # sortdict = dict(marklist)
# print(marklist)

# ===================================

# markdict = {"Tom":67, "Zina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist = sorted(markdict.items(), key=lambda x:x[1])
# sortdict = dict(marklist)
# print(sortdict)

# ===================================
# d.sort(marks)


# asc = sorted(d, reverse=True)
# print(asc)



# sorted(d.items(),


# ===================================

# marklist={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# l=len(marklist)
# for i in range(l-1):
#     for j in range(i+1,l):
#         if marklist[i][1]>marklist[j][1]:
#             t=marklist[i]
#             marklist[i]=marklist[j]
#             marklist[j]=t
#     sortdict=dict(marklist)
#     print(sortdict)

# ===================================


# ========================================================================================================================

# 3.
# Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc.
# Display all words and then ask user to enter a word and display antonym of it.

# ===================================

# d = {"up":"down", "right":"left", "in":'out', "anger":'calm'}
# print(d)
# word = input("enter a word: ")
# meaning = d[word]
# print("antonym is: ", meaning)


# ========================================================================================================================

# 4.
# Count the number of occurrence of each letter in word "MISSISSIPPI". 
# Store count of every letter with the letter in a dictionary.

# ===================================
# word = "MISSISSSIPMMPI"
# d = dict()
# M = 0
# I = 0
# S = 0
# P = 0
# for i in word:
#     if i == "M":
#         M+=1
#     if i == "I":
#         I+=1
#     if i == "S":
#         S+=1
#     if i == "P":
#         P+=1

# d['M'] = M
# d['I'] = I
# d['S'] = S
# d['P'] = P
# print(d)

# ========================================================================================================================
# 5.
# From the previous question, sort according to the number of letters.

# ===================================
# s = sorted(d.values())
# print(s)

# ========================================================================================================================
# 6.
# Take a list containg only strings. 
# Now, take a string input from user and rearrange the elements of the list 
# according to the number of occurence of the string taken from user in the elements of the list.

# E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]

# STRING TAKEN : "bug"

# OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy","bunny bug","no bun"]

# ==================================qstn end


# lst = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# u = input("enter a word: ")
# d = {}
# for i in lst:
#     count = 0
#     for j in i.split():
#         if j == u:
#             count += 1
#     d[count] = i
    
# print(d)
# s_lt = []
# for s in sorted(d):
#     s_lt.append(s)
# s_lt.reverse()
# print(s_lt)

# ========================================================================================================================
# 1.
# Take 10 integer inputs from user and store them in a list and print them on screen.
# ==================================qstn end

# ls = []
# i = 10
# while i > 0:
#     u = int(input("enter a number: "))
#     ls.append(u)
#     i -= 1
# print(ls)

# ========================================================================================================================


















































































































