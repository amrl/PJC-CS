first_hello = True

while True:
    user_input = input("Chatterbox: ")
    words = user_input.split()
    print("Chatterbot: ", end="")

    if "hello" in user_input.lower() and first_hello:
        print("Hi, how are you?\n")
        first_hello = False

    elif "hello" in user_input.lower() and not first_hello:
        print("Hello again, welcome back!\n")

    elif "thanks" in user_input.lower() or "thank you" in user_input.lower():
        print("You are most welcome.\n")

    elif (len(words) >= 3
            and words[0].lower() == "i" and "you" in words[2].lower()):
        verb = words[1]
        print("You", verb, "me? I really", verb, "you too.\n")

    else:
        print("Sorry, I do not understand...\n")
