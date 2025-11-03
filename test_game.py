import unittest
from survivor import Survivor
from zombie import Zombie

class TestGame(unittest.TestCase):

    def test_survivor_heal(self):
        s = Survivor("Test", health=50)
        s.heal(30)
        self.assertEqual(s.health, 80)

    def test_survivor_heal_caps_at_100(self):
        s = Survivor("Test", health=90)
        s.heal(50)
        self.assertEqual(s.health, 100)

    def test_remove_item(self):
        s = Survivor("Test")
        s.pick_up("Water Bottle")
        s.remove_item("Water Bottle")
        self.assertNotIn("Water Bottle", s.inventory)

    def test_remove_item_safely(self):
        s = Survivor("Test")
        # Should NOT crash if item doesn't exist
        s.remove_item("Pizza")
        self.assertEqual(s.inventory, [])

    def test_zombie_has_health(self):
        z = Zombie()
        self.assertTrue(hasattr(z, "health"))

    def test_zombie_take_damage(self):
        z = Zombie()
        z.health = 50
        z.take_damage(20)
        self.assertEqual(z.health, 30)

    def test_zombie_is_dead(self):
        z = Zombie()
        z.health = 0
        self.assertTrue(z.is_dead())

if __name__ == "__main__":
    unittest.main()
