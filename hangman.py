import pygame
import math
import random
#from numpy import *

pygame.init()

X = 1000
Y = 1000

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
display_surface = pygame.display.set_mode((X, Y))

titleFont = pygame.font.Font('freesansbold.ttf', 32)
wordFont = pygame.font.Font('freesansbold.ttf', 50)
loseFont = pygame.font.Font('freesansbold.ttf', 100)

# these guys literally watching anime wtf and omri is watching cars -_-


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def displayTitle():
    title = titleFont.render("Countries Hangman", True, white)
    titleRect = title.get_rect()
    titleRect.center = (X * 0.5, Y * 0.2)
    display_surface.blit(title, titleRect)




def getWord():
    global wrongGuessCounter
    wrongGuessCounter = 9
    global gameWord
    wordBank = []
    with open("countryBank.txt", 'r') as f:
        fileData = f.readlines()
        for line in fileData:
            wordBank.append(line.replace('\n', ''))
    genWord = "Saint Vincent and the Grenadines" # wordBank[random.randrange(0, 193)]
    if len(genWord) > 15:
        enterNeed = True
    tempWord, gameWord = "", ""

    for char in genWord:
        tempWordLen = len(tempWord)
        if enterNeed == True and char == " " and tempWordLen >=30:
            tempWord += "\n"
            gameWord += "\n"
            enterNeed = False
        elif char == " " or char == "-":
            tempWord += char + " "
            gameWord += char + " "
        else:
            tempWord += char + " "
            gameWord += "_ "


        if char == " " or char == "-":
            gameWord += char + " "
        else:
            gameWord += "_ "

    tempWord, gameWord = tempWord[:-1], gameWord[:-1]
    print (tempWord)
    print(gameWord)


def displayGameSetup():
    global wrongGuessCounter
    # pregame hangman
    # base horizontal line
    pygame.draw.line(screen, white, (X * 0.3, Y * 0.6), (X * 0.5, Y * 0.6), width=3)
    # vertical baseline
    pygame.draw.line(screen, white, (X * 0.4, Y * 0.6), (X * 0.4, Y * 0.25), width=3)
    # horizontal top line
    pygame.draw.line(screen, white, (X * 0.4, Y * 0.25), (X * 0.55, Y * 0.25), width=3)
    # head holder line
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.3), (X * 0.55, Y * 0.25), width=3)

    if wrongGuessCounter >= 1:
        pygame.draw.circle(screen, white, (X * 0.55, Y * 0.335), (X * 0.035), width=3) # head
    if wrongGuessCounter >= 2:
        pygame.draw.line(screen, white, (X * 0.55, Y * 0.368), (X * 0.55, Y * 0.5), width=3) # body
    if wrongGuessCounter >= 3:
        pygame.draw.line(screen, white, (X * 0.55, Y * 0.5), (X * 0.5, Y * 0.55), width=3) # left leg
    if wrongGuessCounter >= 4:
        pygame.draw.line(screen, white, (X * 0.55, Y * 0.5), (X * 0.6, Y * 0.55), width=3) # right leg
    if wrongGuessCounter >= 5:
        pygame.draw.line(screen, white, (X * 0.55, Y * 0.4), (X * 0.5, Y * 0.43), width=3) # left hand
    if wrongGuessCounter >= 6:
        pygame.draw.line(screen, white, (X * 0.55, Y * 0.4), (X * 0.6, Y * 0.43), width=3) # right hand
    if wrongGuessCounter >= 7:
        pygame.draw.circle(screen, white, (X * 0.535, Y * 0.33), (X * 0.005)) # left eye
    if wrongGuessCounter >= 8:
        pygame.draw.circle(screen, white, (X * 0.565, Y * 0.33), (X * 0.005)) # right eye
    if wrongGuessCounter >= 9:
        pygame.draw.arc(screen, white, (X * 0.535, Y * 0.347, X * 0.03, Y * 0.01), 2 * math.pi, 1 * math.pi) # mouth
        loseText = loseFont.render("YOU LOST", True, red)
        lostRect = loseText.get_rect()
        lostRect.center = (X * 0.5, Y * 0.5)
        display_surface.blit(loseText, lostRect)

def displayWord():
    global gameWord
    gameWordShow = wordFont.render(gameWord, True, white)
    gameWordRect = gameWordShow.get_rect()
    gameWordRect.center = (X * 0.5, Y * 0.8)
    display_surface.blit(gameWordShow, gameWordRect)



getWord()


while True:
    displayTitle()
    displayGameSetup()
    displayWord()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
