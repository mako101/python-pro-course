list = [3,5,6,2,234,34,3,356,21,1,3,56,6,4,]

print(list)

list.insert(2,int('808'))
print(list)


list.remove(6)
print(list)

list.remove(list[1]) #5
print(list)

print(list.index(356))

print(list.count(3))

#list.sort() - this cannot be stored as variable, changes original the value of list

sorted_list = sorted(list, reverse=True)

for i in sorted_list:
    print("%d has an index of %d" % (i, list.index(i)))


print(list)
list.reverse()  # reverses WITHOUT sorting
print(list)