import pyxel


def UpdateKeys():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def DrawStuff():
    pyxel.cls(col=0)
    pyxel.text(x=55, y=41, s="Hello Pyxel!", col=pyxel.frame_count % 16)
    pyxel.blt(img=0, x=61, y=66, w=16, h=16, u=0, v=0)


pyxel.init(width=160, height=120, title="Hello Pyxel")
pyxel.image(0).load(0, 0, 'assets/pyxel_logo_38x16.png')
pyxel.run(UpdateKeys, DrawStuff)
