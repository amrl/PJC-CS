from task_3_2 import HashKey


def LookUpCurrency():
    country = input("Enter country name: ").upper()
    address = HashKey(country)

    infile = open("DIRECTCURRENCIES.txt", 'r')
    max_address = len(infile.read()) // 30

    while True:
        infile.seek(30*(address-1))
        record = infile.read(30)

        file_country, rate = record.split('#')[0], record.split('#')[-1]

        if country == file_country:  # country found in file
            print("\nAddress: {0}".format(address))
            print("Country: {0}".format(country))
            print("Exchange rate: {0}".format(rate))
            break
        else:
            address += 1  # linear probing
            if address > max_address:
                print("\n- Country not found in file -")
                break

    infile.close()
