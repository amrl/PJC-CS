# NOTE: this is a method in the LinkedList class


def Query(self):
    user_word = input("Enter a word: ")

    found = False
    for listnode in self.Node:
        if user_word == listnode.getWord():
            found = True
            occurrences = listnode.getCount()
            print("Number of occurences:", occurrences)

    if not found:
        print("Word not found.")
