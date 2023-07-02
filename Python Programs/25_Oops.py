# Object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
# It aims to implement real-world entities like inheritance,polymorphisms,encapsulation, etc. in the programming.
# The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

#--------------------------------------------------------------------------
# Class
# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
# It is a logical entity that contains some attributes and methods. 

# class ClassName:
   # Statement-1
   # .
   # .
   # .
   # Statement-N

# self :
#    --> Class methods must have an extra first parameter in the method definition.
#    --> We do not give a value for this parameter when we call the method.
#    --> It holds current object address.

#--------------------------------------------------------------------------
# Constructor :
#       --> It is a special method of a class it executes automatically whenever object is created.
#       --> It allocates the memory for given object. 
#       --> def __init__(self,<arg1>,<arg2>,....):

#--------------------------------------------------------------------------
# Destructor :
#       --> It is a special method of a class it executes automatically whenever control is outside of the object.
#       --> It deallocates memory for object.
#       --> It is called after the program ended
#       --> def __del__(self,<arg1>,<arg2>,.....):

#---------------------------------------------------------------------------
# Object
# If the variable is decleared in class as static then it is called as static variable and method we use (@staticmethod).
# If the variable is decleared in class is called class variable (cls) and method we use (@classmethod).
# It the variable is decleared in constructor of class is called instance (self).
# The object is an entity that has a state and behavior associated with it.
# Object consists :
#       --> state    : Represents the attributs of the Object.
#       --> Behavior : Represents the methods of the Object.
#       --> Identity : Gives unique name to an Object.

#---------------------------------------------------------------------------
# Inheritance :
#     --> Inheritance allows us to define a class that inherits all the methods and properties from other class.
#     --> Parent class is known as base class and it can be inherited. 
#     --> child class is known as derived class and it can inherit from other classes or parent class.
#     --> Types of Inheritance:
#           --> Single Inheritance:
#               -->Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
#           --> Multilevel Inheritance:
#               -->Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.
#           --> Hierarchical Inheritance:
#               -->Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.
#           --> Multiple Inheritance:
#               -->Multiple level inheritance enables one derived class to inherit properties from more than one base class.

#-------------------------------------------------------------------------------
# Polymorphism :
#    --> It means the same function/method name being used for diferent types.
#    --> The key difference is that data types and number of arguments are  used in this function will be vary.
# We have 4 ways to impliment polymorphism :
#                       --> Duck typing
#                       --> Operator overloading
#                       --> Method overloading
#                       --> Method overriding

#------------------------------------------------------------------------------------------
# Encapsulation :
#     --> Wrapping up of both properties and methods into a single logical unit known as encapsulation.
#     --> This can prevent the accidental modification of data. To prevent accidental change.

#-----------------------------------------------------------------------------
# Data Abstraction : 
#     --> It hides the unnecessary code details from the user.
#     --> We do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
#     --> Data Abstraction in Python can be achieved through creating abstract classes.