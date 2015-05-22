def PrepareData():
    usernames = []
    datetimes = []
    scores = []

    # retrieve data from old file
    with open("OLDLOG.DAT", 'r') as infile:
        for line in infile:
            Datetime, Username, Score = line[:-1].split(',')

            Username = Username.ljust(15, ' ')
            Score = Score.rjust(3, ' ')

            usernames.append(Username)
            datetimes.append(Datetime)
            scores.append(Score)

    # sorting usernames (key) with corresponding datetimes and scores
    for loop in range(len(usernames)-1):
        for i in range(len(usernames)-1):
            if usernames[i] > usernames[i+1]:
                usernames[i], usernames[i+1] = usernames[i+1], usernames[i]
                datetimes[i], datetimes[i+1] = datetimes[i+1], datetimes[i]
                scores[i], scores[i+1] = scores[i+1], scores[i]

    # output to new file in correct format
    with open("NEWLOG.DAT", 'w') as outfile:
        for Datetime, Username, Score in zip(datetimes, usernames, scores):
            print("{0}{1}{2}".format(Datetime, Username, Score), file=outfile)


# PrepareData()
