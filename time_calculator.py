def add_time(start, duration, day=None):
    week_days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    start_hours, start_minutes = start.rsplit(":")
    start_minutes, start_dayNight = start_minutes.rsplit()
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)

    duration_hours, duration_minutes = duration.rsplit(":")
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)

    # change to military time
    if start_dayNight == "PM":
        start_hours += 12

    minutes_sum = (start_minutes + duration_minutes) % 60
    hours_sum = (
        start_hours + duration_hours + ((start_minutes + duration_minutes) // 60)
    )

    # new_hours back to 12-hr system
    new_hours = (hours_sum % 24) % 12

    if new_hours == 0:
        new_hours = 12

    # days
    new_day = hours_sum // 24

    # pm to am, am to pm
    new_dayNight = ""
    if (hours_sum % 24) <= 11:
        new_dayNight = "AM"
    else:
        new_dayNight = "PM"

    # simple addition cases
    if minutes_sum <= 9:
        minutes_sum = "0" + str(minutes_sum)
    else:
        minutes_sum = str(minutes_sum)

    new_time = f"{new_hours}:{minutes_sum} {new_dayNight}"

    # multiple-day addition cases
    if day == None:
        if new_day == 0:
            return new_time
        if new_day == 1:
            return new_time + " (next day)"
        return f"{new_time} ({str(new_day)} days later)"
    else:
        final_day = (week_days[day.lower().capitalize()] + new_day) % 7
        for i, j in week_days.items():
            if j == final_day:
                final_day = i
                break
        if new_day == 0:
            return new_time + ", " + final_day
        if new_day == 1:
            return f"{new_time}, {final_day} (next day)"
        return f"{new_time}, {final_day} ({str(new_day)} days later)"
