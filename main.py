from constants import SQ_SIZE, WHITE, WIDTH, HEIGHT
from board import BLACK, Board
import pygame as p

p.init()

screen = p.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()

font = p.font.Font('freesansbold.ttf', 32)

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
    if board.winner != "N":
        if board.winner == "White":
            screen.fill(WHITE)
            text = font.render(f"{board.winner} is the winner", True, BLACK)
        else:
            screen.fill(BLACK)
            text = font.render(f"{board.winner} is the winner", True, WHITE)

        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
        p.display.update()
        p.time.wait(2000)
        p.quit()
        exit()

    screen.fill(WHITE)
    clock.tick(30)
