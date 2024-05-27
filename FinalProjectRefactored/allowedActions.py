import time
import sys

def apples(info):
    if "Bag of apples" in info["Inventory"]:
        if info["Health"] <= 94:
            info["Health"] = info["Health"] + 5
            if info["Points"] <=20:
                info["Points"] += 2
            print("\nYou are healed")
            time.sleep(1)
            print(f'HP: {info["Health"]} / 100')
            return info
        elif info["Health"] == 100:
            print("\nYou are fully healed")
            print(info["Health"], "/ 100")
            time.sleep(1)
            return info
        
        elif info["Health"] >= 95:
            info["Health"] = 100
            if info["Points"] <=20:
                info["Points"] += 2
            print("\nYou are healed")
            time.sleep(1)
            print(info["Health"], "/ 100")
            return info

        if info["Health"] == 100:
            print("\nYou are fully healed")        
            return info
    else:
        print("You have nothing to eat, maybe there are something in the bag")
        return info
