#######     String slicing      ##########

name = "krishna gupta"
print(name[0:7])  # Output: krishna
#            ^ = n-1 
print(name[8:])   # Output: gupta
#           ^ = len(name) - 1

fruit =  "Mango"

print(fruit[0:5])  # Output: Man
print(fruit[:5])  
print(fruit[1:4])  
print(fruit[0:])
#             ^ len(fruit) - 1
print(fruit[0:-2])  
#              ^ len(fruit) -2-1
print(fruit[-1:-2])  

