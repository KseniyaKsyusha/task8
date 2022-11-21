from Cat import Cat
from Lion import Lion
from AbstractAnimal import AbstractAnimal

if __name__ == '__main__':
    cat = Cat("bow_tie", "cane")
    print(f"The animal name is: {cat.name, cat.bow_tie, cat.cane}")
    cat.move()
    cat.animalSounds()
    print()

    lion = Lion("king")
    print(f"The animal name is: {lion.king, lion.name}")
    lion.move()
    lion.animalSounds()

    print()

    try:
        absAnim = AbstractAnimal()
    except Exception as error:
        print("ERROR")
        print(error)
