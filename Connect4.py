# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:04:55 2018

@author: Donghoon Raphael Han
"""

import numpy as np
import pygame
import sys

Num_Row = 6
Num_Col = 7

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
    
#def draw_board(board):
#    pass
    
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

board = create_board()
game_over = False
turn = 0
#
#pygame.init()
#
#box = 100
#width = Num_Col * box
#height = (Num_Row+1) * box
#
#size = (width, height)
#screen = pygame.display.set_mode(size)



while not game_over:
        
    if turn == 0:
        col = int(input("Player1 Selection (0-6): "))
        if check_location(board, col):
            row = next_row(board, col)
            drop(board, row, col, 1)
            
            if winning(board,1):
                print("Player1 wins!")
                game_over = True
    else:
        col = int(input("Player2 Selection (0-6): "))
        if check_location(board, col):
            row = next_row(board, col)
            drop(board, row, col, 2)
            
            if winning(board,2):
                print("Player2 wins!")
                game_over = True
    
    print_board(board)
    turn += 1
    turn = turn % 2
    
    