import time

print(time.tzname)

print("The epoch on this system starts at" + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))


if time.daylight != 0:
    print("\tDaylight savings is in effect in this location")
    print("\tThe DST timezone is " + time.tzname[1])

# http://strftime.org/
print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


