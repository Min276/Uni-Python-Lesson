#Learning Journal Unit 4

#Part 1
#Firstly, I defined a function named hypotenuse and added two arguments in the function for the two sides of the triangle.

# increment 1

def hypotenuse(a,b):

       return 0.0



#Secondly, I added exponents to the arguments I added in the function, then I started printing out the squared values.  

# increment 2

def hypotenuse(a,b):

       fist_squared = a**2

       second_squared = b**2

       print('Fist squared is ', fist_squared)

       print('Second squared is ', second_squared)

       return 0.0



#hirdly, I removed the unnecessary parts of the function, and make it compact overall, and make some addition between squared values.

# increment 3

def hypotenuse(a,b):

       squared = a**2 + b**2

       print('squared is ', squared)

       return 0.0



#Finally, I imported math function to use math.sqrt() to get the value of hypotenuse of a right triangle, removing a print statement which is not necessary, then printing out its value.

# increment 4

import math

def hypotenuse(a,b):

       squared = a**2 + b**2

       result = math.sqrt(squared)


       return result



#Output

>>> hypotenuse(3,4)

5.0

>>> hypotenuse(4,5)

6.4031242374328485

>>> hypotenuse(4,3)

5.0



Part 2
I write a python program that prints out the age based on the birthyear and the currentyear of person, animal or anything you could imagine of.

Firstly, I defined a function and added two arguments in the function.

#increment 1

def print_age(birthyear, currentyear):

       return 0

Secondly, I started printing out the value, making some calculations.

#increment 2

def print_age(birthyear, currentyear):

      print("Birth Year: ", birthyear)

      print("Current Year: ", currentyear)

      age = currentyear - birthyear

      print("Your age is " , age)

Finally, I added the conditon to check the data types that user entered, not to output irrelevant things or numbers.

#increment 3

def print_age(birthyear, currentyear):

       if(type(birthyear) == type(currentyear)):

               age = currentyear - birthyear

               print("Your age is " , age)

       else :

               print("Pls enter valid inputs for year")



#Output

print_age(2003,2021)

#Your age is  18

print_age(1990,2021)

#Your age is  31

print_age(1999,2021)


#Your age is  22



#Part 3


#I feel like I get some low grades than I expected first about the rating that I have received from my peers, and I think it is not that satisfying but the feedbacks are said to be not bad though.



#For the feeedbacks I provided others, I think it may not be that great, but at least, they might not feel upset or something bad about my feedbacks. I am not the kind of person who only gives some few rating, but instead I mostly give good ratings without hesitatin if the content is appeared to be good, and complete.