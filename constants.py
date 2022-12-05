import pygame as p

# numbers
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQ_SIZE = HEIGHT//ROWS

# colours
BLACK = (128, 128, 128)
WHITE = (255, 255, 255)

SIZE = (75, 75)

wP = p.transform.scale(p.image.load("Assets/wP.png"), SIZE)
wN = p.transform.scale(p.image.load("Assets/wN.png"), SIZE)
wB = p.transform.scale(p.image.load("Assets/wB.png"), SIZE)
wR = p.transform.scale(p.image.load("Assets/wR.png"), SIZE)
wQ = p.transform.scale(p.image.load("Assets/wQ.png"), SIZE)
wK = p.transform.scale(p.image.load("Assets/wK.png"), SIZE)

bP = p.transform.scale(p.image.load("Assets/bP.png"), SIZE)
bN = p.transform.scale(p.image.load("Assets/bN.png"), SIZE)
bB = p.transform.scale(p.image.load("Assets/bB.png"), SIZE)
bR = p.transform.scale(p.image.load("Assets/bR.png"), SIZE)
bQ = p.transform.scale(p.image.load("Assets/bQ.png"), SIZE)
bK = p.transform.scale(p.image.load("Assets/bK.png"), SIZE)
