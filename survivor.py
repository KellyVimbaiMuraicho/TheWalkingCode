"""
survivor.py
-----------
Defines the Survivor class used in the game.

A Survivor has:
- A name
- Health (default 100)
- An inventory of items

TODOs:
  1. Implement the heal() method (should increase health but NOT above 100)
  2. Implement remove_item() so survivors can drop an item

These TODOs are tested in test_game.py
"""

class Survivor:
    def __init__(self, name, item , health=100):
        """
        Create a new survivor.

        Parameters:
        name (str): The survivor's name.
        health (int): Starting health (default 100).
        """
        self.name = name
        self.item = item
        self.health = health
        self.inventory = []
        
        

    def pick_up(self, item):
        """Add an item to the survivor's inventory."""
        self.inventory.append(item)

    def remove_item(self,item):
        """
        TODO:
        Remove an item from inventory *if it exists*.
        If the item is NOT in the inventory, do nothing.
        """
        if self.item in self.inventory:
            self.remove_item("") 
        elif self.item() not in self.inventory:
            pass
            

    def take_damage(self, amount):
        """
        Reduce the survivor's health. Health should not go below 0.
        """
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        """
        TODO:
        Increase survivor health by `amount`.
        Health should NOT exceed 100.
        
        """
        self.heal += amount
        if self.heal <= 0:
            self.health = 100
            
        pass  # TODO implement this

    def is_alive(self):
        """Return True if survivor is still alive."""
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Inventory: {self.inventory})"
