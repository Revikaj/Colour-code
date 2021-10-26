import sys, pygame

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

pygame.init()

#making the pygame screen
screen = pygame.display.set_mode(size)

screen.fill(screenColor)

#window caption
pygame.display.set_caption("SCHUR'S GAME")

#initializing the font
font= pygame.font.SysFont("Comic Sans",80)


while 1:
    #delay to avoid multiple actions
    pygame.time.delay(100)
    
  

    #rendering required screen according to inputs
   
        
    
    #getting updated screen
    pygame.display.update()

    for event in pygame.event.get():

        #getting the position of the mouse cursor
        cursorPosition = pygame.mouse.get_pos()
        
        #exit game if quit
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue
            
                        

       
