class Animal:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type

    def move(self):
        print(self.name, 'is moving')

class Cat(Animal):
    say = 'Meow'
    def __init__(self, name, size, type, color):
        super().__init__(name, size, type)
        self.color = color

    def move(self):
        super().move()
        print(self.name, 'Walking')

class Lion(Cat):
    say = 'Gonzha pidoras'
    def __init__(self, name, size, type, color, pride):
        super().__init__(name, size, type, color)
        self.pride = pride
    
    def atack(self, target):
        print(self.name, 'atack', target.name, '!')

Alice = Cat(color = 'White', name = 'Alice', size = 'small', type = 'predator')
Alice.move()
print(Alice.color)

Simba = Lion(name = 'Simba', size = 'Large', type='predator', color='orange', pride='MIIGAiK')
Simba.atack(Alice)