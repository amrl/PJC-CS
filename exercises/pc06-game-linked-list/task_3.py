from linkedlist import LinkedList


SCORE_LIST = LinkedList()
with open("GAME.dat", 'r') as infile:
    for line in infile:
        player_id, score = line[:-1].split()
        SCORE_LIST.add(player_id.lower(), score)


def val_rank_range(rank_range, linkedlist):
    try:
        lower, upper = rank_range.split('-')  # correct format
    except:
        return False

    if lower.isdigit() and upper.isdigit():
        if int(lower) > 0 and int(upper) > 0:
            if int(upper) <= linkedlist.get_max_rank():
                return True
    else:
        return False


def display_rank(linkedlist):
    rank_range = input("Enter a rank range (e.g. 1-3): ")

    ranked_list = []
    rank_count = {}

    if val_rank_range(rank_range, linkedlist):
        lower, upper = [int(i) for i in rank_range.split('-')]

        current = linkedlist.head
        while current is not None:
            current_rank = linkedlist.get_rank(current.id)
            if current_rank >= lower and current_rank <= upper:
                ranked_list.append((current_rank, current.id))
                rank_count[current_rank] = rank_count.get(current_rank, 0) + 1
            current = current.next

        # display rank & player ID header
        print("\n{0:^10}{1}{2:^15}".format("Rank", '|', "Player ID"))
        print('-'*25)
        # display real data
        for data in ranked_list:
            print("{0:^10}{1}{2:^15}".format(data[0], '|', data[1]))

        print()

        # display rank count header
        print("{0:^25}".format("Count"))
        print('-'*25)
        # display real data
        for rank in range(lower, upper+1):
            if rank not in rank_count:
                break
            print("Rank #{0}: {1}".format(rank, rank_count[rank]))

    else:
        print("- Invalid input -")


# display_rank(SCORE_LIST)
