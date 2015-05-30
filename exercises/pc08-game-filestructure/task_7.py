from task_4 import HashKey


def DirectLookup(username):
    address = HashKey(username)

    with open("FASTER.DAT", 'r') as infile:
        # get the address of the last record in the file
        max_char = len(infile.read())
        max_address = max_char // 57

        # find address of record containing the supplied username
        infile.seek((address-1) * 57)
        while infile.read(15).rstrip() != username:
            address += 1
            if address > max_address:  # available addresses exhausted
                print("- User not found -")
                return

            infile.seek((address-1) * 57)

        # move to correct address
        infile.seek((address-1) * 57)

        # retrieve and split the record from the address
        record = infile.read(57)
        highest_score = record[15:18].lstrip()
        datetime = record[18:36]
        games_played = record[36:39].lstrip()
        last_played = record[39:]

        # display stats of the player
        print("Username:", username)
        print("Highest score:", highest_score)
        print("Datetime:", datetime[:10], datetime[10:])
        print("Total games:", games_played)
        print("Last played:", last_played[:10], last_played[10:])


# DirectLookup("buttercurry64")
