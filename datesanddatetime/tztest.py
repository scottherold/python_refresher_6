# checks to see if pytz module is installed correctly.
import pytz
import datetime

country = "Europe/Moscow"

# pytz function (from module)
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# all timezone options
for x in pytz.all_timezones:
    print(x)

# all availble country options
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])

# the timezone for each country
# (BV will crash the program as there is no timezone assigned to BV
# -- this is a polymorphism fail, so you must use the .get() method,
# or you must use a boolean to display alternative test)
for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")