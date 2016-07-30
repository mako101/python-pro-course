from statistics import mean

foo = input("add a list with commas: ")

bar = [int(grade) for grade in foo.split(',')]

print(bar)




print(mean(bar))


