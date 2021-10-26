# 2.
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


# pur_qty = int(input("Enter quantity:"))
# cost_pur_qty = pur_qty * 100
# total_cost = cost_pur_qty - (10/100 * cost_pur_qty)

# if cost_pur_qty > 1000:
#     print("Total cost is:", total_cost)
# else:
#     print("Total cost is:", cost_pur_qty)

# ========================================================================================================

# 4.
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

# yr_serv = int(input("Enter your year of service: "))
# salary = int(input("Enter your salary: "))
# net_bonus_amt = salary + (5/100 * salary)

# if yr_serv > 5:
#     print("Your net bonus salary is ", net_bonus_amt)
# else:
#     print("Your salary is ", salary)

# ========================================================================================================

# 5.
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


# m = int(input("Enter your mark: "))
# if m >= 80:
#     print("Your grade is: A",)
# elif m >= 60 and  m < 80:
#     print("Your grade is: B",)
# elif m >= 50 and m < 60:
#     print("Your grade is: C",)
# elif m >= 45 and m < 50:
#     print("Your grade is: D",)    
# elif m >= 25 and m < 45:
#     print("Your grade is: E",)
# else:
#     print("Sorry!!! You are fail!!")

# ========================================================================================================

# 6.
# Take input of age of 3 people by user and determine oldest and youngest among them.

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))

# if a >= b and a >= c:
#     if a > b and b > c:
#         print(a, "is greater")
#     elif a == b and b == c:
#         print(f"{a} and {b} and {c} are equal")
#     elif a > b and b == c:
#         print(a, "is greater")
#     elif a > b and a == c:
#         print(a, c, " greater")
#     elif a > c and a == b:
#         print(a,b ," greater")
    
# elif b >= a and b >= c:
#     if b > a and b > c:
#         print(b, "is greater")
#     elif b > a and b == c:
#         print(b,c, " greater")
#     elif b > c and b == a:
#         print(a,b, "is greater")
#     elif b > a and a == c:
#         print(b, "is greater")
    
# elif c >= a and c >= b:
#     if c > a and c > b:
#         print(c, "is greater")
#     elif c > a and c == b:
#         print(b,c ," greater")
#     elif c > b and c == a:
#         print(a,c ," greater")
#     elif c > a and a == b:
#         print(c ," greater")


# ========================================================================================================


# 7.
# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1


# a = int(input("Enter a number: "))

# if a < 0:
#     print(-a)
# else:
#     print(a)

# ========================================================================================================

#8. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# c_held = int(input("Enter the number of classes held: "))              # c_held = class_held 
# c_attend = int(input("Enter the number of classes attended: "))        
# p_c_attended = c_attend/c_held * 100                                   #percentage_clas_attended     

# if p_c_attended >= 75:
#     print(f"Congratulations!!! Your percentage of class attended is {p_c_attended}%")
# else:
#     print(f"Sorry!!! Your percentage of class attended is {p_c_attended}%")

# ========================================================================================================
#9. Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.


# c_held = int(input("Enter the number of classes held: "))              # c_held = class_held
 
# c_attend = int(input("Enter the number of classes attended: "))  
# m_cause = input("Enter Y or N if you have any medical cause or not: ")      
# p_c_attended = c_attend/c_held * 100                                   #percentage_clas_attended     

# if p_c_attended >= 75:
#     print(f"Congratulations!!! Your percentage of class attended is {p_c_attended}%")
# else:
#     if m_cause == "Y":
#         print(f"Due to medical cause, you can sit in exam!!! Your percentage of class attended is {p_c_attended}%")
#     else:
#         print(f"Sorry!!! Your percentage of class

# ===============================================================================================================

# 10.Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but
#  if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

#===================================
# yr = int(input("Enter a year: "))
# if yr % 100 == 0:
#     if yr % 400 == 0:
#         print(f"{yr} it is a leap year")
#     else:
#         print(f"{yr} NOTleap")
# elif yr % 4 == 0 :
#     print(f"{yr} LEAP")
# else:
#     print(f"{yr} not leap")


# =======================================================================================================
# 12.
# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and
#  then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

# ===================================
# age = int(input("Enter your age: "))
# sex = input("Enter gender 'M' or 'F': ")
# m_status = input("enter 'Y' or 'No' for maeitial status: ")

# if sex == "F":
#     print("Your place of service is urban areas")
# elif sex == "M": 
#     if age > 20 and age <= 40:
#         print("Your place of service may be anywhere")
#     elif age > 40 and age <= 60:
#         print("Your place of service is urban areas")
# else:
#     Print("Error!!! Your age is not appropriate for this work")


# ========================================================================================================================
# 3.
# A 4 digit number is entered through keyboard. 
# Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895

# ==================================================

num = int(input("enter the number: "))
temp = num

first_no = temp//1000
temp = temp%1000

sec_no = temp//100
temp = temp%100

thrd_no = temp//10
temp = temp%10

fourth_no = temp

rev_no = fourth_no*1000 + thrd_no*100 + sec_no*10 + first_no
print(rev_no)

