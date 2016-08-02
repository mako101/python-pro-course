

foo=dict(age='35', height='173')


print(foo.keys())

print(foo.values())

for key in foo.keys():
    if foo[key] == '35':
        print(key)


