#THIS PROGRAM SAY SHELLO AND ASKS FOR MY NAME
print('HELLO WORLD')
print('What is your name?') #ask for name
myName = input()
print('It is good to meet you,' + myName)
print('The length of your name is: ')
print(len(myName))
print('How old are you?') #ask for age
myAge = input ()
print('You will be ' + str(int(myAge) + 1) + 'in a year')