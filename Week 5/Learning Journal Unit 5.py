#Learning Journal Unit 5


#1. 

#modefined code

prefixes = 'JKLMNOPQ'

suffix = 'ack'



for letter in prefixes:

     if letter in 'OQ':

         print(letter + 'u' + suffix)

     else:

         print(letter + suffix)



#Ouput

#Jack

#Kack

#Lack

#Mack

#Nack

#Ouack

#Pack


#Quack



#2. 

#input code

greeting = 'Hello December'

change = 'Sweet ' + greeting[6:]

print(change)

#output code

Sweet December



#input code

greeting = 'Hello December'

word = greeting[0:5] + ' World'

print(word)

#output code

Hello World



#input

wish =  ", bring us healthy and happiness along with the blessings" 

sentence = greeting[:] + wish

addon = "Have some " + wish[-9:-1]

print(sentence)

print(addon)



#output

#Hello December, bring us healthy and happiness along with the blessings

#Have some blessing