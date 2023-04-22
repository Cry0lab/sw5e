import requests

class Equipment:

    def get_all(self):
            # Make a GET request to the API endpoint
        response = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")

        # Get the JSON data from the response
        data = response.json()

        # Create a dictionary to store the equipment by their category
        equipment_by_category = {}

        # Iterate over the equipment and group them by their category
        for equipment in data:
            category = equipment["equipmentCategory"]
            #if the category doesn't exist yet, create it
            if category not in equipment_by_category:
                equipment_by_category[category] = []
            #Add the equipment to its category
            equipment_by_category[category].append(equipment)
        return equipment_by_category

    def get_categories(self):
        categories = []
        data = self.get_all()
        for key in data:
            categories.append(key)
        return categories

    def get_equipment_from_category(self,specific_category):
        equipment = self.get_all()
        specific_equipment = []
        for category, equipment_list in equipment.items():
            if category == specific_category:
                for item in equipment_list:
                    specific_equipment.append(item)
        return specific_equipment    

    def get_all_weapons_of_type(self,weapon_type):
        equipment = self.get_equipment_from_category("Weapon")
        weapons = []
        for item in equipment:
            if item["weaponClassification"] == weapon_type:
                weapons.append(item)
        return weapons
    
    def get_weapon_types(self):
        equipment = self.get_equipment_from_category("Weapon")
        types = []
        for item in equipment:
            if item["weaponClassification"] not in types:
                types.append(item["weaponClassification"])
        return types

    def get_all_armor_of_type(self,armor_type):
        equipment = self.get_equipment_from_category("Armor")
        armor = []
        for item in equipment:
            if item["armorClassification"] == armor_type:
                armor.append(item)
        return armor

    def get_armor_types(self):
        equipment = self.get_equipment_from_category("Armor")
        types = []
        for item in equipment:
            if item["armorClassification"] not in types:
                types.append(item["armorClassification"])
        return types
    """ # Print the equipment lists by category
    for category, equipment_list in equipment_by_category.items():
        print(category)
        #prints - - to match the legnth of the category name
        print("-" * len(category))
        for equipment in equipment_list:
            print(equipment["name"] + " ## " + str(equipment["cost"]))
        print() """

#e1 = Equipment()
#print(e1.get_armor_types())
#print(e1.get_all_armor_of_type("Heavy"))
#print(e1.get_equipment_from_category("Spice")[0]["name"])