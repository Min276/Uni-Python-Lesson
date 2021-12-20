
#Hello Everyone !!

# 1
#This function works well, and it check whether the string is lower case or not by
#taking a parameter (s), using islower() and looping through it.

def any_lowercase1(s):
for c in s:
if c.islower():
return True
else:
return False

#Output

any_lowercase1("a")
True
any_lowercase1("A")
False
any_lowercase1("k")
True


# 2

#This function doesn't work well as it keeps showing True for upper case letter. It has got
#some errors there especially in conditonal statement, it should be just c not c with single quotes,
#and boolean values doesn't really need quotes as well.

def any_lowercase2(s):
for c in s:
if 'c'.islower():
return 'True'
else:
return 'False'

#Output

any_lowercase2("a")
'True'
any_lowercase2("A")
'True'
any_lowercase2("B")
'True'


# 3
#This function works well even though it doesn't include conditional statement.
def any_lowercase3(s):
for c in s:
flag = c.islower()
return flag

#Output

any_lowercase3("s")
True
any_lowercase3("B")
False
any_lowercase3("K")
False


# 4
#This function works properly, and outputs the correct result, using the logical operator (or).
def any_lowercase4(s):
flag = False
for c in s:
flag = flag or c.islower()
return flag

#Output

any_lowercase4("S")
False
any_lowercase4("a")
True
any_lowercase4("B")
False


# 5

#This function also works well and prints out the correct result, using conditional statement.
def any_lowercase5(s):
for c in s:
if not c.islower():
return False
return True

#Output

any_lowercase5("K")
False
any_lowercase5("G")
False
any_lowercase5("s")
True