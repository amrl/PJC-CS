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
    player_id = input("Enter player ID: ")
    score = input("Enter score: ")

    if val_id(player_id) and val_score(score):

        print("Old rank: ", linkedlist.get_rank(player_id))

        if linkedlist.exists(player_id):
            new_score = linkedlist.get_score(player_id) + int(score)
            # remove player node and readd to place player node into the new
            # correct position
            linkedlist.remove(player_id)
            linkedlist.add(player_id, new_score)
        else:
            linkedlist.add(player_id, score)

        print("New rank: ", linkedlist.get_rank(player_id))

    else:
        print("\n- Invalid input -")


# print(SCORE_LIST)  # BEFORE
# update(SCORE_LIST)
# print(SCORE_LIST)  # AFTER
