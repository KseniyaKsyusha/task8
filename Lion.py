from AbstractAnimal import AbstractAnimal


class Lion(AbstractAnimal):
    def __init__(self, king):
        super().__init__("Lion")
        self.__king = king

    @property
    def king(self):
        return self.__king

    @king.setter
    def king(self, king):
        self.__king = king

    @property
    def name(self):
        return self.animal_name

    def animalSounds(self):
        print("Roar")

    def move(self):
        print("I can roar")
