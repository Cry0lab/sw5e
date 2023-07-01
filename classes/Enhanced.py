import requests

class Enchanced:


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

    def get_enchanced_from_type(self,specific_type):
        enchanced = self.get_all()
        specific_enchanced = []
        for type, enchanced_list in enchanced.items():
            if type == specific_type:
                for item in enchanced_list:
                    specific_enchanced.append(item)
        return specific_enchanced 

    def get_enchanced_of_rarity(self,rarity,enhanced_list):
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

    def get_enchanced_of_rarity_or_less(self,rarity,enhanced_list):
        rarities = ["Blank", "Standard", "Premium", "Prototype", "Advanced", "Legendary", "Artifact"]
        rarity_value = rarities.index(rarity)
        specific_enhanced = []
        #print(rarity_value)
        for item in enhanced_list:
            #print(item["rarityOptionsEnum"])
            if item["rarityOptionsEnum"][0] <= rarity_value:
                print(item["rarityOptionsEnum"])
                specific_enhanced.append(item)
        return specific_enhanced

e1 = Enchanced()
#print(e1.get_types())
weapons = e1.get_enchanced_from_type("Weapon")
#print(weapons)
premium_weapons = e1.get_enchanced_of_rarity_or_less("Premium", weapons)