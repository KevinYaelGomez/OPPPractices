import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Triangle():
    def __init__(self, window, maxWidth, maxHeigth):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangleSlope = -1 * (self.height /self.width)
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeigth - 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.shapeType = "Triangle"

    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False
        
        xOFFset = mousePoint[0] - self.x
        yOFFset = mousePoint[1] - self.y
        if xOFFset == 0:
            return True
        
        pointSlopeFromYIntercept = (yOFFset - self.height) / xOFFset
        if pointSlopeFromYIntercept < self.triangleSlope:
            return True
        else:
            return False
        
    def getType(self):
        return self.shapeType
    
    def getArea(self):
        area = (self.width * self.height) / 2
        return area
    
    def draw(self):
        pygame.draw.polygon(self.window, self.color, ((self.x, self.y + self.height), (self.x, self.y), (self.x + self.width, self.y)))