# Used to randomly generate the x and y of the food
import random
# Use to return rect object that can be used in main.py
import pygame

class Food:
    def __init__(self):
        self.x = random.randrange(0, 64) * 10
        self.y = random.randrange(0, 48) * 10
        self.width = self.height = 10
        self.isEaten = False
        self.color = (70, 171, 105)

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getIsEaten(self):
        return self.isEaten
