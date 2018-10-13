# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:04:55 2018

@author: Donghoon Raphael Han
"""

import numpy as np
import pygame
import math

Num_Row = 6
Num_Col = 7
Blue = (0,0,255)
Black = (0,0,0)
Red = (255,0,0)
Yellow = (255,255,0)
White = (255,255,255)
Green = (0,255,0)

def create_board():
    board = np.zeros((Num_Row,Num_Col))
    return board

def drop(board, row, col, piece):
    board[row][col] = piece

def check_location(board, col):
    return board[Num_Row-1][col] == 0

def next_row(board, col):
    for i in range(Num_Row):
        if board[i][col] == 0:
            return i
        
def print_board(board):
    print(np.flip(board, 0))
    
def draw_board(board):
    for i in range(Num_Col):
        for j in range(Num_Row):
            pygame.draw.rect(screen, Blue, (i*box, j*box+box, box, box))
            pygame.draw.circle(screen, Black, (int(i*box+box/2), int(j*box+box+box/2) ),radius)
                
    for i in range(Num_Col):
        for j in range(Num_Row):
            if board[j][i] == 1:
                pygame.draw.circle(screen, Red, (int(i*box+box/2), height - int(j*box+box/2) ),radius)
            elif board[j][i] == 2:
                pygame.draw.circle(screen, Yellow, (int(i*box+box/2), height - int(j*box+box/2) ),radius)
    pygame.display.update()

    
def winning(board, piece):
    for i in range(Num_Col-3): #last 3 is not gonna work (horizontal)
        for j in range(Num_Row):
            if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
                return True
    
    for i in range(Num_Col): #last 3 is not gonna work (vertical)
        for j in range(Num_Row-3):
            if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
                return True
            
    for i in range(Num_Col-3): #last 3 is not gonna work (positive diagonal)
        for j in range(Num_Row-3):
            if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
                return True
            
    for i in range(Num_Col-3): #last 3 is not gonna work (negative diagonal)
        for j in range(3, Num_Row):
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
                return True

def winning_draw(board,piece):
    for i in range(Num_Col-3):
        for j in range(Num_Row):
            if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
                pygame.draw.line(screen,Green,[int(i*box+box/2),height - int(j*box+box/2)],[int((i+3)*box+box/2),height - int(j*box+box/2)],10)
    
    for i in range(Num_Col):
        for j in range(Num_Row-3):
            if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
                pygame.draw.line(screen,Green,[int(i*box+box/2),height - int(j*box+box/2)],[int(i*box+box/2),height - int((j+3)*box+box/2)],10)          
    
    for i in range(Num_Col-3): 
        for j in range(Num_Row-3):
            if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
                pygame.draw.line(screen,Green,[int(i*box+box/2),height - int(j*box+box/2)],[int((i+3)*box+box/2),height - int((j+3)*box+box/2)],10)
                
    for i in range(Num_Col-3):
        for j in range(3, Num_Row):
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
                pygame.draw.line(screen,Green,[int(i*box+box/2),height - int(j*box+box/2)],[int((i+3)*box+box/2),height - int((j-3)*box+box/2)],10)
    
    pygame.display.update()
    
board = create_board()
game_over = False
turn = 0

pygame.init()

box = 100
width = Num_Col * box
height = (Num_Row+1) * box

size = (width, height)
radius = int(box/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.Font('freesansbold.ttf',80)

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, Black, (0,0, width, box))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, Red, (posx,int(box/2)),radius)
            else:
                pygame.draw.circle(screen, Yellow, (posx,int(box/2)),radius)
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
#            print(event.pos)
            pygame.draw.rect(screen, Black, (0,0, width, box))
            
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/box))
                if check_location(board, col):
                    row = next_row(board, col)
                    drop(board, row, col, 1)
                    
                    if winning(board,1):
                        label = myfont.render("Player1 wins!!",1,White)
                        screen.blit(label,(65,10))
                        print("Player1 wins!")
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/box))
                if check_location(board, col):
                    row = next_row(board, col)
                    drop(board, row, col, 2)
                    
                    if winning(board,2):
                        label = myfont.render("Player2 wins!!",1,White)
                        pygame.display.update()
                        screen.blit(label,(65,10))
                        print("Player2 wins!")
                        game_over = True
            
            print_board(board)
            draw_board(board)
            
            turn += 1
            turn = turn % 2
            if game_over:
                winning_draw(board,1)
                winning_draw(board,2)
                pygame.time.wait(5000)
                pygame.quit()
                quit()
            
    