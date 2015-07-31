from datetime import date


def val_temp(temp):
    """
    Return True if temp is an integer between -90 and 60 inclusive, False
    otherwise.
    """
    return ((temp.startswith('-') and temp[1:].isdigit() or temp.isdigit())
            and -90 <= int(temp) <= 60)


def update():
    # get number of cities to input
    while True:
        no_of_cities = input("Enter number of cities to input: ")
        if no_of_cities.isdigit() and 0 < int(no_of_cities) <= 3:
            no_of_cities = int(no_of_cities)
            print()
            break
        else:
            print("* Invalid number. Try again. *")

    # get name and temp data for each city
    greatest_abs_diff = -1
    CITIES = set()
    for _ in range(no_of_cities):
        print('-'*50)

        while True:
            city = input("Enter city name: ").title()
            if city.isalpha() and city not in CITIES:
                CITIES.add(city)
                break
            else:
                print(" * Invalid city. Try again. *")

        while True:
            highest_temp = input("Enter highest temperature: ")
            if val_temp(highest_temp):
                highest_temp = int(highest_temp)
                break
            else:
                print("* Invalid temperature. Try again. *")

        while True:
            lowest_temp = input("Enter lowest temperature: ")
            if val_temp(lowest_temp) and int(lowest_temp) <= highest_temp:
                lowest_temp = int(lowest_temp)
                break
            else:
                print(" * Invalid temperature. Try again. *")

        abs_diff = highest_temp - lowest_temp

        # get city captured today with greatest abs diff
        if abs_diff > greatest_abs_diff:
            greatest_abs_diff = abs_diff
            final_city = city

    # display info for city with greatest abs diff captured today
    print("\nCity with greatest absolute difference today: {0}"
          .format(final_city))
    print("Absolute difference: {0}°C".format(greatest_abs_diff))

    # get data for city currently in file
    infile = open("WIDEST.txt", 'r')
    file_date = infile.readline()[:-1]
    year, month, day = file_date.split('-')
    file_city, file_abs_diff = infile.readline()[:-1].split(',')
    infile.close()

    # calculate the days since last update of file
    elapsed_days = (date.today() - date(int(year), int(month), int(day))).days
    print("Number of days elapsed since last reading occured: {0}"
          .format(elapsed_days))

    # update file with new data if greater abs diff found today
    if greatest_abs_diff > int(file_abs_diff):
        outfile = open("WIDEST.txt", 'w')
        current_date = str(date.today())
        print(current_date, file=outfile)
        print("{0},{1}".format(final_city, greatest_abs_diff), file=outfile)
        outfile.close()

        print("\nGreater absolute difference captured today.")
        print("- WIDEST.txt updated -")
    else:
        print("\nNo greater absolute difference captured today.")
