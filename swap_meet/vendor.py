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
        if (my_item not in self.inventory) or (their_item not in other_vendor.inventory):
            return False
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
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
        my_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other_vendor.get_best_by_category(my_priority)

        if my_item_to_swap is None or their_item_to_swap is None:
            return False
        
        self.swap_items(other_vendor, my_item_to_swap, their_item_to_swap)
        return True 
