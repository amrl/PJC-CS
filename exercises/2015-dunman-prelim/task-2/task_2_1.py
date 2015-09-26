def generate_final_participants():
    email_registry = dict()  # {email: date, ...}
    duplicate_count = 0

    infile = open("PARTICIPANTS.txt", "r")
    for line in infile:
        date, email = line[:10], line[10:-1]
        if email in email_registry:  # duplicate found
            duplicate_count += 1
        email_registry[email] = date
    infile.close()

    # convert dict to list of tuples [(email, date), ...]
    email_list = list()
    for email in email_registry:
        email_list.append((email, email_registry[email]))

    # sort in alphabetical order
    for i in range(len(email_list)-1):
        for j in range(len(email_list)-1-i):
            if email_list[j][0] > email_list[j+1][0]:
                temp = email_list[j]
                email_list[j] = email_list[j+1]
                email_list[j+1] = temp

    # display email with associated date
    for item in email_list:
        email, date = item
        print("{0},{1}".format(email, date))

    print("\n{0} duplicate entries removed.".format(duplicate_count))
