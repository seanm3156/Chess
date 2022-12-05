import pygame as p
from constants import *

class Piece:
    def __init__(self, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.row = row
        self.col = col
        self.moved = False
        self.legal_moves = []
        
        match self.colour + self.name:
            case 'bP':
                self.img = bP
            case 'bN':
                self.img = bN
            case 'bB':
                self.img = bB 
            case 'bR':
                self.img = bR
            case 'bQ':
                self.img = bQ
            case 'bK':
                self.img = bK
            case 'wP':
                self.img = wP
            case 'wN':
                self.img = wN
            case 'wB':
                self.img = wB
            case 'wR':
                self.img = wR
            case 'wQ':
                self.img = wQ
            case 'wK':
                self.img = wK

        self.rect = self.img.get_rect(center = (self.col * SQ_SIZE + SQ_SIZE//2, self.row *SQ_SIZE + SQ_SIZE//2))
    def __repr__(self) -> str:
        return self.colour + self.name
