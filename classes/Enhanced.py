import requests
import Equipment
import random

class Enhanced:

    def get_all(self):
            # Make a GET request to the API endpoint
        response = requests.get("https://sw5eapi.azurewebsites.net/api/enhancedItem")

        # Get the JSON data from the response
        data = response.json()

        # Create a dictionary to store the enhanced item by their type
        enhanced_by_type = {}

        # Iterate over the enhanced and group them by their type
        for enhanced in data:
            type = enhanced["type"]
            #if the type doesn't exist yet, create it
            if type not in enhanced_by_type:
                enhanced_by_type[type] = []
            #Add the enhanced to its type
            enhanced_by_type[type].append(enhanced)
        return enhanced_by_type

    def get_types(self):
        types = []
        data = self.get_all()
        for key in data:
            types.append(key)
        return types

    def get_random_choice(self,item_list):
        return random.choice(item_list)

    def get_enhanced_from_type(self,specific_type):
        enhanced = self.get_all()
        specific_enhanced = []
        for type, enhanced_list in enhanced.items():
            if type == specific_type:
                for item in enhanced_list:
                    specific_enhanced.append(item)
        return specific_enhanced 

    def get_enhanced_of_rarity(self,rarity,enhanced_list):
        rarities = ["Blank", "Standard", "Premium", "Prototype", "Advanced", "Legendary", "Artifact"]
        rarity_value = rarities.index(rarity)
        specific_enhanced = []
        #print(rarity_value)
        for item in enhanced_list:
            #print(item["rarityOptionsEnum"])
            if item["rarityOptionsEnum"][0] == rarity_value:
                #print(item["rarityOptionsEnum"])
                specific_enhanced.append(item)
        return specific_enhanced

    def get_enhanced_of_rarity_or_less(self,rarity,enhanced_list):
        rarities = ["Blank", "Standard", "Premium", "Prototype", "Advanced", "Legendary", "Artifact"]
        rarity_value = rarities.index(rarity)
        #print(rarity_value)
        specific_enhanced = []
        #print(rarity_value)
        for item in enhanced_list:
            #print(item["rarityOptionsEnum"][0])
            if item["rarityOptionsEnum"][0] <= rarity_value:
                #print(item["rarityOptionsEnum"])
                specific_enhanced.append(item)
        return specific_enhanced

    def get_rarity_level(self,party_level):
        if party_level in range(1,5):
            return "Standard"
        elif party_level in range(5,9):
            return "Premium"
        elif party_level in range(9,13):
            return "Prototype"
        elif party_level in range(13,17):
            return "Advanced"
        else:
            return "Legendary"
    
    def get_enhanced_cost(self,item):
        cost = 0

        roll1 = random.randint(1,100)
        roll2 = random.randint(1,100)
        if roll1 > roll2:
            roll = roll1
        else:
            roll = roll2

        if item["searchableRarity"] == "Standard":
            cost = roll * 10
        elif item["searchableRarity"] == "Premium":
            cost = roll * 50
        elif item["searchableRarity"] == "Prototype":
            cost = roll * 250
        elif item["searchableRarity"] == "Advanced":
            cost = roll * 1000
        elif item["searchableRarity"] == "Legendary":
            cost = roll * 5000
        elif item["searchableRarity"] == "Artifact":
            cost = roll * 25000
        return cost
    
    def get_black_market_enhanced_cost(self,item):
        cost = 0

        roll1 = DND.dice_roll(1,100)
        roll2 = DND.dice_roll(1,100)
        if roll1 > roll2:
            roll = roll1
        else:
            roll = roll2

        if item["searchableRarity"] == "Standard":
            cost = roll * 15
        elif item["searchableRarity"] == "Premium":
            cost = roll * 60
        elif item["searchableRarity"] == "Prototype":
            cost = roll * 300
        elif item["searchableRarity"] == "Advanced":
            cost = roll * 1200
        elif item["searchableRarity"] == "Legendary":
            cost = roll * 7000
        elif item["searchableRarity"] == "Artifact":
            cost = roll * 30000
        return cost

    def format_enhanced_item(self,item,black_market_toggle):
        if black_market_toggle == True:
            cost = self.get_black_market_enhanced_cost(item)
        else:
            cost = self.get_enhanced_cost(item)
        formatted_item = str(item["name"]).replace(',','') + "," + item["type"] + "," + item["searchableRarity"] + "," + str(cost)
        return formatted_item

    def format_random_enhanced_item(self,item_list,black_market_toggle):
        item = self.get_random_choice(item_list)
        formatted = self.format_enhanced_item(item,black_market_toggle)
        return formatted

    def get_enhanced_loot(self,party_level,artifact_toggle):
        rarity = self.get_rarity_level(party_level)
        d20 = random.randint(1,20)
        if rarity == "Legendary":
            if (d20 > 10 and artifact_toggle == True):
                rarity = "Artifact"
        item_list = self.get_enhanced_of_rarity_or_less(rarity,self.get_all())





e1 = Enhanced()
#print(e1.get_types())
weapons = e1.get_enhanced_from_type("Weapon")
#print(weapons)
premium_weapons = e1.get_enhanced_of_rarity_or_less("Artifact", weapons)
#print(premium_weapons[1]["searchableRarity"])
#cost = e1.get_enhanced_cost(premium_weapons[1])
#print(e1.format_random_enhanced_item(premium_weapons,False))