'''

'''

import pyxel

from cartas import *

SIDE_MARGIN = 6
SMALL_SPACE = 4

TOTAL_WIDTH = 200
TOTAL_HEIGHT = 100

META_SCHERMO = TOTAL_WIDTH / 2

BG = 0

TITLE = 'TRUCO ARGENTINO'


def UpdateKeys():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def DrawStuff():
    pyxel.cls(col=BG)
    pyxel.text(
        x=51, y=TOTAL_HEIGHT-9, s=TITLE, col=pyxel.frame_count % 16
    )


pyxel.init(width=TOTAL_WIDTH, height=TOTAL_HEIGHT, title=TITLE)
pyxel.load('assets/truco.pyxres')
pyxel.run(UpdateKeys, DrawStuff)
