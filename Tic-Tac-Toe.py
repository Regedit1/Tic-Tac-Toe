#git test
import pygame
import sys
from pygame.locals import *

pygame.init()
bg = "Background.jpg"
screen = pygame.display.set_mode((300,300),0, 32)
background = pygame.image.load(bg).convert()
pygame.display.set_caption("Tic Tac Toe")
turn = "o"   #controls which sign plays first, change between "x" and "o"


pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#Works out which box on grid has been clicked, see "pos reference"
def whichbox(x, y):
    mousepos = 0
    if x < 100:
        if y < 100:
            mousepos = 0
        elif y < 200:
            mousepos = 3
        elif y < 300:
            mousepos = 6
    elif x < 200:
        if y < 100:
            mousepos = 1
        elif y < 200:
            mousepos = 4
        elif y < 300:
            mousepos = 7
    elif x < 300:
        if y < 100:
            mousepos = 2
        elif y < 200:
            mousepos = 5
        elif y < 300:
            mousepos = 8

    return mousepos



def drawmove(box):
    if turn == "x":
        if box == 0:
            if pos[box] != "o":
            
                pygame.draw.line(background, (0,0,0), (25, 75),(75, 25))
                pygame.draw.line(background, (0,0,0), (25, 25),(75, 75))
                pos[box] = "x"
                
            
        if box == 1:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (125, 75),(175, 25))
                pygame.draw.line(background, (0,0,0), (125, 25),(175, 75))
                pos[box] = "x"
        if box == 2:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (225, 75),(275, 25))
                pygame.draw.line(background, (0,0,0), (225, 25),(275, 75))
                pos[box] = "x"
        if box == 3:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (25, 175),(75, 125))
                pygame.draw.line(background, (0,0,0), (25, 125),(75, 175))
                pos[box] = "x"
        if box == 4:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (125, 175),(175, 125))
                pygame.draw.line(background, (0,0,0), (125, 125),(175, 175))
                pos[box] = "x"
        if box == 5:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (225, 175),(275, 125))
                pygame.draw.line(background, (0,0,0), (225, 125),(275, 175))
                pos[box] = "x"
        if box == 6:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (25, 275),(75, 225))
                pygame.draw.line(background, (0,0,0), (25, 225),(75, 275))
                pos[box] = "x"
        if box == 7:
            if pos[box] != "o":

                pygame.draw.line(background, (0,0,0), (125, 275),(175, 225))
                pygame.draw.line(background, (0,0,0), (125, 225),(175, 275))
                pos[box] = "x"
        if box == 8:
            if pos[box] != "o":
                pygame.draw.line(background, (0,0,0), (225, 275),(275, 225))
                pygame.draw.line(background, (0,0,0), (225, 225),(275, 275))
                pos[box] = "x"
                            


    if turn == "o":
        if box == 0:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (50,50), 25, 2)
                pos[box] = "o"
        if box == 1:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (150,50), 25, 2)
                pos[box] = "o"
        if box == 2:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (250,50), 25, 2)
                pos[box] = "o"
        if box == 3:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (50,150), 25, 2)
                pos[box] = "o"
        if box == 4:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (150,150), 25, 2)
                pos[box] = "o"
        if box == 5:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (250,150), 25, 2)
                pos[box] = "o"
        if box == 6:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (50,250), 25, 2)
                pos[box] = "o"
        if box == 7:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (150,250), 25, 2)
                pos[box] = "o"
        if box == 8:
            if pos[box] != "x":
                pygame.draw.circle(background, (0,0,0), (250,250), 25, 2)
                pos[box] = "o"

def checkwin():
    if pos[0] == pos[1] and pos[0] == pos[2] and pos[0] != 0:
        pygame.draw.line(background, (0,0,0), (0, 50),(300,50))
        win = "true"
        return win
    if pos[3] == pos[4] and pos[3] == pos[5] and pos[3] != 3:
        pygame.draw.line(background, (0,0,0), (0, 150),(300,150))
        win = "true"
        return win
    if pos[6] == pos[7] and pos[6] == pos[8] and pos[6] != 6:
        pygame.draw.line(background, (0,0,0), (0, 250),(300,250))
        win = "true"
        return win
    if pos[0] == pos[3] and pos[0] == pos[6] and pos[0] != 0:
        pygame.draw.line(background, (0,0,0), (50, 0),(50,300))
        win = "true"
        return win
    if pos[1] == pos[4] and pos[1] == pos[7] and pos[1] != 1:
        pygame.draw.line(background, (0,0,0), (150, 0),(150,300))
        win = "true"
        return win
    if pos[2] == pos[5] and pos[2] == pos[8] and pos[2] != 2:
        pygame.draw.line(background, (0,0,0), (250, 0),(250,300))
        win = "true"
        return win
    if pos[0] == pos[4] and pos[0] == pos[8] and pos[0] != 0:
        pygame.draw.line(background, (0,0,0), (0, 0),(300,300))
        win = "true"
        return win
    if pos[2] == pos[4] and pos[2] == pos[6] and pos[2] != 2:
        pygame.draw.line(background, (0,0,0), (0, 300),(300,0))
        win = "true"
        return win
    
       
    
                             
                
        

    

# Main game loop    


while 1:
            
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        gamestate = checkwin()
                  
        if gamestate == "true":
            freeze = 1
        elif gamestate != "true":
            freeze = 0
        if event.type == MOUSEBUTTONDOWN:
            if freeze == 0:
                x , y = pygame.mouse.get_pos()
                box = whichbox(x, y)
                drawmove(box)
                if turn == "x":
                    turn = "o"
                elif turn =="o":
                    turn = "x"       
                

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key ==K_r:
                pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                background.fill((255,255,255))
                freeze=0
                    
            







            


            
    pygame.draw.line(background,(0,0,0), (100,0),(100,300))
    pygame.draw.line(background,(0,0,0), (200,0),(200,300))
    pygame.draw.line(background,(0,0,0), (0,100),(300,100))
    pygame.draw.line(background,(0,0,0), (0,200),(300,200))
    screen.blit(background, (0,0))
    pygame.display.update()
