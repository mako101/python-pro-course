# OLD (Python 2 based) format - string formatting operator
# Can only interpret each value in order from left to right!

age = 25
print("My age is %d %s, %d %s" % (age, 'years', 6, 'months'))

for i in range(1, 11):
    # pad out the inserted value to x amount of characters, eg %2d is ' 1'
    print("No. %2d squared is %3d and cubed is %5d" % (i, i ** 2, i ** 3))

# Specify number of decimals
print('Pi is approximately %10.50f' % (22 / 7))

print("My name is %s" % ('Bob ' + 'Smith'))


# NEW (Python 3 based) format - replacement field
# Can be ordered any way you like!

print('''
    I am {2}.
    He is {1}.
    And she is {0}!!!
    '''.format('third', 'second', 'first'))


# Supports the same operations as the old method
print("No. {0:2} squared is {1 and cubed is %5d" % (i, i ** 2, i ** 3))