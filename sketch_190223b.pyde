from random import randint
import pygame

#Global variables
WIDTH = 150
blacks = 1


class Tile:
    def __init__(self):
        self.pressed = False

grid = [  [Tile() for n in range(6)] for n in range(6) ]     
print grid        

for n in range(blacks):
    x = randint(0, 6)
    y = randint(0, 6)
    if grid[y][x].pressed == False:
        grid[y][x].pressed = True

def setup():
    size(900,900)
    
def draw():
    y = 0
    for row in grid:
        x = 0
        for Tile in row:
            if Tile.pressed == True:
                fill(0, 0, 0)
            else:
                fill(255, 255, 255)
            rect(x,y,WIDTH,WIDTH)
            x+=WIDTH
        y+=WIDTH
                
            
    
    
