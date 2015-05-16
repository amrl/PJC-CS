from linkedlist import LinkedList


SCORE_LIST = LinkedList()
with open("GAME.dat", 'r') as infile:
    for line in infile:
        player_id, score = line[:-1].split()
        SCORE_LIST.add(player_id.lower(), score)


def val_score(score):
    if score.isdigit() and int(score) >= 0 and int(score) <= 20:
        return True
    else:
        return False


def val_id(player_id):
    if len(player_id) >= 3 and player_id[0].isalpha():
        return True
    else:
        return False


def update(linkedlist):
    while True:
        print(linkedlist)  # display the current list

        while True:  # get player ID
            player_id = input("Enter player ID (0 to exit): ")
            if player_id == '0':
                return  # EXIT
            elif not val_id(player_id):
                print("\n- Invalid player ID -\n")
            else:
                break  # all okay

        while True:  # get score
            score = input("Enter score for {0}: ".format(player_id))
            if not val_score(score):
                print("\n- Invalid score -\n")
            else:
                break  # all okay

        # header
        print("\nPlayer: ", player_id)
        print('-'*20)

        print("Old rank: ", linkedlist.get_rank(player_id))

        # updating list with new player/score
        if linkedlist.exists(player_id):
            new_score = linkedlist.get_score(player_id) + int(score)
            # remove player node and readd to place player node into the
            # new correct position
            linkedlist.remove(player_id)
            linkedlist.add(player_id, new_score)
        else:
            linkedlist.add(player_id, score)

        print("New rank: ", linkedlist.get_rank(player_id))
        print()


# update(SCORE_LIST)
