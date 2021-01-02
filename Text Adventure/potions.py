import items

class potion(items.item):
    def __init__(self, itemName, itemType, potionType, potionStrength, note):
        items.item.__init__(self, itemName, itemType)
        self.potionType = potionType
        self.potionStrength = potionStrength
        self.note = note
        
        
        