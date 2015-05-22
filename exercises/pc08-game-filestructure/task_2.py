def UpdateMaster():
    Masterfile = open("MASTER.DAT", 'r')
    Transactionfile = open("NEWLOG.DAT", 'r')
    New_Masterfile = open("NEW_MASTER.DAT", 'w')

    # get 1st record
    MasterRecord = Masterfile.readline()[:-1]
    TransactionRecord = Transactionfile.readline()[:-1]

    MasterKey = MasterRecord[:15]
    TransactionKey = TransactionRecord[18:33]

    while MasterRecord != '' and TransactionRecord != '':  # not EOF
        if MasterKey < TransactionKey:  # no update necessary
            print(MasterRecord, file=New_Masterfile)

            MasterRecord = Masterfile.readline()[:-1]
            MasterKey = MasterRecord[:15]

        elif MasterKey == TransactionKey:  # existing record found
            # update record #

            # get scores
            master_score = MasterRecord[15:18]
            trans_score = TransactionRecord[33:36]

            # get datetimes
            master_datetime = MasterRecord[18:36]
            trans_datetime = TransactionRecord[:18]

            # choose correct new score (highest) and datetime
            if int(master_score) >= int(trans_score):
                new_score = master_score
                new_datetime = master_datetime
            else:
                new_score = trans_score
                new_datetime = trans_datetime

            # increment no. of games played
            new_total_games = int(MasterRecord[36:39]) + 1

            # last played
            last_datetime = TransactionRecord[:18]

            # get next trans record
            TransactionRecord = Transactionfile.readline()[:-1]
            TransactionKey = TransactionRecord[18:33]

            # handle duplicates in trans, if any
            while MasterKey == TransactionKey:
                trans_score = TransactionRecord[33:36]

                trans_datetime = TransactionRecord[:18]

                if int(trans_score) >= int(new_score):
                    new_score = trans_score
                    new_datetime = trans_datetime

                new_total_games += 1

                last_datetime = TransactionRecord[:18]

                # get next trans record
                TransactionRecord = Transactionfile.readline()[:-1]
                TransactionKey = TransactionRecord[18:33]

            # adjustments
            new_score = str(new_score).rjust(3, ' ')
            new_total_games = str(new_total_games).rjust(3, ' ')

            print("{0}{1}{2}{3}{4}"
                  .format(MasterKey, new_score, new_datetime,
                          new_total_games, last_datetime),
                  file=New_Masterfile)

            # get next master record
            MasterRecord = Masterfile.readline()[:-1]
            MasterKey = MasterRecord[:15]

        elif MasterKey > TransactionKey:  # record in trans is new
            orig_TransactionKey = TransactionKey

            # make new record #
            new_score = TransactionRecord[33:36]
            new_datetime = TransactionRecord[:18]
            new_total_games = 1

            # get next trans record
            TransactionRecord = Transactionfile.readline()[:-1]
            TransactionKey = TransactionRecord[18:33]

            # handle duplicates in trans, if any
            while orig_TransactionKey == TransactionKey:
                trans_score = TransactionRecord[33:36]

                trans_datetime = TransactionRecord[:18]

                if int(trans_score) >= int(new_score):
                    new_score = trans_score
                    new_datetime = trans_datetime

                new_total_games += 1

                last_datetime = TransactionRecord[:18]

                # get next trans record
                TransactionRecord = Transactionfile.readline()[:-1]
                TransactionKey = TransactionRecord[18:33]

            # adjustments
            new_score = str(new_score).rjust(3, ' ')
            new_total_games = str(new_total_games).rjust(3, ' ')

            print("{0}{1}{2}{3}{4}"
                  .format(orig_TransactionKey, new_score, new_datetime,
                          new_total_games, new_datetime),
                  file=New_Masterfile)

    while MasterRecord != '':  # handle leftovers in Masterfile
        print(MasterRecord, file=New_Masterfile)

        MasterRecord = Masterfile.readline()[:-1]

    while TransactionRecord != '':  # handle leftovers in Transactionfile
            orig_TransactionKey = TransactionKey

            # make new record #
            new_score = TransactionRecord[33:36]
            new_datetime = TransactionRecord[:18]
            new_total_games = 1

            # get next trans record
            TransactionRecord = Transactionfile.readline()[:-1]
            TransactionKey = TransactionRecord[18:33]

            # handle duplicates in trans, if any
            while orig_TransactionKey == TransactionKey:
                trans_score = TransactionRecord[33:36]

                trans_datetime = TransactionRecord[:18]

                if int(trans_score) >= int(new_score):
                    new_score = trans_score
                    new_datetime = trans_datetime

                new_total_games += 1

                last_datetime = TransactionRecord[:18]

                # get next trans record
                TransactionRecord = Transactionfile.readline()[:-1]
                TransactionKey = TransactionRecord[18:33]

            new_score = str(new_score).rjust(3, ' ')
            new_total_games = str(new_total_games).rjust(3, ' ')

            print("{0}{1}{2}{3}{4}"
                  .format(orig_TransactionKey, new_score, new_datetime,
                          new_total_games, new_datetime),
                  file=New_Masterfile)

    Masterfile.close()
    Transactionfile.close()
    New_Masterfile.close()


# UpdateMaster()
