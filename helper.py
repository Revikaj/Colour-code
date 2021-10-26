

import sys, pygame, copy

size = width, height = 750, 750
screenColor = (0, 0, 0)
optionButtonColor = (255, 255, 255)
optionButtonWidth = 200
optionButtonHeight = 100
optionButtonTextColor = (0, 0, 0)

headingTextButtonColor = (0, 0, 0)
headingTextColor = (255, 255, 255)
correctFontColor = (0, 255, 0)
incorrectFontColor = (255, 0, 0)
initialFontColor = (255, 255, 255)
rectColor = (255, 255, 255)

#initializing the pygame window
pygame.init()

#making the pygame screen
screen = pygame.display.set_mode(size)

screen.fill(screenColor)

#window caption
pygame.display.set_caption("Sudoku")

#initializing the font
font= pygame.font.SysFont("Comic Sans",80)

def computeInitialValueGrid(initial_grid):
    new_grid = []
    for row in initial_grid:
        new_row =[]
        for val in row:
            if(val == 0):
                new_row.append(False)
            else:
                new_row.append(True)
        new_grid.append(copy.deepcopy(new_row))
    print("hello")
    return new_grid