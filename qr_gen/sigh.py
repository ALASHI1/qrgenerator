import time


class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return f" {self.name},{self.age} "

    def __str__(self):
        return self.__class__.__name__


def oldest_dog(dog_lists):
    """This is a class about the Dogs"""
    dog_lists.sort(key=lambda x: x.age, reverse=True)
    print(dog_list)
    print(
        f"The oldest dog is {dog_lists[0].name},its age is {dog_lists[0].age} years old"
    )


dog_list = [Dog(15, "jack"), Dog(18, "billy"), Dog(13, "Bingo")]
oldest_dog(dog_list)


class Dogs:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return f" {self.name},{self.age} "

    def __str__(self):
        return self.__class__.__name__


def oldest_dogs(dog_lists):
    """This is a class about the Dogs"""
    dog_lists.sort(key=lambda x: x.age, reverse=True)
    print(dog_list)
    print(
        f"The oldest dog is {dog_lists[0].name},its age is {dog_lists[0].age} years old"
    )


dog_list = [Dog(15, "jack"), Dog(18, "billy"), Dog(13, "Bingo")]
oldest_dogs(dog_list)
