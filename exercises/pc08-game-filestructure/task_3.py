def Lookup(Username):
    found = False

    with open("NEW_MASTER.DAT", 'r') as infile:
        for line in infile:
            if line[:15].rstrip() == Username:  # correct record found
                line = line[:-1]
                highest_score = line[15:18].lstrip()
                datetime = line[18:36]
                games_played = line[36:39].lstrip()
                last_played = line[39:]
                found = True
                break

    if found:
        print("Username:", Username)
        print("Highest score:", highest_score)
        print("Datetime:", datetime[:10], datetime[10:])
        print("Total games:", games_played)
        print("Last played:", last_played[:10], last_played[10:])
    else:
        print("- User not found -")


# Lookup("uncletobby65")
