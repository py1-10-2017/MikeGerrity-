class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health = self.health - 1 
        print "Health = " + str(self.health)
        return self

    def run(self):
        self.health = self.health - 5 
        print "Health = " + str(self.health)
        return self

a1 = Animal("Zebra")

a1.walk()
a1.run()

class Dog(Animal):
    def __init__(self): 
        super(Dog, self).__init__()
        self.health = 150
        
    def pet(self): 
        self.health = self.health + 5
        print "Thanks for the Petting, My Health is now " + str(self.health)
        return self
    
dog1 = Dog("Charlie")

dog1.walk().walk().walk().run().run().pet()

class Dragon(Animal):
    def __init__(self): 
        super(Dragon, self).__init__()
        self.health = 170

    def fly(self): 
        self.health = self.health - 10
        print "I am a Dragon, my current health is " + str(self.health)
        return self

dragon1 = Dragon("Eugene")

dragon1.fly()
dog1.fly()



