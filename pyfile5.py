#  Typecasting in Python 


a = "1"

b = "3"

print("Addition of a and b is: ", a + b) 
# this will concatenate the strings and print "13"


print("Addition of a and b is:  " , int(a) + int(b) ) 
#this will convert the strings to integers and print 4




string = "123"
number = 456

str_num = int(string) 
num_str = str(number) 

sum1 = str_num + number
sum2 = string + num_str

print("The sum of string and number is: ", sum1)
print("The sum of string and number is: ", sum2)