import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Condition 0-heavily used"
        elif self.condition == 1:
            return "Condition 1"
        elif self.condition == 2:
            return "Condition 2"
        elif self.condition == 3:
            return "Condition 3"
        elif self.condition == 4:
            return "Condition 4"
        elif self.condition == 5:
            return "Condition 5-mint condition"
        
        raise ValueError("Unknown Condition Type")