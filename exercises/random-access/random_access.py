# INPUT FILES: asia.csv, NEWFILE2.txt, searchasia.dat
# OUTPUT FILES: NEWFILE1.txt, NEWFILE2.txt


def HashAsia(country):
    ascii_sum = 0
    for c in country:
        ascii_sum += ord(c)

    address = ascii_sum % 47 + 1  # 47 or 30???

    return address


def GetOne():
    infile = open('asia.csv', 'r')
    infile.readline()  # ignore 1st line (header)

    country, pop = infile.readline().split(',')
    pop = pop[:-1]

    address = HashAsia(country)

    string = country.ljust(20, '#') + pop.ljust(10, '#')

    outfile = open('NEWFILE1.txt', 'w')
    outfile.seek((address-1) * 30)
    outfile.write(string)

    infile.close()
    outfile.close()

    print("File output to NEWFILE1.txt")


def getFreePosition(startposition, outfile):
    # global count  # redo without using global

    count = 0

    while True:
        outfile.seek(startposition)
        if outfile.read(1).isalpha():
            print("Collision encountered at address", startposition)
            print()
            count += 1
            startposition += 30
        else:
            break

    return startposition


def GetAll():
    infile = open('asia.csv', 'r')
    infile.readline()  # ignore 1st line (header)

    outfile = open('NEWFILE2.txt', 'w+')

    for line in infile:

        country, pop = line.split(',')
        pop = pop[:-1]

        address = HashAsia(country)
        string = country.ljust(20, '#') + pop.ljust(10, '#')

        seekposition = getFreePosition((address-1) * 30, outfile)

        outfile.seek(seekposition)
        outfile.write(string)

    infile.close()
    outfile.close()

    # print("Number of collisions encountered:", count)
    print("\nFile output to NEWFILE1.txt")


def Find(seekposition, infile, country):
    while True:

        infile.seek(seekposition)

        if infile.read(len(country)) == country:
            infile.seek(seekposition)
            string = infile.read(30)
            country, pop = string[:20], string[20:]
            break
        else:
            seekposition += 30

    country = country.replace('#', '')
    pop = pop.replace('#', '')
    address = int(seekposition / 30 + 1)

    return address, country, pop


def SearchCountry():
    infile = open('NEWFILE2.txt', 'r')

    country = input("Enter country name: ")
    address = HashAsia(country)

    seekposition = (address-1) * 30

    address, country, pop = Find(seekposition, infile, country)

    print("Address:", address)
    print("Country:", country)
    print("Population:", pop)

    infile.close()


def SearchSomeCountries():
    searchfile = open('searchasia.dat', 'r')
    infile = open('NEWFILE2.txt', 'r')

    countries = searchfile.read().split(', ')
    for country in countries:

        address = HashAsia(country)

        seekposition = (address-1) * 30

        address, country, pop = Find(seekposition, infile, country)

        print("Address:", address)
        print("Country:", country)
        print("Population:", pop)
        print()

    searchfile.close()
    infile.close()
