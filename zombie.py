"""
zombie.py
---------
Defines a Zombie class.

A Zombie has:
- A type (e.g., Walker, Runner)
- A damage value (amount of damage they deal)

TODO:
  1. Add a zombie health attribute
  2. Add a take_damage() method
  3. Add is_dead() method
These are tested in test_game.py
"""

class Zombie:
    def __init__(self, type="Walker", damage=15,health=50):
        self.type = type
        self.damage = damage
        self.health = health
        

        # TODO: Add health attribute (default 50)
        # self.health = 50

    def attack(self, survivor,):
        """Deal damage to a survivor."""
        survivor.take_damage(self.damage)
        
    def take_damage(self,amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        
    # TODO: Implement take_damage(amount) so zombies can be damaged
    # TODO: Implement is_dead() -> returns True if health <= 0
    def is_dead(self,health):
        if self.health <= 0:
            return True
        
    def __str__(self):
        return f"Zombie Type: {self.type} (Damage: {self.damage})"
