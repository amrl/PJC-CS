def get_chip_time(start, end):
    """Return chip time in required format."""
    start_hour, start_min, start_sec = start.split(':')
    end_hour, end_min, end_sec = end.split(':')

    hour_diff = int(end_hour) - int(start_hour)
    min_diff = int(end_min) - int(start_min)
    sec_diff = int(end_sec) - int(start_sec)

    total_diff = hour_diff * 60 * 60 + min_diff * 60 + sec_diff

    chip_hour = total_diff // (60 * 60)
    chip_min = (total_diff - chip_hour * 60 * 60) // 60
    chip_sec = total_diff - chip_hour * 60 * 60 - chip_min * 60

    chip_min = str(chip_min).rjust(2, '0')
    chip_sec = str(chip_sec).rjust(2, '0')

    return "{0} h {1} m {2} s".format(chip_hour, chip_min, chip_sec)


def get_run_time(start, end):
    """Return number of seconds between start and end."""
    start_hour, start_min, start_sec = start.split(':')
    end_hour, end_min, end_sec = end.split(':')

    hour_diff = int(end_hour) - int(start_hour)
    min_diff = int(end_min) - int(start_min)
    sec_diff = int(end_sec) - int(start_sec)

    total_diff = hour_diff * 60 * 60 + min_diff * 60 + sec_diff

    return total_diff


def main():
    infile = open("RACE.txt", "r")
    line = infile.readline()
    fastest_runner, start, end = line[:5], line[5:13], line[13:-1]
    fastest_time = get_run_time(start, end)
    formatted_time = get_chip_time(start, end)
    for line in infile:
        runner, start, end = line[:5], line[5:13], line[13:-1]
        time = get_run_time(start, end)
        if time < fastest_time:
            fastest_runner = runner
            fastest_time = time
            formatted_time = get_chip_time(start, end)
    infile.close()

    print("Fastest runner id: {0}   Chip time: {1}".format(
          fastest_runner, formatted_time))


# main()
