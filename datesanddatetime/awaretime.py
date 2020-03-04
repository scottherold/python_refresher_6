import datetime
import pytz

# Naive time (timezone agnostic)
local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

# Aware time (timzeone intelligent)
# for local time, you DO NOT want to store it as local time
# using the .astimezone() uses UTC and provides the math for the
# local timezone
aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time,
      aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time,
      aware_utc_time.tzinfo))

# timestamps
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp()) # produces data in seconds

s = 1445733000
t = s + (60 * 60) # this puts the timestamp pasth the DST mark

gb = pytz.timezone('GB')
# original timestamp
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
# post DST timestamp
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))