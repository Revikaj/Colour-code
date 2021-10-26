import sys, pygame
import itertools
from pygame.version import ver

NUM_BUTTONS = 20
INITIAL_PADDING = 150
BUTTON_ROW = 5
BUTTON_COL = 4
TOTAL_COLOURS = 3
ALL_COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

size = width, height = 1500, 750
screenColor = (0, 0, 0)

initialButtonColor = (255, 255, 255)
gameButtonWidth = 282
gameButtonHeight = 125
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

def drawNumbers(win):
    btnList = []
    vertical_pad = (height - INITIAL_PADDING - BUTTON_COL * gameButtonHeight)/(BUTTON_COL + 1)
    horizontal_pad = (width - BUTTON_ROW * gameButtonWidth)/(BUTTON_ROW + 1)
    for i in range(1, BUTTON_ROW + 1):
        for j in range (1, BUTTON_COL + 1):
            txt = str (i + (j - 1) * BUTTON_ROW)
            x = (i - 1) * (gameButtonWidth + horizontal_pad) + horizontal_pad
            y  = INITIAL_PADDING + (j -  1) * (gameButtonHeight + vertical_pad) + vertical_pad
            button(initialButtonColor, x, y, gameButtonWidth, gameButtonHeight, initialButtonTextColor, txt, btnList)
    for btn in btnList:
        btn.draw(win)

    return btnList

def makeColourButtons(win):
    heading = button(screenColor, 50, 25, 350, 125, (255, 255, 255), "Pick a colour: ")
    heading.draw(win)
    colourButtons = []
    for i in range(TOTAL_COLOURS):
        btn = button(ALL_COLOURS[i], 50*(i + 1) + 350 + 300 * i, 25, 300, 125, (255, 255, 255), "", colourButtons)
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

allButtons = drawNumbers(screen)
colourButtons = makeColourButtons(screen)
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
                        if(currentColour == ALL_COLOURS[0]):
                            red.add(num)
                            redSubsets.add(sym)
                            redSubsets = set.union(redSubsets, set(itertools.combinations(red, 2)))
                        elif (currentColour == ALL_COLOURS[1]):
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
                if pair[0] + pair[1] in red:
                    game = True
                    sce = [pair, "red"]
                    break

            for pair in greenSubsets:
                if pair[0] + pair[1] in green:
                    game = True
                    sce = [pair, "green"]
                    break

            for pair in blueSubsets:
                if pair[0] + pair[1] in blue:
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
        sum = str(sum)
        for btn in allButtons:
            if btn.text == num1 or btn.text == num2 or btn.text == sum:
                continue
            btn.color = initialButtonColor
            btn.draw(screen)
            

              
                        

       
