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


from time import perf_counter as my_timer
import random

# def game():
#     input('Press Enter to Start')
wait_time = random.randint(1,5)
start_time = my_timer()
#print(start_time)

t.sleep(wait_time)
end_time = my_timer()
#print(end_time)

print(t.localtime(start_time))
print("Started at: " + t.strftime("%X", t.localtime(start_time)))
print(t.localtime(end_time))
print("Finished at: " + t.strftime("%X", t.localtime(end_time)))

print("The interval was {:.4f} seconds".format(end_time - start_time))

from time import perf_counter
from time import monotonic
from time import process_time

print("\nVarious counters:")
print("perf_counter:", perf_counter())
print("monolithic:", monotonic())
print("process_time: (time for CPU perform operations)", process_time())

