# Time Basics
# import time

# # prints start of epoch as tuple
# print(time.gmtime(0))

# # produces current locatime as a tuple
# time_here = time.localtime()
# print(time_here)

# # two ways of outputting the data (via tuple index, or through built in
# # methods)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

# Time manipulation
import time
from time import perf_counter as my_timer
import random

input("Press enter to start ")

# records time between start and stop
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop ")

end_time = my_timer()

# prints and formats time data from start/end
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

# prints time to hit button
print("Your reaction time was {} seconds".format(end_time - start_time))