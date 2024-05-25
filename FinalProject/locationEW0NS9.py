import util
def EW0NS9(info):

    print("You proceed south")
    
    while True:
        command = input("\nWhat do you wish to do?\n")
        command = command.lower()
        if command == "quit":
            util.quitter(info)
        

        if command in {"hint", "help", "help me"}:
            util.hint()
            continue
 
        if command == "info":
                util.playerStats(info)                
        if command in {"open bag", "bag", "search bag"}:
            util.bag()
            continue
        if command[0:3] == "eat":
            util.apples(info)
        if command[0:4] == "look":
            print("You see a fishing boat \nDo you proceed towards it?")
            while True:
                command = input("Yes or No\n")
                command = command.lower()
                if command == "yes":
                    if not "Superpaddle" in info["Inventory"]:
                        print("Your paddle is not strong enough to catch the fishing boat and you are too far for them to see you")
                        break
                if command == "no":
                    break
