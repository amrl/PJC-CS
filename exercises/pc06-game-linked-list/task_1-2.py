# Task 1


class Node:

    def __init__(self, player_id, score):
        self.id = player_id
        self.score = int(score)
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, player_id, score):
        """
        Insert a new Node into the LinkedList according to score, highest
        first. If same score, follow alphabetical ordering.
        """
        new_node = Node(player_id, score)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            prev = None

            while current is not None and new_node.score <= current.score:
                if new_node.score == current.score:
                    if new_node.id < current.id:
                        if prev is None:
                            temp = self.head
                            self.head = new_node
                            new_node.next = temp
                        else:
                            prev.next = new_node
                            new_node.next = current
                        return

                prev = current
                current = current.next

            if prev is None:
                temp = self.head
                self.head = new_node
                new_node.next = temp
            else:
                prev.next = new_node
                new_node.next = current

    def __str__(self):
        output = ""

        current = self.head
        while current is not None:
            output += "[{0}, {1}]---> ".format(current.id, current.score)
            current = current.next

        return output


SCORE_LIST = LinkedList()
CURRENT_ID_LIST = []  # contains player IDs already in SCORE_LIST

with open("GAME.dat", 'r') as infile:
    for line in infile:
        player_id, score = line[:-1].split()

        SCORE_LIST.add(player_id.lower(), score)
        CURRENT_ID_LIST.append(player_id)


def val_score(score):
    if score.isdigit() and int(score) >= 0 and int(score) <= 20:
        return True
    else:
        return False


def val_ID(player_id):
    if len(player_id) >= 3 and player_id[0].isalpha():
        return True
    else:
        return False


def update():
    player_id = input("Enter player ID: ")
    score = input("Enter score: ")

    if val_ID(player_id) and val_score(score):

        if player_id not in CURRENT_ID_LIST:  # new player to the game
            CURRENT_ID_LIST.append(player_id)

            SCORE_LIST.add(player_id, score)

            print("Old rank: NIL")

        else:
            # find current ranking of existing player
            old_rank = 1
            current = SCORE_LIST.head
            prev = None

            while current.id != player_id:
                prev = current
                current = current.next

                if prev.score != current.score:
                    old_rank += 1

            print("Old rank: ", old_rank)

            # remove player's Node from the list (for reinsertion later)
            if prev is None:
                SCORE_LIST.head = current.next
            else:
                prev.next = current.next

            # reinsert player's Node with new score
            new_score = current.score + int(score)
            SCORE_LIST.add(player_id, new_score)

        # find new ranking of new/updated player
        new_rank = 1
        current = SCORE_LIST.head
        prev = None

        while current.id != player_id:
            prev = current
            current = current.next

            if prev.score != current.score:
                new_rank += 1

        print("New rank: ", new_rank)

    else:
        print("\n*Invalid input.")


# print(SCORE_LIST)
# update()
# print(SCORE_LIST)

# Task 2

def val_rank_range(rank_range):
    try:
        lower, upper = rank_range.split('-')
    except:
        return False

    if lower.isdigit() and upper.isdigit():
        return True
    else:
        return False


def display_rank():
    rank_range = input("Enter a rank range (e.g. 1-3): ")

    ranked_list = []
    rank_count = {}

    if val_rank_range(rank_range):
        lower, upper = rank_range.split('-')
        lower, upper = int(lower), int(upper)

        rank = 1
        current = SCORE_LIST.head
        prev = None

        while current is not None and rank <= upper:
            if rank >= lower:
                ranked_list.append((rank, current.id))
                rank_count[rank] = rank_count.get(rank, 0) + 1

            prev = current
            current = current.next

            if current is None:
                break

            if prev.score != current.score:
                rank += 1

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
        print("\n*Invalid input.")
