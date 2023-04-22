import random

class DND_Tools:

    def dice_roll(self,number,dice):
        total = 0
        while number > 0:
            number = number - 1
            roll = random.randint(1, dice)
            total = total + roll
            #print(roll)
        return total

    def define_rarity_level(self,party_level):
        if party_level in range(1,5):
            return 1
        elif party_level in range(5,9):
            return 2
        elif party_level in range(9,13):
            return 3
        elif party_level in range(13,17):
            return 4
        else:
            return 5
    
    def get_random_choice(self,item_list):
        return random.choice(item_list)