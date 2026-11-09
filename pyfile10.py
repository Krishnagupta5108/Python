#  If Else in python 

# a = int(input("Enter a number: "))
# print("You age is :", a)

# if (a >= 18):
#     print("You are eligible to vote")   
    
    
   

# else:
#     print("You are not eligible to vote")
#     print("hello")

# budget = 100 
# apple_price = int(input("Enter the price of apple: "))

# if (apple_price <= budget): 
#     print("You can buy the apple")
    
#     print("hii")    

# else:

#     print("You cannot buy the apple")

# print("hello")


#  elif in python

num = int (input("Enter a number: "))
if (num > 0):
    print("The number is positive")
elif (num < 0):
    print("The number is negative")
elif (num == 99):
    print("The number is 99")
else:
    print("The number is zero")    



#  Nested if else 

num = int (input("Enter a number: "))
if (num < 0):
    print("The number is negative")

elif (num>0):
    if (num<10):
        print("Number is between 1 to 10")
    elif (num<20):
        print("Number is between 11 to 20")
    else:
        print("Number is greater than 20")
else:
    print("The number is zero")        


