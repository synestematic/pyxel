import pyxel


def UpdateKeys():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


NETHERLANDS = {'u': 0, 'v': 0, 'w':16, 'h':16}
ARGENTINA = {'u': 0, 'v': 16, 'w':16, 'h':16}
CROATIA = {'u': 0, 'v': 32, 'w':16, 'h':16}
BRAZIL = {'u': 0, 'v': 48, 'w':16, 'h':16}

ENGLAND  = {'u': 48, 'v': 0, 'w':16, 'h':16}
FRANCE   = {'u': 48, 'v': 16, 'w':16, 'h':16}
MOROCCO = {'u': 48, 'v': 32, 'w':16, 'h':16}
PORTUGAL  = {'u': 48, 'v': 48, 'w':16, 'h':16}

LEFT_BRACKET = {'u': 16, 'v': 32, 'w':8, 'h':32}
RIGHT_BRACKET = {'u': 24, 'v': 32, 'w':8, 'h':32}

TROPHEY = {'u': 16, 'v': 12, 'w':12, 'h':20}

def partita1():
    pyxel.blt(img=0, x=6, y=6, **NETHERLANDS)
    pyxel.blt(img=0, x=6, y=30, **ARGENTINA)
    pyxel.blt(img=0, x=6+16+4, y=10, **LEFT_BRACKET)


def partita2():
    pyxel.blt(img=0, x=6, y=54, **CROATIA)
    pyxel.blt(img=0, x=6, y=78, **BRAZIL)
    pyxel.blt(img=0, x=6+16+4, y=58, **LEFT_BRACKET)


def partita3():
    pyxel.blt(img=0, x=200-6-16, y=6, **ENGLAND)
    pyxel.blt(img=0, x=200-6-16, y=6+24, **FRANCE)
    pyxel.blt(img=0, x=200-6-16-4-8, y=10, **RIGHT_BRACKET)


def partita4():
    pyxel.blt(img=0, x=200-6-16, y=6+48, **MOROCCO)
    pyxel.blt(img=0, x=200-6-16, y=6+48+24, **PORTUGAL)
    pyxel.blt(img=0, x=200-6-16-4-8, y=58, **RIGHT_BRACKET)



def DrawStuff():
    pyxel.cls(col=0)
    pyxel.text(x=51, y=4, s="FIFA WORLD CUP QATAR 2022", col=pyxel.frame_count % 16)
    pyxel.blt(img=0, x=200/2-TROPHEY['u']/2, y=14, **TROPHEY)
    partita1()
    partita2()
    partita3()
    partita4()



pyxel.init(width=200, height=100, title="Hello Pyxel")

# pyxel.image(0).load(0, 0, 'assets/pyxel_logo_38x16.png')

pyxel.load('assets/carumoon.pyxres')

pyxel.run(UpdateKeys, DrawStuff)
