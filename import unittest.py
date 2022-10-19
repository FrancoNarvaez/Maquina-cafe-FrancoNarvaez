import unittest

class NoCoinExeption(Exception):
    pass

class NoCreateExeption(Exception):
   pass

class CoffeeMachinePlus:

    def __init__(self):
        self.coin = 0
        self.sugar = 0
        self.resources = {
            'sugar' : 0,
            'coffee' : 0,
            'milk' : 0,
            'tea' : 0
        }
        self.recipies = {
            'coffee_alone' : {
                'coffee' : 30,
            },
            'coffee_milk' : {
                'coffee' : 30,
                'milk' : 200
            },
            'coffee_doble_alone' : {
                'coffee' : 60,
            },
            'coffee_doble_milk' : {
                'coffee' : 60,
                'milk' : 200
            },
            'tea_simple_alone' : {
                'tea' : 10
            },
            'tea_milk' : {
                'tea' : 10,
                'milk' : 200
            },
        }

    def add_resources(self, type, amount):
        self.resources[type] += amount

    def create_drink (self, create):
        if self.coin == 0:
            raise NoCoinExeption()
        drink = self.recipies[create]
        for type in drink.keys():
            if self.resources(type) < self.resources(create):
                raise NoCreateExeption ('Missing {}'.format(type))
        self.coin -= 1
        if type in drink.key():
            self.resources[type] -= self.recipies[type]

    def add_coin(self):
        self.coin += 1

class TestCoffee(unittest.TestCase):
    def test_inicial_coin(self):
        machine = CoffeeMachinePlus()
        self.assertEqual(machine.coin, 0)

    def test_add_coin(self):
        machine = CoffeeMachinePlus()
        machine.add_coin()
        self.assertEqual(machine.coin, 1)

    def test_inicial_sugar(self):
        machine = CoffeeMachinePlus()
        self.assertEqual(machine.sugar, 0)

    def test_inicial_resources(self):
        machine = CoffeeMachinePlus()
        self.assertEqual(machine.resources,{'sugar':0,'coffee':0,'milk':0,'tea':0})

    def test_add_resources_correct(self):
        machine = CoffeeMachinePlus()
        machine.add_resources(type= 'sugar', amount= 800)
        machine.add_resources(type= 'coffee', amount= 1000)
        machine.add_resources(type= 'milk', amount= 5000)
        machine.add_resources(type= 'tea', amount= 500)
        self.assertEqual(machine.resources,{'sugar': 800, 'coffee': 1000, 'milk': 5000, 'tea': 500})

    def test_exeption_nocoin(self):
        machine = CoffeeMachinePlus()
        with self.assertRaises(NoCoinExeption):
            machine.create_drink('coffee_alone')
if __name__ == "__main__":
    unittest.main()