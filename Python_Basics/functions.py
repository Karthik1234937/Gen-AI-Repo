"""
    functions
    *********
        set of instructions called as functions
             (or)
        particular "business logic" also called as function
        
        functions are used to "reuse" business logic

        "def" is the keyword, used to declare the function

        "pass" is the keyword, used to create "empty functions"
"""
# no para - no return type
# def addition():
#         num1 = 200
#         num2 = 100
#         res = num1 + num2
#         print(res)                  #300

# addition()

# no para - with return type
# def subtraction():
#     num1 = 200
#     num2 = 100
#     res = num1 - num2
#     return res

# x = subtraction()
# print(x)

# with para - no return type
# def multiply(num1,num2):
#     res = num1 * num2
#     print(res)

# multiply(200,100)

# with para - with return type
# def division(num1,num2):
#     res = num1 / num2
#     return res

# x = division(200,0)
# print(x)

# with para - with return type
# def login(uname,pwd):
#     #res = "success" if uname=="admin" and pwd=="admin@123" else "fail"
#     res=""
#     if uname=="admin" and pwd=="admin@123":
#         res = "success"
#     else:
#         res = "fail" 
    
#     return res

# res = login("admin","admin@123")
# print(res)

# default parameters
# def test_func(param1="Hello"):
#     print(param1)

# test_func()
# test_func("Welcome")
# test_func(None)

# def test_func(num1,num2=10):
#     return num1 + num2

# print(test_func(5))
# print(test_func(10,20))

# default parameters order must be last in parameters list
# def test_func(param1="Hello",param2):
#     pass
    
# in case of list, modified list will be used in next iterations
# def test_func(x=[]):   
#     x.append(1)
#     return x

# print(test_func()) # [1]
# print(test_func()) # [1,1]
#                    # [1,1,1]


# def test_func(x=None):
#     if x is None:
#         x = []
#     x.append(1)
#     return x

# print(test_func())
# print(test_func())


# by default int is immutable
# for every call num1 will be "5"
# def test_func(num1=5):
#     num1 += 1
#     return num1
# print(test_func())
# print(test_func())

# default parameters are initilized while declaraing the functions
# num1 = 100
# def test_func(param1 = num1):
#     print(param1)

# num1 = 200
# test_func()

# def test_func(sub="Gen AI",version=2):
#     print(sub,version)

# test_func(version=3,sub="Agentic AI")


# variable length arguments
# def test_func(*param1):   
#     print(param1)
#     print(type(param1))

# test_func(10,20,30,40,50)

# param1 - non default
# param2 - variable length (tuple)
# param3 - default parameter

# def test_func(param1,*param2,param3="Hello"):
#     print(param1,param2,param3)

#test_func() #TypeError: test_func() missing 1 required positional argument: 'param1'
#test_func(10) #10 () Hello
#test_func(10,20,30,40,50) #10 (20, 30, 40, 50) Hello
#test_func(10,20,param3="Welcome") #10 (20,) Welcome
#test_func(100, 10, 20, 30, 40, 50, param3="Python")


# we are able to pass only one tuple per function
# def test_func(*param1,*param2):
#     pass


# def test_func(**param1):
#     print(param1) 
# test_func(name="John",age=30,city="New York")

#name - non default parameter
#course - default parameter
#skills - variable length (tuple)
#details - variable length (dict)
#def test_fact(name,
#             course="Python",
#            *skills,
#           **details):
#    print(name)
#   print(course)
#   print(skills)
#   print(details)

#test_fact("Karthik", "Gen AI", "ML", "DL", "NLP", city="Hydrabad")


#normal --> default --> variable length (tuple) --> variable length (dict)


# Lambda functions (or) Anonymous functions - functions without name
# "lambda" is the keyword used to declare the lambda functions


#def add(num1,num2):
#    return num1 + num2
#print(add(200,100))

#add = lambda num1,num2:num1+num2
#print(add(200,100))


#find the bigger number
#big = lambda num1,num2: num1 if num1>num2 else num2
#print(big(200,100))

#evwn or odd
#even_odd = lambda num1: "Even" if num1%2==0 else "Odd" 
#print(even_odd(10))


# str = "Hello" len(str) --> 5

#res = lambda str: len(str)
#print(res("Python"))

"""
            map() function
 [1,2,3,4,5] --> [10,20,30,40,50]
    map() - predefined function, used to manipulate "all list elements"
                            filter()
    [100,200,300,400,500] >300 --> 400,500
 """

#res=list(map(lambda num1:num1*10,[1,2,3,4,5]))
#print(res)

#print(list(filter(lambda param1:param1>300,[100,200,300,400,500])))

#[1,2,3,4,5] --> even elements
#print(list(filter(lambda num1:num1%2==0,[1,2,3,4,5])))

#sorted() - used to sort the list 
#names = ["Karthik","ravi","A","python"]
#print(sorted(names,key=lambda x:len(x))) #['A', 'ravi', 'python', 'Karthik']

#sort based on marks
#students = [
#    ("std1",85),
#    ("std2",90),
#    ("std3",80)
#]
#print(sorted(students,key=lambda std:std[1]))

#reduce() - used to perfom sum of elements
# [1,2,3,4,5] --> [15]
#from functools import reduce
#print(reduce(lambda num1,num2:num1+num2,[1,2,3,4,5]))


































