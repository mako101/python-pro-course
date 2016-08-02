from statistics import *

myList = [5,5,12,74,85,1,7,4,58,587,8,8,8,5,9,7,744,7,85,12,5,]

for n in myList:
    print(n,end=' ')

print('mean is', mean(myList))

print('median is', median(myList))

print('mode is', mode(myList))

print('standard deviation is', stdev(myList))

print('variance is', variance(myList))








