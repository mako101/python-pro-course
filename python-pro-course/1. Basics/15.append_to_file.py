base = 'foo bsr baz'


file = open('testFile.txt.txt', 'a')
for i in range(1,6):
    text = base + ' ' + str(i)
    file.write(text)
    file.write('\n')
file.close

