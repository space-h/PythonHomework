# NS = 0, EW = 1 
def EW0SN9(info):

    if "Superpaddler" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Superpaddler" in info["Inventory"]:
        yesNo = input("You see bigger, better paddle. Do you wish to pick it up?\n")
        if yesNo == "yes":
            if not "Superpaddler" in info["Inventory"]:
                info["Inventory"].append("Superpaddler")
                info["Points"] =  info["Points"] + 5
                print("You have found a better paddle")
                return info
        else:
            return info
        

# NS = 1, EW = 1
def EW1SN1(info):     

    if "Map of ship routes" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Map of ship routes" in info["Inventory"]:
        yesNo = input('A map with a plastic cover floats past you in the water. Do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Map of ship routes" in info["Inventory"]:
                info["Inventory"].append("Map of ship routes")
                info["Points"] =  info["Points"] + 5
                print("With the information provided by the map, you are fairly certain that\n")
                print("if you continue North, you will find eventually find a ship\n")
                return info
        else:
            return info

 # NS = 0, EW = -1                
def EW9SN0(info):     

    if "Rudder" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Rudder" in info["Inventory"]:
        yesNo = input("You see boat rudder, it could be useful, do you wish to pick it up?\n")
        if yesNo == "yes":
            if not "Rudder" in info["Inventory"]:
                info["Inventory"].append("Rudder")
                info["Points"] =  info["Points"] + 5
                return info
        else:
            return info
           
# NS = -1, EW = -1 
def EW9SN9(info):     

    if "Signal Flare" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Signal Flare" in info["Inventory"]:
        yesNo = input('You see a box floating on the sea, it says "Signal flares", it could be useful, do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Signal Flare" in info["Inventory"]:
                info["Inventory"].append("Signal Flare")
                info["Points"] =  info["Points"] + 15
                return info
        else:
            return info

    
# NS = 1, EW = -1 
def EW9SN1(info):     

    if "Lifejacket" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Lifejacket" in info["Inventory"]:
        yesNo = input('You see a lifejacket floating on the sea. Do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Lifejacket" in info["Inventory"]:
                info["Inventory"].append("Lifejacket")
                info["Points"] =  info["Points"] + 10
                return info
        else:
            return info

# NS = -1, EW = 2 
def EW2SN9(info):     

    if "Shortwave radio" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Shortwave radio" in info["Inventory"]:
        yesNo = input('You find a shortwave radio. Do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Shortwave radio" in info["Inventory"]:
                info["Inventory"].append("Shortwave radio")
                info["Points"] =  info["Points"] + 5
                print("The battery seems dead, but otherwise it's alright\n")
                print('To use the radio, input "radio"')
                return info
        else:
            return info

# NS = -1, EW = +1 
def EW1SN9(info):     

    if "Shortwave radio battery" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Shortwave radio battery" in info["Inventory"]:
        yesNo = input('You find a battery for a shortwave radio. Do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Shortwave radio battery" in info["Inventory"]:
                info["Inventory"].append("Shortwave radio battery")
                info["Points"] =  info["Points"] + 5
                print("The battery seems intact\n")
                return info
        else:
            return info

# NS = -2, EW = +2 
def EW2SN8(info):     

    if "Whistle" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Whistle" in info["Inventory"]:
        yesNo = input('A plastic Whistle floats past you in the water. Do you wish to pick it up?\n')
        if yesNo == "yes":
            if not "Whistle" in info["Inventory"]:
                info["Inventory"].append("Whistle")
                info["Points"] =  info["Points"] + 5
                print("Seems to be working\n")
                return info
        else:
            return info

def EW2SN2(info):     

    if "A DVD box of Monty Python" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "A DVD box of Monty Python" in info["Inventory"]:
        yesNo = input('You see a DVD box of Monty Python, do you pick it up?\n')
        if yesNo == "yes":
            if not "A DVD box of Monty Python" in info["Inventory"]:
                info["Inventory"].append("A DVD box of Monty Python")
                info["Points"] =  info["Points"] + 10
                print("It might not be the most useful thing around here, but at least you have it")
                return info
        else:
            return info

def EW0SN1(info):     

    if "A box of black licorice. " in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Swiss army knife" in info["Inventory"]:
        yesNo = input('You see a box of black licorice, do you pick it up?\n')
        if yesNo == "yes":
            if not "A box of black licorice" in info["Inventory"]:
                info["Inventory"].append("A box of black licorice")
                info["Points"] =  info["Points"] + 5
                return info
        else:
            return info
        
def EW8SN0(info):     

    if "Jellyfish. " in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Jellyfish" in info["Inventory"]:
        yesNo = input('A jellyfish floats on the sea. Do you pick it up?\n')
        if yesNo == "yes":
            if not "Jellyfish" in info["Inventory"]:
                info["Inventory"].append("Jellyfish")
                info["Health"] =  info["Health"]  - 10
                if info["Health"] < 1:
                    print("Your health has reached 0, the game is over")
                    return info  
                print("You have lost 10HP, but now you have a jellyfish, you weirdo")
                
                return info
        else:
            return info


def EW0SN1(info):     

    if "Swiss army knife" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Swiss army knife" in info["Inventory"]:
        yesNo = input('You spot a swiss army knife, with a wooded cover in the water\n')
        if yesNo == "yes":
            if not "Swiss army knife" in info["Inventory"]:
                info["Inventory"].append("Swiss army knife")
                info["Points"] =  info["Points"] + 5
                return info
        else:
            return info
        
def EW8SN1(info):     

    if "A captain's hat" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "A captain's hat" in info["Inventory"]:
        print("A captain's hat float past you, a little wet but otherwise intact.\n")
        yesNo = input("Do you put it on?")
        if yesNo == "yes":
            if not "A captain's hat" in info["Inventory"]:
                info["Inventory"].append("A captain's hat")
                info["Points"] =  info["Points"] + 15
                info["Name"] = "Captain " + info["Name"]
                return info
        else:
            return info

def nothingButSea(info):

    print("You see nothing but more ocean here")
    return info





           
    
    
            
    
    
