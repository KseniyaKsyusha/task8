from AbstractAnimal import AbstractAnimal


class Cat(AbstractAnimal):

    def __init__(self, bow_tie, cane):
        super().__init__("Begemot")
        self.__bow_tie = bow_tie
        self.__cane = cane

    @property
    def bow_tie(self):
        return self.__bow_tie

    @bow_tie.setter
    def bow_tie(self, bow_tie):
        self.__bow_tie = bow_tie

    @property
    def cane(self):
        return self.__cane

    @cane.setter
    def cane(self, cane):
        self.__cane = cane

    @property
    def name(self):
        return self.animal_name

    def animalSounds(self):
        return 'Meow'

    def move(self):
        super().aac()
        print("I can catch mice")
