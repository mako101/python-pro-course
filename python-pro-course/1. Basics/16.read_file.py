readMe = open('testFile.txt', 'r').read()

split = readMe.split('\n')

joined = '<|>'.join(split)

readMe2 = open('testFile.txt', 'r').readlines()

print(readMe2)
print(split[1])
print(joined)