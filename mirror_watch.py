def mirrored_time(realtime: str) -> str:
    time_list = realtime.split(":")
    time_list = [int(x) for x in time_list]
    hours, minutes = time_list

    if hours >= 12:
        hours = hours - 12
    if minutes > 0:
        minutes = 60 - minutes
        hours = 11 - hours
    elif minutes == 0:
        hours = 12 - hours

    ans = ''
    if hours < 9:
        ans = f"0{hours}"
    else:
        ans = f"{hours}"
    if minutes < 9:
        ans = f"{ans}:0{minutes}"
    else:
        ans = f"{ans}:{minutes}"
    return ans


print(mirrored_time("09:00"))
