# # fun with time
# import time

# # epoch
# print("The epoch on this system starts at " + time.strftime(
#     '%c', time.gmtime(0)))

# # current local time
# # using first tuple position, second time method
# print("The current timezome is {0} with an offset of {1}".format(
#     time.tzname[0], time.timezone))

# # daylight savings check
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])

# # local time
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


# fun with datetime
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())