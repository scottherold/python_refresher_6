# Write a small program to display information on the frou clocks whose
# functions we have just looked at: i.e. time(), perf_counter(),
# monotonic() and process_time().
#
# Use the documentation for hte get_clock_info() function to work out
# how to call it for each of the clocks

import time

time_clock = time.get_clock_info('time')
time_mono = time.get_clock_info('monotonic')
time_perf = time.get_clock_info('perf_counter')
time_process = time.get_clock_info('process_time')

times = [time_clock, time_mono, time_perf, time_process]

for time_var in times:
    print(time_var)