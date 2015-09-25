def get_avg_rainfall():
    # get year from user
    while True:
        user_year = input("Enter a year between 2009 and 2014: ")
        if user_year.isdigit() and 2009 <= int(user_year) <= 2014:
            break
        else:
            print("* Error: Invalid input. Try again.\n*")

    # get total annual rainfall from selected year
    total_rainfall = 0
    infile = open("Rainfall_mth.csv", "r")
    infile.readline()  # ignore header
    for line in infile:
        if line.startswith(user_year):
            rainfall = line[:-1].split(',')[1]
            total_rainfall += float(rainfall)
    infile.close()

    # get number of rainy days in selected year
    total_rainy_days = 0
    infile = open("Rainfall_day.csv", "r")
    infile.readline()  # ignore header
    for line in infile:
        if line.startswith(user_year):
            rainy_days = line[:-1].split(',')[1]
            total_rainy_days += float(rainy_days)
    infile.close()

    # calculate average rainfall
    avg_rainfall = total_rainfall / total_rainy_days

    # display average rainfall
    print("Average rainfall for a rainy day in {0}: {1:.1f}mm"
          .format(user_year, avg_rainfall))
