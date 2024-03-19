import json
import requests
import random

#Shop Types
#Weapon
	#All Shops
		#Simple Blaster
		#Simple Vibroweapon
	#Some Shops
		#Martial Blaster
		#Martial Vibroweapon
		#Explosive
	#All Shops, but Random
		#Ammunition
		#Enhanced Items
			#Blaster Modification
			#Vibroweapon Modification
			#Consumables
				#Ammunition
				#Explosive
			#Weapon				
#Armor and Clothing
	#All shops
		#Armor
	#Some Shops
		#Weapon Armor or Accessory
		#Clothing
	#All Shops, but Random
		#Enchanced Items
			#Consumables
				#Barrier
			#Armor
			#Armor Modification
			#Clothing Modification
			#Shield
			#Adventuring Gear with a Category
#Tech Shop
	#All Shops
		#Gear
			#Communications
			#Data Recording and Storage
				#No Holocron
			#Kit
			#Tool
			#Utility
	#All Shops, but Random
		#Enchanced Items
			#Consumables
				#Technology
				#Barrier
			#Armor Modification
			#Vibroweapon Modification
			#Blaster Modification
			#Wristpad Modification
			#Clothing Modification
			#Item Modification
			#Shield
			#Adventuring Gear with no Category
			#Focus
				#Tech
			#Droid Customization
#Cantina
	#Alcholic Beverage
	#Gaming Set
	#Musical instrument
	#Spice
	#Storage
	#Enchanced Items
		#Consumables
			#Adrenal
			#Stimpack
#Medical
	#All Shops
		#Gear
			#Medical
	#All Shops, but Random
		#Consumables
			#Medpac
			#Stimpac
			#Adrenal
#Black Market
	#Depending on the dealer, make this like another shop, but inflated prices with better odds of good shit.
	#Enhanced Items
		#Consumables
			#Substance
#Jedi
	#All Shops
		#Simple Lightweapon
	#All Shops, but Random
		#Martial Lightweapon
	#All Shops, but Random
		#Enhanced Items
			#Focus
				#Force
				#Focus
			#Focus Generator
			#Lightweapon Modification		
#Shipyard
	#Gear
		#Life Support
		#Storage
		#Utility
		#Tool
		#Spice - Random
	#Ship Armor
	#Ship Shield
	#Ship Weapon

count =0
equipment = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
equipmentData = equipment.json()
#print(equipmentData)

EnhancedItems = requests.get("https://sw5eapi.azurewebsites.net/api/enhancedItem")
EnhancedItemsData = EnhancedItems.json()

StarshipEquipment = requests.get("https://sw5eapi.azurewebsites.net/api/starshipEquipment")
StarshipEquipmentData = StarshipEquipment.json()

StarshipMods = requests.get("https://sw5eapi.azurewebsites.net/api/starshipModification")
StarshipModData = StarshipMods.json()

#Equipment Items
Ammunition = {}
Explosive = {}
Utility = {}
Storage = {}
Communications = {}
DataRecordingAndStorage = {}
LifeSupport = {}
Medical = {}
WeaponOrArmorAccessory = {}
Tool = {}
GamingSet = {}
MusicalInstrument = {}
Clothing = {}
Kit = {}
AlcoholicBeverage = {}
Spice = {}
SimpleBlaster = {}
MartialBlaster = {}
SimpleVibroweapon = {}
MartialVibroweapon = {}
SimpleLightweapon = {}
MartialLightweapon = {}
LightArmor = {}
MediumArmor = {}
HeavyArmor = {}
Shield = {}

#Enchanced Items
AdventuringGear = {}
AdventuringGearNoCategory = {}
EnhancedArmor = {}
Adrenal = {}
substance = {}
EnhancedAmmunition = {}
barrier = {}
EnhancedExplosive = {}
medpac = {}
poison = {}
stimpac = {}
technology = {}
DroidCustomization = {}
Focus = {}
ItemModification = {}
EnhancedShield = {}
EnhancedWeapon = {}
ShipArmor = {}
ShipShield = {}
ShipWeapon = {}
BlasterModification = {}
ClothingModification = {}
WristpadModification = {}
ArmorModification = {}
VibroweaponModification = {}
LightweaponModification = {}
FocusGeneratorModification = {}

#Parse Equipment into Dictionaries
for item in equipmentData:
    if item["equipmentCategoryEnum"] == 1:
        Ammunition[len(Ammunition)] = item
    elif item["equipmentCategoryEnum"] == 2:
        Explosive[len(Explosive)] = item
    elif item["equipmentCategoryEnum"] == 5:
        Storage[len(Storage)] = item
    elif item["equipmentCategoryEnum"] == 7:
        Communications[len(Communications)] = item
    elif item["equipmentCategoryEnum"] == 8:
        DataRecordingAndStorage[len(DataRecordingAndStorage)] = item
    elif item["equipmentCategoryEnum"] == 9:
        LifeSupport[len(LifeSupport)] = item
    elif item["equipmentCategoryEnum"] == 10:
        Medical[len(Medical)] = item
    elif item["equipmentCategoryEnum"] == 11:
        WeaponOrArmorAccessory[len(WeaponOrArmorAccessory)] = item
    elif item["equipmentCategoryEnum"] == 12:
        Tool[len(Tool)] = item
    elif item["equipmentCategoryEnum"] == 16:
        Utility[len(Utility)] = item
    elif item["equipmentCategoryEnum"] == 17:
        GamingSet[len(GamingSet)] = item
    elif item["equipmentCategoryEnum"] == 18:
        MusicalInstrument[len(MusicalInstrument)] = item
    elif item["equipmentCategoryEnum"] == 20:
        Clothing[len(Clothing)] = item
    elif item["equipmentCategoryEnum"] == 21:
        Kit[len(Kit)] = item
    elif item["equipmentCategoryEnum"] == 22:
        AlcoholicBeverage[len(AlcoholicBeverage)] = item
    elif item["equipmentCategoryEnum"] == 23:
        Spice[len(Spice)] = item
    elif item["weaponClassificationEnum"] == 1:
        SimpleBlaster[len(SimpleBlaster)] = item
    elif item["weaponClassificationEnum"] == 2:
        MartialBlaster[len(MartialBlaster)] = item
    elif item["weaponClassificationEnum"] == 3:
        SimpleVibroweapon[len(SimpleVibroweapon)] = item
    elif item["weaponClassificationEnum"] == 4:
        MartialVibroweapon[len(MartialVibroweapon)] = item
    elif item["weaponClassificationEnum"] == 5:
        SimpleLightweapon[len(SimpleLightweapon)] = item
    elif item["weaponClassificationEnum"] == 6:
        MartialLightweapon[len(MartialLightweapon)] = item
    elif item["armorClassificationEnum"] == 1:
        LightArmor[len(LightArmor)] = item
    elif item["armorClassificationEnum"] == 2:
        MediumArmor[len(MediumArmor)] = item
    elif item["armorClassificationEnum"] == 3:
        HeavyArmor[len(HeavyArmor)] = item
    elif item["armorClassificationEnum"] == 4:
        Shield[len(Shield)] = item
#Parse Enchanced Items into Dictionaries
for item in EnhancedItemsData:
    if item["typeEnum"] == 1:
        if item["subtype"] == "":
            AdventuringGearNoCategory[len(AdventuringGearNoCategory)] = item
        else:
            AdventuringGear[len(AdventuringGear)] = item
    elif item["typeEnum"] == 2:
        EnhancedArmor[len(EnhancedArmor)] = item  
    elif item["subtype"] == "adrenal":
        Adrenal[len(Adrenal)] = item
    elif item["subtype"] == "substance":
        substance[len(substance)] = item
    elif item["subtype"] == "ammunition":
        EnhancedAmmunition[len(EnhancedAmmunition)] = item
    elif item["subtype"] == "explosive":
        EnhancedExplosive[len(EnhancedExplosive)] = item
    elif item["subtype"] == "medpac":
        medpac[len(medpac)] = item
    elif item["subtype"] == "poison":
        poison[len(poison)] = item
    elif item["subtype"] == "stimpac":
        stimpac[len(stimpac)] = item
    elif item["subtype"] == "barrier":
        barrier[len(barrier)] = item
    elif item["subtype"] == "technology":
        technology[len(technology)] = item
    elif item["typeEnum"] == 5:
        DroidCustomization[len(DroidCustomization)] = item 
    elif item["typeEnum"] == 6:
        Focus[len(Focus)] = item 
    elif item["typeEnum"] == 8:
        EnhancedShield[len(EnhancedShield)] = item 
    elif item["typeEnum"] == 9:
        EnhancedWeapon[len(EnhancedWeapon)] = item 
    elif item["typeEnum"] == 11:
        ShipArmor[len(ShipArmor)] = item 
    elif item["typeEnum"] == 12:
        ShipShield[len(ShipShield)] = item 
    elif item["typeEnum"] == 13:
        ShipWeapon[len(ShipWeapon)] = item 
    elif item["subtype"] == "blaster":
        BlasterModification[len(BlasterModification)] = item 
    elif item["subtype"] == "clothing":
        ClothingModification[len(ClothingModification)] = item 
    elif item["subtype"] == "wristpad":
        WristpadModification[len(WristpadModification)] = item 
    elif item["subtype"] == "armor":
        ArmorModification[len(ArmorModification)] = item 
    elif item["subtype"] == "vibroweapon":
        VibroweaponModification[len(VibroweaponModification)] = item 
    elif item["subtype"] == "lightweapon":
        LightweaponModification[len(LightweaponModification)] = item 
    elif item["subtype"] == "focus generator":
        FocusGeneratorModification[len(FocusGeneratorModification)] = item
    elif item["typeEnum"] == 7:
        ItemModification[len(ItemModification)] = item 

def dice_roll(number,dice):
    total = 0
    while number > 0:
        number = number - 1
        roll = random.randint(1, dice)
        total = total + roll
        #print(roll)
    return total

def define_rarity_level(party_level):
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

def get_random_choice(item_list):
        return random.choice(item_list)

def equipment_printer_random(shop_size,multiplier,items,title):
    count = shop_size * multiplier
    print()
    print(title)
    print("Item,Cost")
    while count > 0:
        format_equipment(get_random_choice(items))
        count -= 1

def equipment_print_all(list,title):
    print()
    print()
    print(title)
    print("Item,Cost")
    for item in list:
        format_equipment(list[item])
def starship_equipment_print_all():
    print("Starship Equipment")
    for item in StarshipEquipmentData:
        print(str(item["name"]) + "," + str(item["cost"]) + "," + str(item["type"]))

def format_equipment(item):
    print(str(item["name"].replace(',','')) + " | " + str(item["cost"]))

def format_enchanced_item(item):
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



    print(str(item["name"]).replace(',','') + " | " + item["type"] + " | " + item["searchableRarity"] + " | " + str(cost))

def format_enchanced_item_black_market(item):
    cost = 0

    roll1 = random.randint(1,100)
    roll2 = random.randint(1,100)
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



    print(str(item["name"]).replace(',','') + " | " + item["type"] + " | " + item["searchableRarity"] + " | " + str(cost))
def enchanced_item_list_generator(item_list,party_level,artifact_toggle):
    rarity = define_rarity_level(party_level)
    d20 = dice_roll(1,20)
    if rarity == 5:
        if (d20 > 10 and artifact_toggle == False):
            rarity = rarity + 2
        else:
            rarity = rarity + 1
    else:
        rarity = rarity + 2
    new_list = {}
    standard = {}
    premium = {}
    prototype = {}
    advanced = {}
    legendary = {}
    artifact = {}
    count = len(item_list)-1
    while count > 0:
        count -= 1
        if  1 in ((item_list[count]["rarityOptionsEnum"])):
            standard[len(standard)] = item_list[count]
        elif 2 in ((item_list[count]["rarityOptionsEnum"])):
            premium[len(premium)] = item_list[count]
        elif 3 in ((item_list[count]["rarityOptionsEnum"])):
            prototype[len(prototype)] = item_list[count]
        elif 4 in ((item_list[count]["rarityOptionsEnum"])):
            advanced[len(advanced)] = item_list[count]
        elif 5 in ((item_list[count]["rarityOptionsEnum"])):
            legendary[len(legendary)] = item_list[count]
        elif 6 in ((item_list[count]["rarityOptionsEnum"])):
            artifact[len(artifact)] = item_list[count]
    count = len(item_list)-1
    while count >= 0:
        item_rarity = item_list[count]["rarityOptionsEnum"]
        if any (x in item_rarity for x in range(rarity)):
            new_list[len(new_list)] = item_list[count]
        count -= 1
    return new_list

def equipment_printer_random_enhanced(shop_size,multiplier,items,title,party_level):
    rarity = define_rarity_level(party_level)
    count = shop_size * multiplier
    print()
    print(title)
    print("Item,Type,Rarity,Cost")
    while count > 0:
        item = get_random_choice(items)
        if not(6 in (item["rarityOptionsEnum"])):
            format_enchanced_item(get_random_choice(items))
        count -= 1
    artifact = {}
    count = len(items)-1
    if rarity == 5:
        while count > 0:
            count -= 1
            if 6 in ((items[count]["rarityOptionsEnum"])):
                artifact[len(artifact)] = items[count]
        if len(artifact)>0:
            format_enchanced_item(get_random_choice(artifact))

def equipment_printer_random_enhanced_black_market(shop_size,multiplier,items,title,party_level):
    rarity = define_rarity_level(party_level)
    count = shop_size * multiplier
    print()
    print(title)
    print("Item,Type,Rarity,Cost")
    while count > 0:
        item = get_random_choice(items)
        if not(6 in (item["rarityOptionsEnum"])):
            format_enchanced_item_black_market(get_random_choice(items))
        count -= 1
    artifact = {}
    count = len(items)-1
    if rarity == 5:
        while count > 0:
            count -= 1
            if 6 in ((items[count]["rarityOptionsEnum"])):
                artifact[len(artifact)] = items[count]
        if len(artifact)>0:
            format_enchanced_item_black_market(get_random_choice(artifact))
            
def shop_list_generator(shop_size,multiplier,item_list,title,party_level,artifact_toggle):
    items = enchanced_item_list_generator(item_list, party_level, artifact_toggle)
    equipment_printer_random_enhanced(shop_size, multiplier, items, title, party_level)


#Shop Generators

def create_Weapon_Shop(shop_size,party_level):
    print("Weapon Shop")
    equipment_print_all(SimpleBlaster,"Simple Blasters")
    equipment_print_all(SimpleVibroweapon, "Simple Vibroweapons")
    if shop_size > 1:
        equipment_printer_random(shop_size, 3, MartialBlaster,"Martial Blasters")
        equipment_printer_random(shop_size, 3, MartialVibroweapon, "Martial Vibroweapons")
    equipment_printer_random(shop_size, 2, Explosive, "Explosives")
    equipment_printer_random(shop_size, 2, Ammunition, "Ammunition")
    blaster_mods = enchanced_item_list_generator(BlasterModification,party_level,False)
    equipment_printer_random_enhanced(shop_size, 3, blaster_mods, "Blaster Mods", party_level)
    vibro_mods = enchanced_item_list_generator(VibroweaponModification,party_level,False)
    equipment_printer_random_enhanced(shop_size, 3, vibro_mods, "Vibroweapon Mods", party_level)
    ammo = enchanced_item_list_generator(EnhancedAmmunition,party_level,False)
    equipment_printer_random_enhanced(shop_size, 3, ammo, "Enhanced Ammunition", party_level)
    boom = enchanced_item_list_generator(EnhancedAmmunition,party_level,False)
    equipment_printer_random_enhanced(shop_size, 3, boom, "Enhanced Explosives", party_level)

def create_Armor_Shop(shop_size,party_level):
    print("Armor Shop")
    equipment_print_all(LightArmor, "Light Armor")
    if shop_size > 1:
        equipment_print_all(MediumArmor, "Medium Armor")
    if shop_size > 2:
        equipment_print_all(HeavyArmor, "Heavy Armor")
    if shop_size > 1:
        equipment_printer_random(shop_size, 2, WeaponOrArmorAccessory, "Weapon and Armor Accessories")
        equipment_printer_random(shop_size, 2, Clothing, "Clothing")
    equipment_printer_random(shop_size, 2, Shield, "Shields")
    armor_plus = enchanced_item_list_generator(EnhancedArmor, party_level,False)
    equipment_printer_random_enhanced(shop_size, 1, armor_plus, "Enhanced Armor", party_level)
    armor_mods = enchanced_item_list_generator(ArmorModification, party_level,False)
    equipment_printer_random_enhanced(shop_size, 2, armor_mods, "Armor Mods", party_level)
    cloth_mods = enchanced_item_list_generator(ClothingModification, party_level,False)
    equipment_printer_random_enhanced(shop_size, 1, cloth_mods, "Clothing Mods", party_level)
    barrier_shop = enchanced_item_list_generator(barrier, party_level,False)
    equipment_printer_random_enhanced(shop_size, 1, barrier_shop, "Barriers", party_level)
    shields = enchanced_item_list_generator(EnhancedShield, party_level,False)
    equipment_printer_random_enhanced(shop_size, 2, shields, "Enhanced Shields", party_level)
    Adventure = enchanced_item_list_generator(AdventuringGear, party_level,False)
    equipment_printer_random_enhanced(shop_size, 3, Adventure, "Enhanced Gear", party_level)

def create_Medical_Shop(shop_size,multiplier,party_level,artifact_toggle):
    print("Medical Supplies")
    equipment_print_all(Medical, "Basic Medical Supplies")
    equipment_print_all(LifeSupport, "Life Support Supplies")
    shop_list_generator(shop_size, multiplier, medpac, "Enhanced Medpacs", party_level, artifact_toggle)

def create_Tech_Shop(shop_size,multiplier,party_level,artifact_toggle):
    print("Tech Shop")
    equipment_print_all(Communications, "Communications")
    equipment_print_all(DataRecordingAndStorage, "Data Recording and Storage")
    equipment_print_all(Kit, "Kit")
    equipment_print_all(Tool, "Tools")
    equipment_print_all(Utility, "Utility")
    shop_list_generator(shop_size, multiplier, ArmorModification, "Armor Mods", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, VibroweaponModification, "Vibroweapon Mods", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, BlasterModification, "Blaster Mods", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, WristpadModification, "Wristpad Mods", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, EnhancedShield, "Enhanced Shields", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, DroidCustomization, "Droid Customizations", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, technology, "Misc Tech", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier, barrier, "Barriers", party_level, artifact_toggle)
    if (dice_roll(1, 20)>10):
        shop_list_generator(shop_size, (multiplier/2), LightweaponModification, "Lightweapon Mods", party_level, artifact_toggle)

def create_Cantina(shop_size,multiplier,party_level,artifact_toggle):
    print("Cantina")
    equipment_print_all(AlcoholicBeverage, "Alcoholic Beverages")
    equipment_print_all(GamingSet, "Gaming Sets")
    equipment_print_all(MusicalInstrument, "Musical Instruments")
    equipment_print_all(Storage, "Storage")
    shop_list_generator(shop_size, multiplier, Adrenal, "Adrenals", party_level, artifact_toggle)
    shop_list_generator(shop_size, multiplier/3, stimpac, "Stimpacs", party_level, artifact_toggle)

def create_Black_Market_Dealer(shop_size,multiplier,party_level,artifact_toggle):
    items = enchanced_item_list_generator(EnhancedItemsData, party_level, artifact_toggle)
    equipment_printer_random_enhanced_black_market(shop_size, multiplier,items, "Black Market", party_level)
    

def loot_individual(cr,party_level):
    roll = dice_roll(1, 100)
    roll_level = 0
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
    
    
    

    cr_level = 0
    if cr > 0 and cr <= 4:
        cr_level = 0
    elif cr > 4 and cr <= 10:
        cr_level = 1
    elif cr > 10 and cr <= 16:
        cr_level = 2
    elif cr > 16:
        cr_level = 3
    

    cr_1_4 = [dice_roll(1, 3),dice_roll(4, 6),(dice_roll(3, 6)*5),((dice_roll(3, 6))*10),((dice_roll(1, 6))*100)]
    cr_5_10 = [dice_roll(9, 6)*10,dice_roll(5, 6)*50,dice_roll(7, 6)*100,dice_roll(4, 6)*100,dice_roll(5, 6)*100]
    cr_11_16 = [dice_roll(7, 6)*200,dice_roll(3, 6)*500,dice_roll(3, 6)*1000,dice_roll(3, 6)*1000,dice_roll(3, 6)*1000]
    cr_17_plus = [dice_roll(4, 6)*2000,dice_roll(2, 6)*6000,dice_roll(2, 6)*7000,dice_roll(2, 6)*10000,dice_roll(3, 6)*10000]
    cr_table = [cr_1_4,cr_5_10,cr_11_16,cr_17_plus]

    credit_table = cr_table[cr_level]
    credit_loot = credit_table[roll_level]
    print(str(credit_loot) + " Credits")
    if roll_level > 1 and cr_level < 3:
        loot = enchanced_item_list_generator(EnhancedItemsData, party_level,True)
        equipment_printer_random_enhanced(1, 1, loot, "Loot", party_level)
    elif roll_level > 1 and cr_level == 3:
        loot = enchanced_item_list_generator(EnhancedItemsData, party_level,False)
        equipment_printer_random_enhanced(1, 1, loot, "Loot", party_level)
    
def loot_chest(cr,party_level):
    roll = dice_roll(1, 100)
    print("You rolled a " + str(roll))
    roll_level = 0
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
    
    
    

    cr_level = 0
    if cr > 0 and cr <= 4:
        cr_level = 0
    elif cr > 4 and cr <= 10:
        cr_level = 1
    elif cr > 10 and cr <= 16:
        cr_level = 2
    elif cr > 16:
        cr_level = 3
    

    cr_1_4 = [dice_roll(2, 6)*100,dice_roll(2, 6)*500,dice_roll(2, 6)*500,dice_roll(2, 6)*500,dice_roll(2, 6)*500]
    cr_5_10 = [dice_roll(2, 6)*500,dice_roll(2, 6)*1000,dice_roll(2, 6)*1000,dice_roll(2, 6)*1000,dice_roll(2, 6)*1000]
    cr_11_16 = [dice_roll(2, 6)*1000,dice_roll(2, 6)*2000,dice_roll(3, 6)*2000,dice_roll(4, 6)*2000,dice_roll(5, 6)*2000]
    cr_17_plus = [dice_roll(9, 6)*2000,dice_roll(4, 6)*5000,dice_roll(4, 6)*5000,dice_roll(4, 6)*10000,dice_roll(5, 6)*10000]
    cr_table = [cr_1_4,cr_5_10,cr_11_16,cr_17_plus]

    multiplier = roll_level + 1
    credit_table = cr_table[cr_level]
    credit_loot = credit_table[roll_level]
    print(str(credit_loot) + " Credits")
    if cr_level < 3:
        loot = enchanced_item_list_generator(EnhancedItemsData, party_level,True)
        equipment_printer_random_enhanced(1, multiplier, loot, "Loot", party_level)
    elif cr_level == 3:
        loot = enchanced_item_list_generator(EnhancedItemsData, party_level,False)
        equipment_printer_random_enhanced(1, multiplier, loot, "Loot", party_level)
    print(str(random.randint(0,cr_level+1)) + " Medpacs")
    print(str(random.randint(0,cr_level+1)) + " Repair Kits")

shop_size = 3
multiplier = 3
party_level = 7
artifact_toggle = False

#create_Black_Market_Dealer(shop_size, multiplier, party_level, artifact_toggle)

#create_Weapon_Shop(shop_size,party_level)
#create_Armor_Shop(shop_size, party_level)
#create_Medical_Shop(3, 2, 5, False)
#create_Tech_Shop(1, 2, 5, False)
#create_Cantina(shop_size, multiplier, party_level, False)

#i = 2
#while i > 0:
#    loot_individual(14, party_level)
#    i -= 1

#Light = enchanced_item_list_generator(LightweaponModification, 4, False)
#equipment_printer_random_enhanced(1, 1, Light, "Loot", 4)
#print(ShipArmor)
loot_chest(7, party_level)

