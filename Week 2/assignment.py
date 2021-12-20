#function which outputs one line
def new_line() :
    print('.')

#function which outputs three lines
def three_lines() :
    new_line()
    new_line()
    new_line()

#function which outputs nine lines
def nine_lines() :
    three_lines()
    three_lines()
    three_lines()

#function wich outputs twenty-five lines
def clear_screen() :
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

#calling function to print nine lines
print("Printing nine lines")
nine_lines()

#calling function to print twenty-five lines
print("Printing twenty-five lines")
clear_screen()
