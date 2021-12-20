#Discussion Forum

#Create your own Python code examples that demonstrate each of the following. Do not copy examples from the book or any other source. Try to be creative with your examples to demonstrate that you invented them yourself.


#Example 1: Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.

#Example 2: Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 

#Example 3: Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.

#Example 4: Create a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.

#Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.


#Answers

#Hello Everyone ! This is my Python Code Examples for this discussion forum.

#Example 1:

def say_hello(greeting) :
    print("Have a good " + greeting)
    say_hello("morning")

#greeting which is inside the () of the say_hello function is parameter, and "morning" string data value inside the function name is argument.

#Example 2:

#This is a value argument.
say_hello("night")
#Have a good night

#This is a variable argument.
say_hello(greeting = "afternoon")
#Have a good afternoon

#This is an expression argument.
say_hello(str(24 - 13) + " pm")
#Have a good 11 pm

#Example 3 :

#his is a local variable
def say_meow() :
     message = "Meow !!"
     return message

say_meow()
#Meow !!

#Here, when the function is being called, it started to find the variable related to it, and when it found out,
#it print out its output. That variable is called global variable, which can be used from anywhere inside the code.

def say_meow() :
    return message
    message = "Meow !!"

say_meow()
Meow !!

#Example 4:

def show_customer(username) :
    customer = "Customer Name: " + username
    return customer

show_customer("Min Khant")
#'Customer Name: Min Khant'

#When I try to use that parameter name outside the function it show NameError and that is not defined as parameter name can only be used with respective functions.

print("Hello Customer: " + username)

#Traceback (most recent call last):
#File "", line 1, in NameError: name 'username' is not defined

#Example 5 :

name = "Thanlyin Technological University"
def my_university() :
    name = "University of the People"
    return name

 my_university()
'University of the People'

#Although the variable names are the same, it prioritize the variable inside the function. So, when I call its function name, the variable value inside the function
#appears. The variable outside the function only works when we don't declare a variable inside the function.