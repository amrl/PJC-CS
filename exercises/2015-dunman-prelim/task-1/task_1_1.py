def get_party(letter):
    """Return party name associated with letter"""
    if letter == 'A':
        return "NSP"
    elif letter == 'B':
        return "PAP"
    elif letter == 'C':
        return "WP"
    elif letter == 'V':
        return "Void"


def get_percentage(number, total):
    """Return a percentage the number represents from the total"""
    return number / total * 100


def voting_stats():
    votes = dict()  # {party name: vote count, ...}
    total_votes = 0

    # populate dict with votes in file
    infile = open("ELECTION.txt", "r")
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

    # display results
    print("Results for the Electoral Division of MacPherson")
    for item in votes_count:
        party = item[0]
        percentage = get_percentage(item[1], total_votes)
        print("{0:<5}{1:>5.1f}%".format(party, percentage))
    print("Winner is {0}".format(votes_count[0][0]))
