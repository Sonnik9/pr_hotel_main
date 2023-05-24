def convert_to_24_hours(time_str):
    hour, minute = map(int, time_str[:-3].split(":"))
    period = time_str[-2:]

    if period == "PM" and hour < 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"
time_12_hour = "7:00 AM"
time_24_hour = convert_to_24_hours(time_12_hour)
print(time_24_hour)  # Output: 19:00

import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
print(current_date)

# python testFormatTime.py
