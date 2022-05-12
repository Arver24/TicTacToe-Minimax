import random

import pygame as pg
import numpy as np
from zmq import NULL


# assuming X to be human and O to be computer and human plays first


pg.init()
w = 600
h = 600
frame = pg.display.set_mode(size=(w, h))
white = (255, 255, 255)
red=(255,0,0)
players = ["X", "O"]
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
currPlayer = players[0]       # players[np.random.randint(0, 2)]
running = True
isWon=False
print("starting with ", currPlayer)

# nos are hard coded, found no other solution
def DrawX(posX, posY):
    posX *= 200
    posY *= 200
    startX = posX + 50
    startY = posY + 50
    endX = posX + 150
    endY = posY + 150
    pg.draw.line(frame, white, (startX, startY), (endX, endY))
    pg.draw.line(frame, white, (endX, startY), (startX, endY))


def DrawO(posX, posY):
    posX *= 200
    posY *= 200
    cX = posX + 100
    cY = posY + 100
    pg.draw.circle(frame, white, (cX, cY), 50, 1)



while running:
    event = pg.event.wait()
    if event.type == pg.QUIT:
        break
    else:
        pg.display.update()
        # horizontal lines

        pg.draw.line(frame, white, (w / 3, 0), (w / 3, h))
        pg.draw.line(frame, white, (2 * w / 3, 0), (2 * w / 3, h))

        # vertical lines

        pg.draw.line(frame, white, (0, h / 3), (w, h / 3))
        pg.draw.line(frame, white, (0, 2 * h / 3), (w, 2 * h / 3))

        # mouse click detection

        if not isWon:
            # only detect mouse click if game is not over
            i=np.random.randint(0,3)
            j=np.random.randint(0,3)
            if event.type == pg.MOUSEBUTTONUP:
                mouseX = pg.mouse.get_pos()[0]
                mouseY = pg.mouse.get_pos()[1]

                # board and screen connecting logic

                newMouseX = int(mouseX / 200)
                newMouseY = int(mouseY / 200)
                
                if board[newMouseY][newMouseX] == " ":

                    # X moves
                    if currPlayer == "X":
                        board[newMouseY][newMouseX] = "X"
                        currPlayer = "O"
                        DrawX(newMouseX, newMouseY)

                    # O moves

                    else:
                        print("Computer's Turn")

            if (board[i][j]==" ") and currPlayer=="O":
                            board[i][j] = "O"
                            currPlayer = "X"
                            DrawO(j, i)
            else:
                print("Human's turn")

            # winning conditions

            # horizontal


            if board[0][0] == board[0][1] == board[0][2] != " ":
                isWon=True
                pg.draw.line(frame,red,(50,100),(550,100))

            if board[1][0] == board[1][1] == board[1][2] != " ":
                isWon=True
                pg.draw.line(frame,red,(50,300),(550,300))
            if board[2][0] == board[2][1] == board[2][2] != " ":
                isWon=True
                pg.draw.line(frame,red,(50,500),(550,500))


            # vertical


            if board[0][0] == board[1][0] == board[2][0] != " ":
                isWon=True
                pg.draw.line(frame,red,(100,50),(100,550))
            if board[0][1] == board[1][1] == board[2][1] != " ":
                isWon=True
                pg.draw.line(frame,red,(300,50),(300,550))
            if board[0][2] == board[1][2] == board[2][2] != " ":
                isWon=True
                pg.draw.line(frame,red,(500,50),(500,550))


            # diagonal


            if board[0][0] == board[1][1] == board[2][2] != " ":
                isWon=True
                pg.draw.line(frame,red,(50,50),(550,550))
            if board[0][2] == board[1][1] == board[2][0] != " ":
                isWon=True
                pg.draw.line(frame,red,(550,50),(50,550))
            
            # Win line is currently hardcoded, will have to find a mathematical relation to replace the hardcode


            for i in range(len(board)):
                for j in range(len(board[i])):
                    if not isWon and (board[0].count("X")+board[1].count("X")+board[2].count("X"))==5:
                        
                        print("!!!  Game Draw  !!!")
                        pg.display.update()
                        pg.time.delay(100)
                        running=False
                        

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end="")
        
    print()
