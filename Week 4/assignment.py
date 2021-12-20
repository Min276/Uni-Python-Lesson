#check whether it is divisible or not
def is_divisible(x, y):
    #output true if divisible
    if x % y == 0:
           return True
    #output false if not divisible
    else:
           return False

#defining a function that check power and call is_divisible function
def is_power(x, y):
#second argument is equal to 1
    if y == 1 :
           return x == 1
    #two argument are equal to each other
    if x == y :
           return is_divisible(x,y)
    #calling function names
    return is_divisible(x,y) and is_power(int(x/y), y)
      
