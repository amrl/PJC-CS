from task_3_2 import HashKey


def FindCollisions():
    infile = open("NEWCURRENCIES.txt", 'r')
    searchfile = open("DIRECTCURRENCIES.txt", 'r')

    collisions = []
    for line in infile:
        country, rate = line[:-1].split(',')
        supposed_address = HashKey(country)

        searchfile.seek(30*(supposed_address-1))
        record = searchfile.read(30)
        file_country = record.split('#')[0]

        if country != file_country:  # record affected by collision
            real_address = supposed_address + 1

            while True:
                searchfile.seek(30*(real_address-1))
                record = searchfile.read(30)

                file_country = record.split('#')[0]

                if country == file_country:  # country found in file
                    break
                else:
                    real_address += 1  # linear probing

            collisions.append((country, rate, supposed_address, real_address))

    infile.close()
    searchfile.close()

    # display header
    print("\n- Records affected by collisions -")
    print("{0:^5}|{1:^16}|{2:^16}|{3:^18}|{4:^16}".format(
          "No.", "Country", "Rate", "Supposed address", "Real address"))
    print('-'*75)
    # display records affected by collisions
    for index, data in enumerate(collisions):
        print("{0:^5}|{1:^16}|{2:^16}|{3:^18}|{4:^16}"
              .format(index+1, data[0], data[1], data[2], data[3]))
