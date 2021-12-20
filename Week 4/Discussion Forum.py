
#Hello Everyone !

#There are three possibilites to consider if a function
#is not working :

#From Textbook :
#• There is something wrong with the arguments the
#function is getting; a precondition is violated.
#• There is something wrong with the function;
#a postcondition is violated.
#• There is something wrong with the return value
#or the way it is being used.

#My own words :

#=> Arguments that a function receives might be different to its Data Types (for
#example, putting integer data typed values where a function outputs string values

#=> A function that fails to include parameters even though having arguments values
#when it is being called. There might have syntax error like missing out : after defining function's name
#and typing errors, plus indentation error.

#=> There may be something wrong in returning values inside the function. Indentaion erros
#and calling undefined variable names like name error (typos) could be the problem there.


#Preconditon and Postcondition (Reference from a website)

#A precondition is something that must be correct at the start of a function in order for it to work correctly.
#A postcondition is something that the function guarantees is correct when it finishes.

#For 1st Possiblity :

#Wrong Argument (that must be string data type there)

#Input
def resolution(day,username):
wish = "\nPost: I will be trying out something new, and I will make myself productive as possible."
post = "Day : " + day + " , " + "User : " + username
print(post , wish)

resolution(8, "Min_Kyaw")

#Output
Traceback (most recent call last):
resolution(8,"Min_Kyaw")
post = "Day : " + day + " , " + "User : " + username

#TypeError: can only concatenate str (not "int") to str



#For 2nd Possiblity :

#Output
def resolution(day,username):
wish = "\nPost: I will be trying out something new, and I will make myself productive as possible."
post = "Day : " + day + " , " + "User : " + username
print(post , wish)

#IndentationError: unindent does not match any outer indentation level


#For 3rd Possiblity :

#Output
def resolution(day,username):
wish = "\nPost: I will be trying out something new, and I will make myself productive as possible."
post = "Day : " + day + " , " + "User : " + username
return pots, wish

resolution("Wednesday", "Min_Kyaw")

#Traceback (most recent call last):
#NameError: name 'pots' is not defined


#Reference
#https://swcarpentry.github.io/python-novice-inflammation-2.7/08-defensive.html