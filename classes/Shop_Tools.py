import Equipment
import Enhanced
import DND_Tools

class Shop_Tools:
    equipment_list = Equipment.Equipment()
    DND = DND_Tools.DND_Tools()
    #print(DND.get_random_choice(equipment_list.get_equipment_from_category("Kit")))

    def format_equipment(self,item):
        item = str(item["name"]) + "     " + str(item["cost"])
        return item
    
    def equipment_print_all(self,category):
        print(category)
        print("-" * len(category))
        print()
        print("Item     Cost")
        print("--------------")
        print()
        items = equipment_list.get_equipment_from_category(category)
        #print(items)
        for item in items:
            print(self.format_equipment(item))

Shop = Shop_Tools()
equipment_list = Equipment.Equipment()
DND = DND_Tools.DND_Tools()
item = DND.get_random_choice(equipment_list.get_equipment_from_category("Kit"))
print(Shop.format_equipment(item))
Shop.equipment_print_all("Kit")   