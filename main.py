class Cat:

    say = 'Meow'     
    
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return 'Cat name: ' + self.name + '\nCat color:' + self.color + '\nCat age: ' + self.age

    def __repr__(self):
        return 'Cat name: ' + self.name + '\nCat color:' + self.color + '\nCat age: ' + self.age

    def say_name(self):
        print('My name is' + self.name, ',', self.__class__.say, '!')

    @classmethod
    def walk(cls):
        print('cat walks')

    def let_say(cls):
        print(cls.say)

cats = []
Alice = Cat('Alice', 'White', '2')
cats.append(Alice)
Gja = Cat('Gja', 'Black', '1000')
cats.append(Gja)
print(cats[0])
cats[0].say_name()
cats[1].say_name()