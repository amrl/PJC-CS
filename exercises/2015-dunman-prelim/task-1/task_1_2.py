from task_1_1 import get_party, get_percentage


def generate_text_file():
    total_votes = 28481
    NSP_count = round(7/100 * total_votes)   # A
    PAP_count = round(45/100 * total_votes)  # B
    WP_count = round(45/100 * total_votes)   # C
    Void_count = round(3/100 * total_votes)  # V

    outfile = open("TIE.txt", "w")
    for _ in range(NSP_count):
        outfile.write('A\n')
    for _ in range(PAP_count):
        outfile.write('B\n')
    for _ in range(WP_count):
        outfile.write('C\n')
    for _ in range(Void_count):
        outfile.write('V\n')
    outfile.close()


def voting_stats():
    votes = dict()  # {party name: vote count, ...}
    total_votes = 0

    # populate dict with votes in file
    infile = open("TIE.txt", "r")
    for line in infile:
        party = get_party(line[:-1])
        votes[party] = votes.get(party, 0) + 1
        total_votes += 1
    infile.close()

    # conver dict to list of tuples [(party name, vote count), ...]
    votes_count = list()
    for party in votes:
        votes_count.append((party, votes[party]))

    # sort parties by number of votes (descending)
    for i in range(len(votes_count)-1):
        for j in range(len(votes_count)-1-i):
            if votes_count[j][1] < votes_count[j+1][1]:
                temp = votes_count[j]
                votes_count[j] = votes_count[j+1]
                votes_count[j+1] = temp

    # check for ties
    tied_parties = list()
    highest_votes = votes_count[0][1]
    for item in votes_count:
        if item[1] == highest_votes:
            tied_parties.append(item[0])

    # display results
    print("Results for the Electoral Division of MacPherson")
    for item in votes_count:
        party = item[0]
        percentage = get_percentage(item[1], total_votes)
        print("{0:<5}{1:>5.1f}%".format(party, percentage))

    # display message according to if tie happened or not
    if len(tied_parties) >= 2:
        parties = ' and '.join(tied_parties)
        print("Revote between", parties)
    else:
        print("Winner is {0}".format(votes_count[0][0]))
