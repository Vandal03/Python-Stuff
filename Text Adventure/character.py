import textFunctions

class character:
    def __init__(self, firstName):
        self.firstName = firstName
        self.items = []
        self.health = 10
        
        
    def addItem(self, item):
        self.items.append(item)
        if item.itemType == "Potion":
            if item.potionType == "Health":
                textFunctions.slowText(f"You have acquired a {item.itemName}. It can restore {item.potionStrength} health. ", 0.05, 1)
        elif item.itemType == "Weapon":
            textFunctions.slowText(f"You have acquried an {item.itemName}. It can do {item.weaponStrength} damage.", 0.05, 1)
        
    def useItem(self, item):
        if item.itemType == "Potion":
            if item.potionType == "Health":
                textFunctions.slowText(f"You used a {item.itemName} and restored {item.potionStrength} health points.", 0.05, 1)
                self.health += item.potionStrength
                if self.health > 10:
                    self.health = 10
        
    def checkHealth(self):
        textFunctions.slowText(f"You have {self.health} points. ", 0.05, 1)