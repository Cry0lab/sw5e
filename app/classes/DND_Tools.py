import requests
import Equipment
import Enhanced
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
            return 2
        elif party_level in range(5,9):
            return 3
        elif party_level in range(9,13):
            return 4
        elif party_level in range(13,17):
            return 5
        else:
            return 6
    
    def get_random_choice(self,item_list):
        return random.choice(item_list)

    def get_cr_level(self,cr):
        cr_level = 0
        if cr > 0 and cr <= 4:
            cr_level = 0
        elif cr > 4 and cr <= 10:
            cr_level = 1
        elif cr > 10 and cr <= 16:
            cr_level = 2
        elif cr > 16:
            cr_level = 3
        
        return cr_level

    def get_roll_level(self):
        roll_level = 0
        roll = self.dice_roll(1, 100)
        
        if roll < 31:
            roll_level = 0
        elif roll < 61:
            roll_level = 1
        elif roll < 71:
            roll_level = 2
        elif roll < 96:
            roll_level = 3
        else:
            roll_level = 4

        return roll_level

    def loot_credits_mob(self,cr):
        credits = 0
        
        cr_1_4 = [self.dice_roll(1, 3),self.dice_roll(4, 6),(self.dice_roll(3, 6)*5),((self.dice_roll(3, 6))*10),((self.dice_roll(1, 6))*100)]
        cr_5_10 = [self.dice_roll(9, 6)*10,self.dice_roll(5, 6)*50,self.dice_roll(7, 6)*100,self.dice_roll(4, 6)*100,self.dice_roll(5, 6)*100]
        cr_11_16 = [self.dice_roll(7, 6)*200,self.dice_roll(3, 6)*500,self.dice_roll(3, 6)*1000,self.dice_roll(3, 6)*1000,self.dice_roll(3, 6)*1000]
        cr_17_plus = [self.dice_roll(4, 6)*2000,self.dice_roll(2, 6)*6000,self.dice_roll(2, 6)*7000,self.dice_roll(2, 6)*10000,self.dice_roll(3, 6)*10000]
        cr_table = [cr_1_4,cr_5_10,cr_11_16,cr_17_plus]
        
        
        credit_table = cr_table[self.get_cr_level(cr)]
        #print(credit_table)
        credit_loot = credit_table[self.get_roll_level()]
        return credit_loot

    def loot_item_mob(self,cr,party_level):
        e1 = Enhanced.Enhanced()
        cr_level = self.get_cr_level(cr)
        roll_level = self.get_roll_level()
        artifact_toggle = False
        if roll_level > 1 and cr_level < 3:
            artifact_toggle = True
            #loot = enchanced_item_list_generator(EnhancedItemsData, party_level,True)
            #equipment_printer_random_enhanced(1, 1, loot, "Loot", party_level)
        loot = e1.get_enhanced_loot(party_level,artifact_toggle)
    #def loot_mob(self,cr,party_level):
        

dnd = DND_Tools()
#creds = dnd.loot_credits_mob(4)
#print(creds)
item = dnd.loot_item_mob(4,4)
print(item)