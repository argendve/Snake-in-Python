# import to use rect class to return to main.py
import pygame

class Block:
    def __init__(self, x, y, xSpeed, ySpeed):
        self.x = x
        self.y = y
        self.width = self.height = 10
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def copy(self, block):
        self.x = block.x
        self.y = block.y
        self.xSpeed = block.xSpeed
        self.ySpeed = block.ySpeed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getxSpeed(self):
        return self.xSpeed

    def getySpeed(self):
        return self.ySpeed

    # return the block behind this one
    def blockBehind(self):
        return Block(self.x + self.xSpeed, self.y + self.ySpeed,\
                     self.xSpeed, self.ySpeed)

    # Make the block continue to move in the same direction
    def advance(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

        if (self.x > 640 or self.x < 0) or (self.y > 480 or self.y < 0):
            return False
        else:
            return True

    def turnLeft(self):
        if self.xSpeed == 0:
            self.xSpeed = -10
            self.ySpeed = 0

    def turnRight(self):
        if self.xSpeed == 0:
            self.xSpeed = 10
            self.ySpeed = 0

    def moveUp(self):
        if self.ySpeed == 0:
            self.xSpeed = 0
            self.ySpeed = -10

    def moveDown(self):
        if self.ySpeed == 0:
            self.xSpeed = 0
            self.ySpeed = 10

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
