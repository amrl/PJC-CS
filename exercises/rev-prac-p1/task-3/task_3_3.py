from task_3_2 import HashKey


def CreateCurrency():
    # calculate address for record
    # seek to position (max record length * address) in outfile
    # if a record already exist in position, increment address (linear probing)
    # repeat until position is available for writing

    infile = open("NEWCURRENCIES.txt", 'r')
    outfile = open("DIRECTCURRENCIES.txt", 'w+')

    for line in infile:
        country, rate = line[:-1].split(',')
        address = HashKey(country)

        country = country.ljust(15, '#')
        rate = rate.rjust(15, '#')
        record = country + rate

        while True:
            outfile.seek(30*(address-1))
            if outfile.read(1).isalpha():  # collision handling
                address += 1  # linear probing
            else:
                break

        outfile.seek(30*(address-1))
        outfile.write(record)

    infile.close()
    outfile.close()
