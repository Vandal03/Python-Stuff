import items

class weapon:
    def __init__(self, itemName, itemType, weaponType, weaponStrength, note):
        items.item.__init__(self, itemName, itemType)
        self.weaponType = "Dagger"
        self.weaponStrength = 2
        self.note = note
        
        