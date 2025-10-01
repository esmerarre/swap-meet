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
            return "heavily used 0"
        elif self.condition == 1:
            return "gently used 1"
        elif self.condition == 2:
            return "barely used 2"
        elif self.condition == 3:
            return "brand new 3"
        elif self.condition == 4:
            return "with tags 4"
        elif self.condition == 5:
            return "mint condition 5"
        
        #raising an Error if the conditions are not between 0-5
        raise ValueError("Unknown Condition Type")