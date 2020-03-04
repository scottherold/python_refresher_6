# Create a program that allows a user to choose one of up to 9 time
# zones from a menu. You can choose any zones you want from the
# all_timezones list.
#
# The program will then display the time in that timezone, as well as
# the local time and the UTC time.
#
# Display the dates and times in a format suitable for the user of your
# program to understand, and include the timezone name when displaying
# the chosen time

import datetime
import pytz

# data
tz_list = ['CET', 'EET', 'EST', 'GB', 'GMT', 'HST', 'MET', 'MST', 'NZ', 'PRC',
           'ROC', 'ROK', 'WET']

while True:
    # create string from data for UI
    timezones = ', '.join(map(str, tz_list,))

    # user input
    selected_time = input("Please choose a timezone (or 'quit' to exit): " + timezones + '\n').upper()

    # check user input against data
    if selected_time == "QUIT":
        break
    elif selected_time not in tz_list:
        print("\nSorry, that timezone is unavailble.")
    else:
        # Generic Time -- will be formatted
        cur_time = datetime.datetime.utcnow()

        # set timezone
        selected_tz = pytz.timezone(selected_time)

        # formatted time
        local_time = pytz.utc.localize(cur_time).astimezone()
        utc_time = pytz.utc.localize(cur_time).astimezone(pytz.timezone('UTC'))
        input_time = pytz.utc.localize(cur_time).astimezone(selected_tz)
        time_format = '%Y-%m-%d %H:%M:%S'
        
        print("The time in the {} timezone is: ".format(selected_time) + input_time.strftime(
            time_format))
        print("Your local time is: " + local_time.strftime(
            time_format))
        print("The current UTC time is: " + utc_time.strftime(
            time_format))
        print()