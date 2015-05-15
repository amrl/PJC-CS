class Node:

    def __init__(self, player_id, score):
        self.id = player_id
        self.score = int(score)
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def exists(self, player_id):
        """Check if a player is already in the list."""
        current = self.head

        while current is not None:
            if current.id == player_id:
                return True
            current = current.next

        return False

    def add(self, player_id, score):
        """
        Add a new player node into the list, highest score first.
        If same score, add alphabetically.
        """
        new_node = Node(player_id, score)

        if self.head is None:
            self.head = new_node
        else:
            prev = None
            current = self.head

            # finding correct position
            while current is not None and new_node.score <= current.score:
                if new_node.score == current.score:
                    if new_node.id < current.id:
                        break

                prev = current
                current = current.next

            # insertion
            if current is None:
                prev.next = new_node
            else:
                if prev is None:
                    temp = current
                    self.head = new_node
                    new_node.next = temp
                else:
                    prev.next = new_node
                    new_node.next = current

    def remove(self, player_id):
        """Remove a player node in the list with the given player id.
        Assumes player exists.
        """
        prev = None
        current = self.head

        while current.id != player_id:
            prev = current
            current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def get_score(self, player_id):
        current = self.head

        while current.id != player_id:
            current = current.next

        return current.score

    def get_rank(self, player_id):
        rank = 1
        position = 1  # absolute

        current = self.head
        prev = None

        while current.id != player_id and current.next is not None:
            position += 1

            prev = current
            current = current.next

            if prev.score != current.score:
                rank = position

        if current.id == player_id:
            return rank
        else:
            return None

    def get_max_rank(self):
        """Return the maximum ranking in a populated list."""
        max_rank = 1
        position = 1

        prev = None
        current = self.head

        while current.next is not None:
            position += 1

            prev = current
            current = current.next

            if prev.score != current.score:
                max_rank = position

        return max_rank

    def __str__(self):
        output = "\n"

        current = self.head
        while current is not None:
            output += "[{0}, {1}]---> ".format(current.id, current.score)
            current = current.next
        output += " (END)\n"

        return output
