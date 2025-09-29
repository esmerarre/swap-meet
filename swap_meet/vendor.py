class Vendor:
# Vendor class constructor with empty arrary initialization
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory

# Instance method to add to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

# Instance method to remove item in inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item 
