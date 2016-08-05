
print("House" + 'of cards')

print("House", 'of cards')

#print('I am number' + 5)

print('I am number' , 5)

print(5 , 'is my number')

print("I'm 5")

print("c:\\users\\settings\\text")

print("c:/users/settings/text")



# Testing print capabilities and writing directly to file
test_file = open('testFile2.txt.', 'a')

for i in range(5):
    print(1, 2,3, 4, sep='>:<', end='[---]', file=test_file)

print('\nFinal line', file=test_file)


# Everythng that can be done with strings
#https://docs.python.org/3.1/library/string.html