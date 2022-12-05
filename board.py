from constants import ROWS, COLS, SQ_SIZE, BLACK
import pygame as p
from piece import Piece

class Board:
    def __init__(self):
        self.board = [
                [Piece("R", "b", 0, 0), Piece("N", "b", 1, 0), Piece("B", "b", 2, 0), Piece("Q", "b", 3, 0), Piece("K", "b", 4, 0), Piece("B", "b", 5, 0), Piece("N", "b", 6, 0), Piece("R", "b", 7, 0)],
                [Piece("P", "b", 0, 1), Piece("P", "b", 1, 1), Piece("P", "b", 2, 1), Piece("P", "b", 3, 1), Piece("P", "b", 4, 1), Piece("P", "b", 5, 1), Piece("P", "b", 6, 1), Piece("P", "b", 7, 1)],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [Piece("P", "w", 0, 6), Piece("P", "w", 1, 6), Piece("P", "w", 2, 6), Piece("P", "w", 3, 6), Piece("P", "w", 4, 6), Piece("P", "w", 5, 6), Piece("P", "w", 6, 6), Piece("P", "w", 7, 6)],
                [Piece("R", "w", 0, 7), Piece("N", "w", 1, 7), Piece("B", "w", 2, 7), Piece("Q", "w", 3, 7), Piece("K", "w", 4, 7), Piece("B", "w", 5, 7), Piece("N", "w", 6, 7), Piece("R", "w", 7, 7)],
                ]
        self.selected = 0
        self.turn = "w"
        

    def draw_board(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (col+1) % 2 == (row) % 2:
                    p.draw.rect(screen, BLACK, (row*SQ_SIZE, col*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def draw_pieces(self, screen):
        for row in self.board:
            for piece in row:
                if piece != 0:
                    screen.blit(piece.img, piece.rect)

    def select(self, col, row):
        if self.selected != 0 and self.selected != None and (col, row) in self.selected.legal_moves and self.selected.colour == self.turn:
            # move the piece image
            # set its origional position to empty
            # move the piece
            self.move(self.selected, col, row)

        self.selected = self.board[row][col]

    def move(self,piece, col, row, switch=True):
        piece.rect.center = (col*SQ_SIZE +SQ_SIZE//2, row*SQ_SIZE +SQ_SIZE//2)
        self.board[piece.row][piece.col] = 0
        if piece.name == "K":
            # short castle
            if col - piece.col == 2:
                switch = False
                self.move(self.board[row][col+1], col-1, row, switch)
                switch = True
            # long castle
            elif col - piece.col == -2:
                switch = False
                self.move(self.board[row][col-2], col+1, row, switch)
                switch = True
        self.board[row][col] = piece
        self.board[row][col].row, self.board[row][col].col = row, col
        self.board[row][col].moved = True
        if switch:
            self.switch_turn()

    def switch_turn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"

    def get_all_valid_moves(self):
        for row in self.board:
            for each in row:
                if each != 0 and each != None:
                    each = self.get_legal_moves(each)
    
    def get_legal_moves(self, piece):
        col = piece.col
        row = piece.row
        colour = piece.colour
        name = piece.name
        mult = 1
        piece.legal_moves = []
        # if colour != self.turn:
        #     return
        #

        # pawn
        if name == "P":
            if colour == "w":
                direction = -1
            else:
                direction = 1
            
            if row + direction != 8 and row + direction != -1:
                if self.board[row + direction][col] == 0:
                    piece.legal_moves.append((col, row + direction))
                    if self.board[row + 2*direction][col] == 0 and piece.moved == False:
                        piece.legal_moves.append((col, row + 2*direction))
                if col + 1 != 8:
                    if self.board[row + direction][col + 1] != 0 and self.board[row + direction][col + 1].colour != colour:
                        piece.legal_moves.append((col+1, row+direction))
                if col -1 != -1:
                    if self.board[row + direction][col - 1] != 0 and self.board[row + direction][col - 1].colour != colour:
                        piece.legal_moves.append((col-1, row+direction))


        # bishop
        if name == "B":
            while True:
                if row+1*mult == 8 or col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row+1*mult][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1 or col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row-1*mult][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row+1*mult == 8 or col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row+1*mult][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1 or col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row-1*mult][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break


        # knight
        if name == "N":
            if not(row + 2 >= 8) and col + 1 != 8:
                if self.board[row+2][col+1] == 0 or self.board[row+2][col+1].colour != colour:
                    piece.legal_moves.append((col+1, row+2))
            if not(row + 2 >= 8) and col - 1 != -1:
                if self.board[row+2][col-1] == 0 or self.board[row+2][col-1].colour != colour:
                    piece.legal_moves.append((col-1, row+2))
        
            if not(row - 2 <= -1) and col + 1 != 8:
                if self.board[row-2][col+1] == 0 or self.board[row-2][col+1].colour != colour:
                    piece.legal_moves.append((col+1, row-2))
            if not(row - 2 <= -1) and col - 1 != -1:
                if self.board[row-2][col-1] == 0 or self.board[row-2][col-1].colour != colour:
                    piece.legal_moves.append((col-1, row-2))

            if not(col + 2 >= 8) and row + 1 != 8:
                if self.board[row+1][col+2] == 0 or self.board[row+1][col+2].colour != colour:
                    piece.legal_moves.append((col+2, row+1))
            if not(col + 2 >= 8) and row - 1 != -1:
                if self.board[row-1][col+2] == 0 or self.board[row-1][col+2].colour != colour:
                    piece.legal_moves.append((col+2, row-1))
        
            if not(col - 2 <= -1) and row + 1 != 8:
                if self.board[row+1][col-2] == 0 or self.board[row+1][col-2].colour != colour:
                    piece.legal_moves.append((col-2, row+1))
            if not(col - 2 <= -1) and row - 1 != -1:
                if self.board[row-1][col-2] == 0 or self.board[row-1][col-2].colour != colour:
                    piece.legal_moves.append((col-2, row-1))

        # rook
        if name == "R":
            while True:
                if row+1*mult == 8:
                    mult = 1
                    break
                if self.board[row+1*mult][col] == 0:
                    piece.legal_moves.append((col, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col].colour != colour:
                    piece.legal_moves.append((col, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1:
                    mult = 1
                    break
                if self.board[row-1*mult][col] == 0:
                    piece.legal_moves.append((col, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col].colour != colour:
                    piece.legal_moves.append((col, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row))
                    mult += 1
                elif self.board[row][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row))
                    mult += 1
                elif self.board[row][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

        # queen
        if name == "Q":
            while True:
                if row+1*mult == 8:
                    mult = 1
                    break
                if self.board[row+1*mult][col] == 0:
                    piece.legal_moves.append((col, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col].colour != colour:
                    piece.legal_moves.append((col, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1:
                    mult = 1
                    break
                if self.board[row-1*mult][col] == 0:
                    piece.legal_moves.append((col, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col].colour != colour:
                    piece.legal_moves.append((col, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row))
                    mult += 1
                elif self.board[row][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row))
                    mult += 1
                elif self.board[row][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row+1*mult == 8 or col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row+1*mult][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1 or col+1*mult == 8:
                    mult = 1
                    break
                if self.board[row-1*mult][col+1*mult] == 0:
                    piece.legal_moves.append((col+1*mult, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col+1*mult].colour != colour:
                    piece.legal_moves.append((col+1*mult, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row+1*mult == 8 or col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row+1*mult][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row+1*mult))
                    mult += 1
                elif self.board[row+1*mult][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row+1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

            while True:
                if row-1*mult == -1 or col-1*mult == -1:
                    mult = 1
                    break
                if self.board[row-1*mult][col-1*mult] == 0:
                    piece.legal_moves.append((col-1*mult, row-1*mult))
                    mult += 1
                elif self.board[row-1*mult][col-1*mult].colour != colour:
                    piece.legal_moves.append((col-1*mult, row-1*mult))
                    mult = 1
                    break
                else:
                    mult = 1
                    break

        # king
        if name == "K":
            if row + 1 != 8:
                if self.board[row+1][col] == 0:
                    piece.legal_moves.append((col, row+1))

                elif self.board[row+1][col].colour != colour:
                    piece.legal_moves.append((col, row+1))

            if row - 1 != -1:
                if self.board[row-1][col] == 0:
                    piece.legal_moves.append((col, row-1*mult))

                elif self.board[row-1][col].colour != colour:
                    piece.legal_moves.append((col, row-1))

            if col + 1 != 8:
                if self.board[row][col+1] == 0:
                    piece.legal_moves.append((col+1, row))

                elif self.board[row][col+1].colour != colour:
                    piece.legal_moves.append((col+1, row))
            
            if col - 1 != -1:
                if self.board[row][col-1] == 0:
                    piece.legal_moves.append((col-1, row))

                elif self.board[row][col-1].colour != colour:
                    piece.legal_moves.append((col-1, row))

            
            if row + 1 != 8 and col + 1 != 8:
                if self.board[row+1][col+1] == 0:
                    piece.legal_moves.append((col+1, row+1))

                elif self.board[row+1][col+1].colour != colour:
                    piece.legal_moves.append((col+1, row+1))
            
            if row - 1 != -1 and col + 1 != 8:
                if self.board[row-1][col+1] == 0:
                    piece.legal_moves.append((col+1, row-1))

                elif self.board[row-1][col+1].colour != colour:
                    piece.legal_moves.append((col+1, row-1))

            if row + 1 != 8 and col - 1 != -1:
                if self.board[row+1][col-1] == 0:
                    piece.legal_moves.append((col-1, row+1))

                elif self.board[row+1][col-1].colour != colour:
                    piece.legal_moves.append((col-1, row+1))

            if row - 1 != -1 and col - 1 != -1:
                if self.board[row-1][col-1] == 0:
                    piece.legal_moves.append((col-1, row-1))

                elif self.board[row-1][col-1].colour != colour:
                    piece.legal_moves.append((col-1, row-1))

            # castleing
            # short side
            no_castle = False
            if not piece.moved and self.board[row][col+3] != 0 and self.board[row][col+3].name == "R":
                if not self.board[row][col+3].moved:
                    if self.board[row][col+1] == 0 and self.board[row][col+2] == 0:
                        for r in self.board:
                            for each in r:
                                if each != 0 and each != None and each.colour != piece.colour:
                                    if (col, row) in each.legal_moves or (col+1, row) in each.legal_moves or (col+2, row) in each.legal_moves or (col+3, row) in each.legal_moves:
                                        no_castle = True
                                        break
                                    
                            if no_castle:
                                break
                        if not no_castle:
                            piece.legal_moves.append((col+2, row))
            # long side
            no_castle = False
            if not piece.moved and self.board[row][col-4] != 0 and self.board[row][col-4].name == "R":
                if not self.board[row][col-4].moved:
                    if self.board[row][col-1] == 0 and self.board[row][col-2] == 0 and self.board[row][col-3] == 0:
                        for r in self.board:
                            for each in r:
                                if each != 0 and each != None:
                                    if (col, row) in each.legal_moves or (col-1, row) in each.legal_moves or (col-2, row) in each.legal_moves or (col-3, row) in each.legal_moves or (col-4, row) in each.legal_moves:
                                        no_castle = True
                                        break
                        if not no_castle:
                            piece.legal_moves.append((col-2, row))
        return piece
