import sys, pygame
import itertools
from pygame.version import ver

NUM_BUTTONS = 20
INITIAL_PADDING = 150
BUTTON_ROW_GAME1 = 5
BUTTON_COL_GAME1 = 4
BUTTON_ROW_GAME2 = 8
BUTTON_COL_GAME2 = 6

TOTAL_COLOURS_GAME1 = 3
ALL_COLOURS_GAME1 = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


TOTAL_COLOURS_GAME2 = 5
ALL_COLOURS_GAME2 = [(245, 130, 49), (255, 225, 25), (60, 180, 75), (66, 212, 244), (240, 32, 230)]

size = width, height = 1500, 750
screenColor = (0, 0, 0)

initialButtonColor = (255, 255, 255)
gameButtonWidth_1 = 282
gameButtonHeight_1 = 125
gameButtonWidth_2 = 165
gameButtonHeight_2 = 75
initialButtonTextColor = (0, 0, 0)

colourButtonHeight = headingColourHeight = INITIAL_PADDING - 25
colourButtonWidth = 300
headingColourWidth = 350 
colourButtonOutlineColour = (204, 204, 0)


headingTextButtonColor = (0, 0, 0)
headingTextColor = (255, 255, 255)
correctFontColor = (0, 255, 0)
incorrectFontColor = (255, 0, 0)
initialFontColor = (255, 255, 255)
rectColor = (255, 255, 255)

optionButtonWidth = 600
optionButtonHeight = 300

class button():
    def __init__(self, color, x,y,width,height, textColor = (0,0,0), text='', btnList = None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textColor = textColor
        self.text = text
        if btnList != None:
            btnList.append(self)

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-5,self.y-5,self.width+10,self.height+10),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, self.textColor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def drawGameOption(win):

    b1 = button(initialButtonColor, 100 , 200, optionButtonWidth, optionButtonHeight, initialButtonTextColor, "2 - players 3 - colours", None)
    b2 = button(initialButtonColor, 100 * 2 + optionButtonWidth , 200, optionButtonWidth, optionButtonHeight, initialButtonTextColor, "5 player elimination", None)
    b1.draw(win)
    b2.draw(win)

    return b1, b2

def drawEquationOption(win):
    btnList = []

    button(initialButtonColor, 100 , 200, optionButtonWidth, optionButtonHeight, initialButtonTextColor, "x + y = z", btnList)
    button(initialButtonColor, 100 * 2 + optionButtonWidth , 200, optionButtonWidth, optionButtonHeight, initialButtonTextColor, "x + y = 2z", btnList)

    for btn in btnList:
        btn.draw(win)

    return btnList



def drawNumbers_game1(win):
    btnList = []
    vertical_pad = (height - INITIAL_PADDING - BUTTON_COL_GAME1 * gameButtonHeight_1)/(BUTTON_COL_GAME1 + 1)
    horizontal_pad = (width - BUTTON_ROW_GAME1 * gameButtonWidth_1)/(BUTTON_ROW_GAME1 + 1)
    for i in range(1, BUTTON_ROW_GAME1 + 1):
        for j in range (1, BUTTON_COL_GAME1 + 1):
            txt = str (i + (j - 1) * BUTTON_ROW_GAME1)
            x = (i - 1) * (gameButtonWidth_1 + horizontal_pad) + horizontal_pad
            y  = INITIAL_PADDING + (j -  1) * (gameButtonHeight_1 + vertical_pad) + vertical_pad
            button(initialButtonColor, x, y, gameButtonWidth_1, gameButtonHeight_1, initialButtonTextColor, txt, btnList)
    for btn in btnList:
        btn.draw(win)

    return btnList


def drawNumbers_game2(win):
    btnList = []
    vertical_pad = (height - INITIAL_PADDING - BUTTON_COL_GAME2 * gameButtonHeight_2)/(BUTTON_COL_GAME2 + 1)
    horizontal_pad = (width - BUTTON_ROW_GAME2 * gameButtonWidth_2)/(BUTTON_ROW_GAME2 + 1)
    for i in range(1, BUTTON_ROW_GAME2 + 1):
        for j in range (1, BUTTON_COL_GAME2 + 1):
            txt = str (i + (j - 1) * BUTTON_ROW_GAME2)
            x = (i - 1) * (gameButtonWidth_2 + horizontal_pad) + horizontal_pad
            y  = INITIAL_PADDING + (j -  1) * (gameButtonHeight_2 + vertical_pad) + vertical_pad
            button(initialButtonColor, x, y, gameButtonWidth_2, gameButtonHeight_2, initialButtonTextColor, txt, btnList)
    for btn in btnList:
        btn.draw(win)

    return btnList


def makeColourButtons_game1(win):
    heading = button(screenColor, 50, 25, 350, 125, (255, 255, 255), "Pick a colour: ")
    heading.draw(win)
    colourButtons = []
    for i in range(TOTAL_COLOURS_GAME1):
        btn = button(ALL_COLOURS_GAME1[i], 50*(i + 1) + 350 + 300 * i, 25, 300, 125, (255, 255, 255), "", colourButtons)
        btn.draw(win)
    return colourButtons

def makeColourButtons_game2(win):
    colourButtons = []
    for i in range(TOTAL_COLOURS_GAME2):
        btn = button(ALL_COLOURS_GAME2[i], 50*(i + 1) + 240 * i, 25, 240, 125, (0, 0, 0), "Player " + str(i + 1), colourButtons)
        btn.draw(win)
    return colourButtons


pygame.init()

#making the pygame screen
screen = pygame.display.set_mode(size)

screen.fill(screenColor)

#window caption
pygame.display.set_caption("SCHUR'S GAME")

#initializing the font
font= pygame.font.SysFont("Comic Sans",80)

gameTypeChosen = False
gameEquationChosen = False
initialScreen = True

option_2, option_elimination = drawGameOption(screen)
currentColourFlag = False

green = set()
red = set()
blue = set()

redSubsets = set()
greenSubsets = set()
blueSubsets = set()

game = False

while 1:
    #delay to avoid multiple actions
    pygame.time.delay(100)
    
    #getting updated screen
    pygame.display.update()

    for event in pygame.event.get():

        #exit game if quit
        if event.type == pygame.QUIT: 
            sys.exit()
        
        #getting the position of the mouse cursor
        cursorPosition = pygame.mouse.get_pos()
        

        if game:
            continue

        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if not gameTypeChosen:
                if option_2.isOver(cursorPosition):
                    gameType = 1
                    gameTypeChosen = True
                    eq1, eq2 = drawEquationOption(screen)
                elif option_elimination.isOver(cursorPosition):
                    gameType = 2
                    gameTypeChosen = True 
                    eq1, eq2 = drawEquationOption(screen)
                continue

            if not gameEquationChosen and gameTypeChosen:
                if eq1.isOver(cursorPosition):
                    gameEquation = 1
                    gameEquationChosen = True
                elif eq2.isOver(cursorPosition):
                    gameEquation = 2
                    gameEquationChosen = True
                
            if gameEquationChosen and gameTypeChosen and initialScreen:
                button(screenColor, 0, 0, width, height).draw(screen)
                initialScreen = False
                if gameType == 1:
                    colourButtons = makeColourButtons_game1(screen)
                    allButtons = drawNumbers_game1(screen)
                else:
                    allButtons = drawNumbers_game2(screen)
                    colourButtons = makeColourButtons_game2(screen)

            optimizer = False
            for btn in colourButtons:
                if (btn.isOver(cursorPosition)):
                    btn.draw(screen, colourButtonOutlineColour)
                    currentColour = btn.color
                    currentColourFlag = True
                    optimizer = True
                else:
                    btn.draw(screen, btn.color)

            if optimizer:
                continue

            for btn in allButtons:
                if (btn.isOver(cursorPosition)):
                    print(btn.text) 
                    if(currentColourFlag and btn.color == initialButtonColor): 
                        btn.color = currentColour
                        num = int(btn.text)
                        sym = (num, num)
                        if(currentColour == ALL_COLOURS_GAME1[0]):
                            red.add(num)
                            redSubsets.add(sym)
                            redSubsets = set.union(redSubsets, set(itertools.combinations(red, 2)))
                        elif (currentColour == ALL_COLOURS_GAME1[1]):
                            green.add(num)
                            greenSubsets.add(sym)
                            greenSubsets = set.union(greenSubsets, set(itertools.combinations(green, 2)))
                        else:
                            blue.add(num)
                            blueSubsets.add(sym)
                            blueSubsets = set.union(blueSubsets, set(itertools.combinations(blue, 2)))
                        btn.draw(screen)
                        print(redSubsets, greenSubsets, blueSubsets)
                        break

            for pair in redSubsets:
                if gameEquation == 1:
                    if pair[0] + pair[1] in red:
                        game = True
                        sce = [pair, "red"]
                        break
                else:
                    print(0.5 * (pair[0] + pair[1]))
                    if 0.5 * (pair[0] + pair[1]) in red and pair[0] != pair[1]:
                        game = True
                        sce = [pair, "red"]
                        break

            for pair in greenSubsets:
                if gameEquation == 1:
                    if pair[0] + pair[1] in green:
                        game = True
                        sce = [pair, "green"]
                        break
                else:
                    if 0.5 * (pair[0] + pair[1]) in green and pair[0] != pair[1]:
                        game = True
                        sce = [pair, "green"]
                        break

            for pair in blueSubsets:
                if gameEquation == 1:
                    if pair[0] + pair[1] in blue:
                        game = True
                        sce = [pair, "blue"]
                        break
                else:
                    if 0.5 * (pair[0] + pair[1]) in blue  and pair[0] != pair[1]:
                        game = True
                        sce = [pair, "blue"]
                        break

    if game:
        print(sce)
        num1 = sce[0][0]
        num2 = sce[0][1]
        sum = num1 + num2
        num1 = str(num1)
        num2 = str(num2)
        if gameEquation == 1:
            sum = str(sum)
        else:
            sum = str(int(sum/2))
        for btn in allButtons:
            if btn.text == num1 or btn.text == num2 or btn.text == sum:
                continue
            btn.color = initialButtonColor
            btn.draw(screen)
            

              
                        

       
