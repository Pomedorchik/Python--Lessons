class Animal:
    def __init__(self, animal_type=None):
        self.animal_type = animal_type

    def speak(self):
        print("Животное издает звук")

    def move(self):
        print("Животное передвигается")
