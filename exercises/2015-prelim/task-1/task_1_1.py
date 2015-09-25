def find_total_annual_rainfall():
    annual_rainfall = dict()  # {year: rainfall, ...}

    # get annual rainfall amount
    infile = open("Rainfall_mth.csv", "r")
    infile.readline()  # ignore header
    for line in infile:
        year_month, rainfall = line[:-1].split(',')
        year = year_month.split('M')[0]
        year, rainfall = int(year), float(rainfall)
        annual_rainfall[year] = annual_rainfall.get(year, 0) + rainfall
    infile.close()

    # convert dict to list of tuples [(year, rainfall), ...]
    annual_rainfall_list = list()
    for year in annual_rainfall:
        annual_rainfall_list.append((year, annual_rainfall[year]))

    # sort by year (ascending)
    for i in range(len(annual_rainfall_list)-1):
        for j in range(len(annual_rainfall_list)-i-1):
            if annual_rainfall_list[j][0] > annual_rainfall_list[j+1][0]:
                temp = annual_rainfall_list[j]
                annual_rainfall_list[j] = annual_rainfall_list[j+1]
                annual_rainfall_list[j+1] = temp

    # display table header
    print('-'*60)
    print("|{0:^10}|{1:^47}|"
          .format("Year", "Total Annual Rainfall (millimetres in 1 d.p.)"))
    print('-'*60)

    # display year and rainfall amountin table form
    for item in annual_rainfall_list:
        year, rainfall = item[0], item[1]
        print("|{0:^10}|{1:^47.1f}|".format(year, rainfall))
    print('-'*60)
