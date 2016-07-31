import statistics

import shelve


print(dir(statistics.mean))
help(statistics.mean)


print(dir(shelve.Shelf))


#help(shelve.Shelf)

print(dir())



for object in dir(statistics):
    if object[0] != '_':
        print(object)