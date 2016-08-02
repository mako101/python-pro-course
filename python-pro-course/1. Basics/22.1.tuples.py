
def example():
    return 19,32


a,b = example()

print(a)
print(b)

print()

tuple = (4,3)
x,y = tuple
print(x)
print(y)


print()

tuples = ((3,54),(5,3),(87,52),3,7) # round brackets

try:
    print(type(tuples))

    for a,b in tuples:
        print(a,b)
        print(a * 2)
        print(b * 2)
        print('\n')

except TypeError as t:
    print('Can\'t understand list values in the sequence of tuples:\n', t, '\n')

list = [(3,54),(5,3),(87,52),3,7]
print('List can iterate over anything:', list)
print(type(list))

for x in list:
    print(type(x),x)


print('\n', 'Nested tuples!', '\n')

nested_tuples = (((3,54),(5,3)),((87,52),(3,7)))

for x,y in nested_tuples:
    print(x, 'and', y)
    print(x + (10,3))
    # print(y - (2,1)) doesn't work
    print(x * 2)
    # print(x ** 2) doesn't work
    for x in x,y:
        a = x[0]
        b = x[1]
        print(a)
        print(b)


print('\n', 'SUPER Nested tuples!', '\n')
super_nested_tuples = ((((3,54),(5,3)),((87,52),(3,7))),(((4,5),(7,8)),((43,13),(5,8))))
for x,y in super_nested_tuples:
    print('x =',x)
    print('y =',y)
    for x in x, y:
        a = x[0]
        b = x[1]
        print('a =', a)
        print('b =', b)
        for a in a,b:
            c = a[0]
            d = a[1]
            print('c =', c)
            print('d =', d)


