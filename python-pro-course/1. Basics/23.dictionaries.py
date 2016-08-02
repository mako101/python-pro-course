classGrades = {'Bob': 100, 'Sam': 80, 'Vik':90 }
print(classGrades)
print(type(classGrades))

classGrades['Bob'] = 75
print(classGrades)

classGrades['Kim'] = 93
print(classGrades)

del classGrades['Sam']
print(classGrades)


# lets mix it up!!
allGrades = {'Bob': [80, 65],
             'Sam': (80, 40),
             'Vik':[[90, 87], (50,50)]
             }

print(allGrades)
print(allGrades['Bob'][1])


a,b = allGrades['Vik'][0]
print('a is', a)
print('b is', b)

# getting keys or values, and keys from values
foo=dict(age='35', height='173')

print(foo.keys())

print(foo.values())

for key in foo.keys():
    if foo[key] == '35':
        print(key)
