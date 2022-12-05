from constants import SQ_SIZE, WHITE, WIDTH, HEIGHT
from board import Board
import pygame as p

p.init()

screen = p.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()

def draw_legal_moves(screen):
    if board.selected != 0 and board.selected != None and board.selected.colour == board.turn:
        for move in board.selected.legal_moves:
            col, row = move
            x, y = col * SQ_SIZE + SQ_SIZE//2, row * SQ_SIZE + SQ_SIZE//2
            p.draw.circle(screen, "Red", (x, y), 15)

board = Board()
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()

        if event.type == p.MOUSEBUTTONDOWN:
            x, y = p.mouse.get_pos()
            col, row = x//SQ_SIZE, y//SQ_SIZE
            board.select(col, row)
    
    board.get_all_valid_moves()
    board.draw_board(screen)
    board.draw_pieces(screen)
    draw_legal_moves(screen)


    p.display.update()

    screen.fill(WHITE)
    clock.tick(30)
