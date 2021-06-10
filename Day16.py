from typing import MappingView


class Animal:
    shape = ''
    gender = ''
    color = ''
    height = 0.0
    volume = 0.0
    age = 0
    sound = ''
    species = ''
    # def __init__(self, shape, gender, color, height, volume, age, sound, species):
    #     self.shape = shape
    #     self.gender = gender
    #     self.color = color
    #     self.height = height
    #     self.volume = volume
    #     self.age = age
    #     self.sound = sound
    #     self.species = species
    def __int__(self, age, color):
        self.age = age
        self.color = color

    def speak(self):
        print("noise...")
    def eat(self):
        print("munch...")
    def sleep(self):
        print('zzzz...')
    def set_shape(self, shape):
        self.shape = shape
    def set_gender(self, gender):
        self.gender = gender
    def set_color(self, color):
        self.color = color
    def set_heght(self, height):
        self.height = height
    def set_volume(self, volume):
        self.volume = volume
    def set_age(self, age):
        self.age = age
    def set_sound(self, sound):
        self.sound = sound
    def set_speceis(self, species):
        self.species = species

animal1 = Animal()
# animal1.set_shape('circle'), animal1.set_gender('male'), animal1.set_color('black and white'), animal1.set_heght(3.5), animal1.set_volume('loud'), animal1.set_age(15), animal1.set_speceis('dog')
# print(animal1.shape, animal1.age, animal1.color)
animal1(15, 'black and white')
print(animal1.age)

class Dog(Animal):
    # PROPERTIES
    breed = ''
    fur = False
    fur_color = ''
    floppyEars = False

    def fetch():
        pass
    def zoomie():
        pass
    def chewing():
        pass
    def drool():
        pass
    def wag_tail():
        pass

class Lion(Animal):
    # PROPERTIES
    has_mane
    has_pride
    
