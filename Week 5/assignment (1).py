#Part One
import math
#define function
def my_sqrt(a):
     x = 3
     while True:
        y = (x + a/x)/2.0
        if y == x:
           break
        x = y

     return y

#Part Two
#define test function      
def test_sqrt():
    a = 1
    while a<26:
        print('a =', a,'| my_sqrt(a) =',my_sqrt(a),'| math.sqrt(a) =', math.sqrt(a),'| diff =', abs(math.sqrt(a)-my_sqrt(a)))
        a = a + 1
    return 0
