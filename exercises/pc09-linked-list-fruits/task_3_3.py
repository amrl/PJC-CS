from task_3_2 import LinkedList


def main():
    testlist = LinkedList()
    testlist.Initialise()

    while True:
        print("\n1. Add an item")
        print("2. Traverse the linked list of used nodes and output the data"
              " values")
        print("3. Output all pointers and data values")
        print("4. Traverse the linked list of used nodes and output the data"
              " values in reverse order")
        print("5. Exit")

        option = input("\nEnter option number: ")
        print()

        if option == '1':
            if testlist.IsFull():
                print("- Error. List is full. -")
            else:
                new_data = input("Enter item to add: ")
                testlist.AddNode(new_data)

        elif option == '2':
            testlist.Traversal()

        elif option == '3':
            testlist.DisplayLinkedList()

        elif option == '4':
            testlist.ReverseTraversal()

        elif option == '5':
            break

        else:
            print("* Invalid option. Try again. *")

main()
