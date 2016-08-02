import time as t

# These return named tuples
print(t.gmtime(0))
print(t.localtime())
print(t.time())

# eg.
# time.struct_time(tm_year=2016, tm_mon=8, tm_mday=2, tm_hour=15, tm_min=25, tm_sec=29, tm_wday=1, tm_yday=215, tm_isdst=1)

# We can access elements of named tuples by index OR by name
time_here = t.localtime()

print(time_here)


# Referring to tuple field by name
print('Year:', time_here[0], time_here.tm_year)
print('Month:', time_here[1], time_here.tm_mon)


#print standard time!

l = t.localtime()

for i in (range(3)):
    t.sleep(1)
    l = t.localtime()
    print(l.tm_hour, l.tm_min, l.tm_sec, sep=':')

