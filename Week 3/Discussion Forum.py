#Discussion Forum

#We will discuss this week the following given scenarios.

#Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.


#Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional. Do not copy the example from the textbook.



#Answer
#Hello Everyone ! This is my discussion post for this week.
#1.
#Chained Conditional
#Conditional in chained work step by step and more detailed and systematic step-by-step flows using if, elif, and else statements. It is mostly use when you have mutiple values to be checked by the Python.

username = input("Enter your username")
password = input("Enter your password")

if username== "Min@Kyaw" and password == "min#276" :
    print("You are authenticated as " + username )
elif username== "Min@Kyaw" or password == "min#276" :
    print("Username or Password incorrect")
else :
    print("Login failed, try again")

#Nested Conditional
#Conditions in nested do not include elif statement. But, it will work step-by-step inside the if and else statements nested condiitionals.

food_order = int(input("How many pizza do you want to order ? "))
check = "Are you sure you want to order " + food_order + " pizzas ?"
confirm = input(check)

if food_order >= 1 :
      if confirm == "Yes" or confirm == "yes" :
           success = "We will deliver " + food_order + " pizzas for you.  Thank  you for your order."
          print("Order Confirmed : " + success)
     else :
         print("We hope you would purchase pizza next time.")
else :
   print("We hope you would purchase pizza next time.")
    

#Both are decision makers that decide the code flow and its outputs based on what user's data might be or the values typed in.


#2. We can avoid using nested conditonals by using logical operators also boolean expressions (and, or, not) . using those can reduce lines of code for the steps we need to check in a program.

3#. We can modify the nested conditional I mentioned under Nested Conditional section in the follwing way.

if food_order >= 1 and confirm == "Yes" or confim == "yes" :
      success = "We will deliver " + food_order + " pizzas for you. Thank you for your order."
      print("Order Confirmed : " + success)
else :
      print("We hope you would purchase pizza next time.")