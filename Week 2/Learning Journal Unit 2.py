#Learning Journal Unit 2

#Part 1 Question

#The volume of a sphere is 4/3πr3, where π has the value of "pi" given in Section 2.1 of your textbook. Write a function called print_volume (r) that takes an argument for the radius of the sphere, and prints the volume of the sphere.

#Call your print_volume function three times with different values for radius.

#Include all of the following in your Learning Journal:

#The code for your print_volume function.
#The inputs and outputs to three calls of your print_volume.

#Part 2 Question

#Write your own function that illustrates a feature that you learned in this unit. The function must take at least one argument. The function should be your own creation, not copied from any other source. Do not copy a function from your textbook or the Internet.

#Include all of the following in your Learning Journal:

#The code for the function that you invented.
#The inputs and outputs to three calls of your invented function.
#A description of what feature(s) your function illustrates.  


#Part 1 Answers

#This function basically prints out the volume of the

#sphere using the pi's value from the text book.



 def print_volume (r) :

     pi = 3.141592653589793

     volume = (4/3 * pi) * (r ** 3)

     return volume



#outputs 

print_volume(1)

4.1887902047863905



print_volume(5)

523.5987755982989



print_volume(10)

4188.790204786391



#Part 2 Answer

#I use string concatenation, return keyword, and function with 

#two parameters and two arguments. I apply all those features to 

#make a small and simple love_letter generator.



 def love_letter(name, crush) :

      greet = "Dear " + crush + ", "

      print(greet + " I lowkey fell in love with you since the day I first saw you. ")

      print(" You were just so attractive that my heart leap up at the moment I gazed at you. ")

      print(" I could be your soul mate who will ever be by your side for the rest of my life. ")

      print(" Baby, please let me be yours. Looking forward to hearing from you !! ")

      return " Yours sincerely, " + name



#Outputs

love_letter("Min", "Zin")

#Dear Zin,  I lowkey fell in love with you since the day I first saw you.

 #You were just so attractive that my heart leap up at the moment I gazed at you.

 #I could be your soul mate who will ever be by your side for the rest of my life.

 #Baby, please let me be yours. Looking forward to hearing from you !!

#' Yours sincerely, Min'



love_letter("Min", "Su Su")

#Dear Su Su,  I lowkey fell in love with you since the day I first saw you.

 #You were just so attractive that my heart leap up at the moment I gazed at you.

 #I could be your soul mate who will ever be by your side for the rest of my life.

 #Baby, please let me be yours. Looking forward to hearing from you !!

#' Yours sincerely, Min'



love_letter("Min", "Sophia")

#Dear Sophia,  I lowkey fell in love with you since the day I first saw you.

 #You were just so attractive that my heart leap up at the moment I gazed at you.

 #I could be your soul mate who will ever be by your side for the rest of my life.

 #Baby, please let me be yours. Looking forward to hearing from you !!

#' Yours sincerely, Min'