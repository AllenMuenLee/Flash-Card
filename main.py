import library, random

cards = library.readcards()


while True:
    command = input("add card(ac) or practice(p) or search(type the vocab directly): ")

    if command == "ac":
        word = input("word: ")
        meaning = input("meaning: ")
        example = input("example: ")
        cards[word] = [meaning, example]
        library.savecards(cards)
        print(cards)
        print("done")
    elif command == "p":
        cards_key = cards.keys()
        cards_key = list(cards_key)
        random.shuffle(cards_key)
        for i in range(len(cards_key)):
            print(("the meaning of " + cards_key[i] + " is?"), end = '')
            input()
            print("the meaning is: " + cards[cards_key[i]][0])
            print("for example: " + cards[cards_key[i]][1])
    else:
        library.searchcard(cards, command)