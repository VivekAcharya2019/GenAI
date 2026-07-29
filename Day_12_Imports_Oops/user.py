
user1 = 10
user2 = 10

# # import  full file 
# import calculator
# user1 = 45
# user2 = 56

# total = calculator.add(user1,user2)
# print(total)

# total = calculator.subtract(user1,user2)
# print(total)

# total = calculator.multiply(user1,user2)
# print(total)

# total = calculator.divide(user1,user2)
# print(total)


# ## import specific functions 
# from calculator import multiply, divide
# total = multiply(user1,user2)
# print(total)

# total = divide(user1,user2)
# print(total)


# ## use alias for imported function
# import calculator as cl
# from calculator import multiply as ml

# def multiply(a,b):
#     print("inside user file")
#     return a*b

# total = cl.add(user1,user2)
# print(total)

# total = ml(user1,user2)
# print(total)

# total = multiply(user1,user2)
# print(total)


## importing from folder
# # 1.  import whole file from folder  
# from utils import userutils
# name = "Micro Degree"
# userutils.show_name(name)


# # 1.  import whole file from folder  
# from utils.userutils import show_name
# name = "Micro Degree"
# show_name(name)


# # 1.  import whole file from folder  
# from utils.userutils import show_name as sn
# name = "Micro Degree"
# sn(name)




def multiply(a,b):
    print("inside user file")
    return a*b
from calculator import multiply 
print(multiply(12,12))
