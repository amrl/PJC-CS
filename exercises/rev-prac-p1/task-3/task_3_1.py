def update():
    # get names and rates from old file
    old_file = open("CURRENCIES.txt", 'r')
    OLD_NAMES = []
    OLD_RATES = []
    for line in old_file:
        country, rate = line[:-1].split(',')
        OLD_NAMES.append(country)
        OLD_RATES.append(rate)
    old_file.close()

    # get names and rates from update file
    update_file = open("UPDATED.txt", 'r')
    UPDATED_NAMES = []
    UPDATED_RATES = []
    for line in update_file:
        country, rate = line[:-1].split(',')
        UPDATED_NAMES.append(country)
        UPDATED_RATES.append(rate)
    update_file.close()

    # get names and rates found in old file but NOT in update file
    NEW_NAMES = []
    NEW_RATES = []
    for index, country in enumerate(OLD_NAMES):
        if country not in UPDATED_NAMES:
            NEW_NAMES.append(country)
            NEW_RATES.append(OLD_RATES[index])

    # combine (records from old file with no updates) with (all records in
    # update file)
    NEW_NAMES += UPDATED_NAMES
    NEW_RATES += UPDATED_RATES

    # write records obtained to new file
    new_file = open("NEWCURRENCIES.txt", 'w')
    for index, country in enumerate(NEW_NAMES):
        print("{0},{1}".format(country, NEW_RATES[index]), file=new_file)
    new_file.close()
