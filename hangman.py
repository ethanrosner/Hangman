import pygame
import math
import random

pygame.init()

X = 1000
Y = 1000

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Takes Care of the word bank

wordBank = []
with open("countryBank.txt", 'r') as f:
    fileData = f.readlines()
    for line in fileData:
        wordBank.append(line.replace('\n', ''))

# Word bank is successfully filled.

display_surface = pygame.display.set_mode((X, Y))
titleFont = pygame.font.Font('freesansbold.ttf', 32)
wordFont = pygame.font.Font('freesansbold.ttf', 50)
title = titleFont.render("Countries Hangman", True, white)
titleRect = title.get_rect()
titleRect.center = (X * 0.5, Y * 0.2)

# def getWord():
rSlotN = random.randrange(0,193)
genCountry = wordBank[rSlotN]
# genCountryL = len(genCountry)
# print(genCountryL)

genCountryReplaced = ""

print(genCountry)

for char in genCountry:
    if char != " " and char != "-":
        genCountryReplaced += "_ "
    elif char == " ":
        genCountryReplaced += "  "
    elif char == "-":
        genCountryReplaced += "-"
print(genCountryReplaced)

genWordShow = wordFont.render(genCountryReplaced, True, white)
genRect = genWordShow.get_rect()
genRect.center = (X * 0.5, Y * 0.8)

# def playGame():


while True:
    display_surface.blit(title, titleRect)
    # pregame hangman
    # base horizontal line
    pygame.draw.line(screen, white, (X * 0.3, Y * 0.6), (X * 0.5, Y * 0.6), width=3)
    # vertical baseline
    pygame.draw.line(screen, white, (X * 0.4, Y * 0.6), (X * 0.4, Y * 0.25), width=3)
    # horizontal top line
    pygame.draw.line(screen, white, (X * 0.4, Y * 0.25), (X * 0.55, Y * 0.25), width=3)
    # head holder line
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.3), (X * 0.55, Y * 0.25), width=3)

    # drawing word text
    display_surface.blit(genWordShow, genRect)

    # in game drawing
    # head
    pygame.draw.circle(screen, white, (X * 0.55, Y * 0.335), (X * 0.035), width=3)
    # body
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.368), (X * 0.55, Y * 0.5), width=3)
    # left leg
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.5), (X * 0.5, Y * 0.55), width=3)
    # right leg
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.5), (X * 0.6, Y * 0.55), width=3)
    # left hand
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.4), (X * 0.5, Y * 0.43), width=3)
    # right hand
    pygame.draw.line(screen, white, (X * 0.55, Y * 0.4), (X * 0.6, Y * 0.43), width=3)
    # left eye
    pygame.draw.circle(screen, white, (X * 0.535, Y * 0.33), (X * 0.005))
    # right eye
    pygame.draw.circle(screen, white, (X * 0.565, Y * 0.33), (X * 0.005))
    # mouth
    pygame.draw.arc(screen, white, (X * 0.535, Y * 0.347, X * 0.03, Y * 0.01), 2 * math.pi, 1 * math.pi)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
