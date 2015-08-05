while True:
    print("1. Add an item")
    print("2. Traverse the linked list of used nodes and output the data"
          " values")
    print("3. Output all pointers and data values")
    print("5. Exit")

    option = input("Enter option number: ")

    if option == '1':
        new_data = input("Enter item to add: ")
        testlist.AddNode(new_data)
    elif option == '2':
        testlist.Traversal()
    elif option == '3':
        testlist.DisplayLinkedList()
    elif option == '5':
        break
    else:
        print("* Invalid option. Try again. *")
