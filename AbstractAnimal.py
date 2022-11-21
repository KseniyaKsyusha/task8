import abc


class AbstractAnimal(abc.ABC):

    @abc.abstractmethod
    def __init__(self, animal_name):
        self.animal_name = animal_name

    @property
    @abc.abstractmethod
    def name(self):
        pass

    def aac(self):
        print("Abstract Animal Class")

    @abc.abstractmethod
    def animalSounds(self):
        pass

    @abc.abstractmethod
    def move(self):
        pass
