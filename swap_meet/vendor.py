from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item 

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item 
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        my_item_index = -1
        their_item_index = -1

        for index in range(len(self.inventory)):
            item = self.inventory[index]
            if my_item == item:
                my_item_index = index 

        for index in range(len(other_vendor.inventory)):
            item = other_vendor.inventory[index]
            if their_item == item:
                their_item_index = index

        if my_item_index > -1 and their_item_index > -1:
            other_vendor.inventory.append(self.inventory.pop(my_item_index))
            self.inventory.append(other_vendor.inventory.pop(their_item_index))
            return True

        return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        temp_item = self.inventory[0]
        self.inventory[0] = other_vendor.inventory[0]
        other_vendor.inventory[0] = temp_item
        return True
    
    def get_by_category(self, category):
        items_with_category = []

        for item in self.inventory:
            if item.get_category() == category:
                items_with_category.append(item)

        return items_with_category

    def get_best_by_category(self, category):
        items_with_category = self.get_by_category(category)
        best_condition = -1
        item_to_return = None
        for item in items_with_category:
            if item.condition > best_condition:
                best_condition = item.condition
                item_to_return = item

        return item_to_return
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_category = self.get_best_by_category(my_priority)
        their_best_category = other_vendor.get_best_by_category(their_priority)

        if my_best_category is None or their_best_category is None:
            return False
        
        self.swap_items(other_vendor, my_best_category, their_best_category)
