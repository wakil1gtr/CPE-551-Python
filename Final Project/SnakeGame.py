import pygame
import random

#Project Description:
# From python code I would like to make a game. It will have the following requirements:
#- As you know the snake game where the snake gets bigger as you eat the apple. My game is like that but in reverse. 
#- Essentially there will be three choices for the users at the home screen Easy, Medium, Hard.
#- Easy level: Snake is 15 ft long and will get 1 ft smaller when the snake eats an apple. 
#- Medium level: Snake is 25 ft long and will get 1 ft smaller when the snake eats an apple.
#- Hard level: Snake is 35 ft long and will get 1 ft smaller when the snake eats an apple.
#- I will have the snake's length size shown in the upper right corner of the screen and have it be updated to the snakes new length. 
#- As it eats an apple and when the snake is out of length it will say "You Won Congrats!" 
#- If snake hits the wall it is game over for player
#= Also if the snake crashes into itself it is also game over.
#- Whenever the player loses, a Game Over You Lost screen will appear and users will have the choice to play again.
#- User will also have the choice to play again even if they have won. 

Name = "Wakil Andalib CPE 551 Final Project"
EASY = 0
MEDIUM = 1
HARD = 2
width = 800
height = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (211,211,211)
GREEN = (144,238,144)
RED = (178,34,34)
pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Reverse Snake Game")
font = pygame.font.Font('freesansbold.ttf', 32)
BackGround = SnakeBody = pygame.image.load('BackGround.jpg')
BackGround = pygame.transform.scale(BackGround, (width, height))
SnakeHead = pygame.image.load('SnakeHead.png')
SnakeBody = pygame.image.load('SnakeBody.png')
Apple = pygame.image.load('Apple.png')
velocity = 32
Size = [14, 24, 34]
Dimension = 32
listX = [32]
listY = [height - 2*Dimension]

def Screen1Update(string, textColor, BackGroungColor, y):
    displayButton('Easy', BLACK, GREEN, 200)
    displayButton('Medium', BLACK, GREEN, 250)
    displayButton('Hard', BLACK, GREEN, 300)

    displayButton(string, textColor, BackGroungColor, y)
    pygame.display.update()


def displayButton(string, textColor, BackGroungColor, y):
    Font_string = font.render(string, True, textColor, BackGroungColor)
    Font_string_Rect = Font_string.get_rect().center = (width / 2 - Font_string.get_rect().width / 2, y)
    button = window.blit(Font_string, Font_string_Rect)
    return button


def Screen1():
    pygame.mouse.set_visible(1)
    window.fill(WHITE)
    window.blit(BackGround,(0,0))

    displayButton('Reverse Snake Game', BLACK, GREY, 0)
    Easy_button = displayButton('Easy', BLACK, GREEN, 200)
    Medium_button = displayButton('Medium', BLACK, GREEN, 250)
    Hard_button = displayButton('Hard', BLACK, GREEN, 300)
    displayButton('By: ' + Name, BLACK, GREY, height - 100)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Easy_button.collidepoint(pos):
                    return EASY
                elif Medium_button.collidepoint(pos):
                    return MEDIUM
                elif Hard_button.collidepoint(pos):
                    return HARD

            elif event.type != pygame.MOUSEBUTTONDOWN:
                if Easy_button.collidepoint(pos):
                    Screen1Update('Easy', BLACK, WHITE, 200)
                elif Medium_button.collidepoint(pos):
                    Screen1Update('Medium', BLACK, WHITE, 250)
                elif Hard_button.collidepoint(pos):
                    Screen1Update('Hard', BLACK, WHITE, 300)
                else:
                    Screen1Update("", WHITE, WHITE, 0)


def Screen2Update():
    window.fill(GREEN)
    for i in range(len(listX)-1):
        window.blit(SnakeBody, (listX[i+1], listY[i+1]))
    SnakeHead_local = pygame.transform.rotate(SnakeHead, Headangle)
    window.blit(SnakeHead_local, (listX[0], listY[0]))
    window.blit(Apple, (Apple_Dim[0],Apple_Dim[1]))
    font = pygame.font.SysFont(None, 35)
    text = font.render('Size(ft): ' + str(len(listX)), True, BLACK)
    window.blit(text, (width-200 , 42))
    pygame.draw.rect(window, RED, [0, 0, 32, height])
    pygame.draw.rect(window, RED, [width-32, 0, 32, height])
    pygame.draw.rect(window, RED, [0, 0, width, 32])
    pygame.draw.rect(window, RED, [0, height-32, width, 32])
    pygame.display.update()


def listUpdate(x,y):
    tempX = listX[0]
    tempY = listY[0]
    listX[0] = (listX[0] + x)%width
    listY[0] = (listY[0] + y)%height
    for i in range(len(listX)-1):
        temp1X = listX[i+1]
        temp1Y = listY[i+1]
        listX[i+1] = tempX
        listY[i+1] = tempY
        tempX = temp1X
        tempY = temp1Y


def Rect(x,y,h,w):
    rect = pygame.Rect(0,0,h,w)
    rect.center = (x,y)
    return rect


def Screen2(level):
    global Headangle
    Headangle = 0
    window.fill(WHITE)

    for i in range(Size[level]):
        listX.append(32 - (i+1)*Dimension)
        listY.append(height - 2*Dimension)

    global  Apple_Dim
    Apple_Dim = [random.random() * (width - 3*Dimension)+32, random.random() * (height - 3*Dimension)+32]
    Screen2Update()
    run = True
    while run:
        pygame.time.wait(80)
        x = y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if a person press quit button(X)
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if Headangle == 90:
                       Headangle = (Headangle + 90) % 360
                    elif Headangle == 270:
                        Headangle = (Headangle + 270) % 360

                elif event.key == pygame.K_RIGHT:
                    if Headangle == 90:
                        Headangle = (Headangle + 270) % 360
                    elif Headangle == 270:
                        Headangle = (Headangle + 90) % 360

                elif event.key == pygame.K_UP:
                    if Headangle == 0:
                        Headangle = (Headangle + 90) % 360
                    elif Headangle == 180:
                        Headangle = (Headangle + 270) % 360

                elif event.key == pygame.K_DOWN:
                    if Headangle == 0:
                        Headangle = (Headangle + 270) % 360
                    elif Headangle == 180:
                        Headangle = (Headangle + 90) % 360

        if Headangle == 0:
            x = x + velocity
            listUpdate(x, y)
        elif Headangle == 180:
            x = x - velocity
            listUpdate(x, y)
        elif Headangle == 90:
            y = y - velocity
            listUpdate(x, y)
        elif Headangle == 270:
            y = y + velocity
            listUpdate(x, y)

        Screen2Update()

        Snake_Head_rect = Rect(listX[0], listY[0], Dimension, Dimension)
        Apple_rect = Rect(Apple_Dim[0], Apple_Dim[1], Dimension, Dimension)
        if Snake_Head_rect.colliderect(Apple_rect):
            Apple_Dim = [random.random() * (width - 3 * Dimension) + 32,
                         random.random() * (height - 3 * Dimension) + 32]
            listX.pop()
            listY.pop()
            if len(listX) <= 0:
                print("You won!!")
                return True

        if listX[0]<32 or listY[0]<32 or listX[0]+5>(width-32) or listY[0]+5>(height-32):
            return False


        for i in range(len(listX)-1):
            rect = Rect(listX[i+1], listY[i+1], Dimension, Dimension)
            if Snake_Head_rect.colliderect(rect):
               return False


def Screen3(status):
    window.fill(WHITE)
    window.blit(BackGround, (0, 0))
    PlayAgain_Button = displayButton('Play Again', BLACK, WHITE, 200)
    if status:
       displayButton('You Won Congrats!!!', BLACK, GREY, int(height/2))
    else:
       displayButton('Game Over You Lost!!!', RED, GREY, int(height/2))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and PlayAgain_Button.collidepoint(pos):
                return True
            

if __name__ == '__main__':
    Condition = True
    while Condition:    
          level = Screen1()     
          listX = [32]  
          listY = [height - 2 * Dimension]    
          Condition = Screen3(Screen2(level))
    pygame.quit()


