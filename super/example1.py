class Animal:
    def __init__(self,name):
        self.name = name
        print("Animal initialized")

    def speak(self):
        print("Animal makes sound!")

class Dog(Animal):
        def __init__(self,name,breed):
            super().__init__(name) # Calling Parent Constructor
            self.breed = breed
            print("Dog initialized")

        def speak(self):
            super().speak()
            print("Dog Barks!!!")

d = Dog("Tom","Jerry")
d.speak()
