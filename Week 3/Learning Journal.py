#Learning Journal Unit 3
#1. Copy the countdown function from Section 5.8 of your textbook.

def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

#Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

countup(-3)
-3
-2
-1
#Blastoff!

#Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

#If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

#Provide the following.

#The code of your program.
#Output for the following input: a positive number, a negative number, and zero.
#An explanation of your choice for what to call for input of zero.

#2. Write your own unique Python program that has a runtime error. Do not copy the program from your textbook or the Internet. Provide the following.

#The code of your program.
#Output demonstrating the runtime error, including the error message.
#An explanation of the error message.
#An explanation of how to fix the error.


#Answers

#1. Recursive function countup

def countup(n) :

     if n >= 0 :

        print('Blastoff!')

     else :

        print(n)

        countup(n+1)


countup(-3)

-3

-2

-1

#Blastoff!



#Keyboard Input
number = int(input("Enter a number :"))

    if number > 0 :

          countdown(number) 

    elif number < 0 :

          countup(number)

    else :

          countup(number)

def countdown(n) :

       if n <= 0 :

           print('Blastoff!')

       else :

           print(n)

           countdown(n-1)

def countup(n) :

       if n >= 0 :

           print('Blastoff!')

       else :

           print(n)

           countup(n+1)

#>>> Enter a number : 3

3

2

1

#Blastoff!




#>>> Enter a number : -3

-3

-2

1

#Blastoff!

#>>> Enter a number : 0
#Blastoff!


#I chose countup function for input of zero,

#as I think that zero is neutral number and

#it need to be a positive number rather than

#being a negative number. That's why I prefer

#countup function to countdown function.



#2. Runtime Error
price = int(input("How much prices cost ? "))

tax = price * 0.5 

total = price + tax 

print("Total Amount : " , Total)



#NameError: name 'Total' is not defined



#I think name error is a part of runtime error

#as it outputs its error message after the program

#has fully run. The program finds out the variable

#name is wrong so it prints out NameError after it

#has run. 



#We can just simply change the wrong variable name 

#"Total" to  "total" so as to fix the error in our program.