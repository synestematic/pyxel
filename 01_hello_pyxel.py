'''

'''

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

SPAZIO_LATERALE = 6
SMALL_SPACE = 4

WIDTH_FLAG = 16
WIDTH_TOTALE = 200
HEIGHT_TOTALE = 100


def QuartoFinaleSinistra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    pyxel.blt(**team1, img=0, x=SPAZIO_LATERALE, y=quanto_in_giu)
    pyxel.blt(**team2, img=0, x=SPAZIO_LATERALE, y=quanto_in_giu+24)
    pyxel.blt(
        **LEFT_BRACKET, img=0,
        x=SPAZIO_LATERALE+WIDTH_FLAG+SMALL_SPACE,
        y=quanto_in_giu+4
    )
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    pyxel.text(
        s=str(goals1),
        x=SPAZIO_LATERALE+WIDTH_FLAG+LEFT_BRACKET['w']+SMALL_SPACE,
        y=quanto_in_giu+5,
        col=15
    )
    pyxel.text(
        s=str(goals2),
        x=SPAZIO_LATERALE+WIDTH_FLAG+LEFT_BRACKET['w']+SMALL_SPACE,
        y=quanto_in_giu+30,
        col=15
    )
    pyxel.blt(
        **winner, img=0,
        x=SPAZIO_LATERALE+WIDTH_FLAG+LEFT_BRACKET['w']+SMALL_SPACE+SMALL_SPACE,
        y=quanto_in_giu+12,
    )


def QuartoFinaleDestra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    pyxel.blt(**team1, img=0, x=WIDTH_TOTALE-SPAZIO_LATERALE-WIDTH_FLAG, y=quanto_in_giu)
    pyxel.blt(**team2, img=0, x=WIDTH_TOTALE-SPAZIO_LATERALE-WIDTH_FLAG, y=quanto_in_giu+24)
    pyxel.blt(
        **RIGHT_BRACKET, img=0,
        x=WIDTH_TOTALE-SPAZIO_LATERALE-WIDTH_FLAG-SMALL_SPACE-RIGHT_BRACKET['w'],
        y=quanto_in_giu+4,
    )
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    pyxel.text(
        s=str(goals1),
        x=WIDTH_TOTALE-SPAZIO_LATERALE-SMALL_SPACE-RIGHT_BRACKET['w']-WIDTH_FLAG-2,
        y=quanto_in_giu+5,
        col=15
    )
    pyxel.text(
        s=str(goals2),
        x=WIDTH_TOTALE-SPAZIO_LATERALE-SMALL_SPACE-RIGHT_BRACKET['w']-WIDTH_FLAG-2,
        y=quanto_in_giu+30,
        col=15
    )
    pyxel.blt(
        **winner, img=0,
        x=WIDTH_TOTALE-SPAZIO_LATERALE-WIDTH_FLAG-SMALL_SPACE-RIGHT_BRACKET['w']-WIDTH_FLAG-SMALL_SPACE,
        y=quanto_in_giu+12,
    )






def DrawStuff():
    pyxel.cls(col=0)
    pyxel.text(x=51, y=4, s="FIFA WORLD CUP QATAR 2022", col=pyxel.frame_count % 16)
    pyxel.blt(img=0, x=WIDTH_TOTALE/2-TROPHEY['u']/2, y=12, **TROPHEY)

    QuartoFinaleSinistra(
        team1=[NETHERLANDS, 5],
        team2=[ARGENTINA, 6],
        quanto_in_giu=SPAZIO_LATERALE
    )

    QuartoFinaleSinistra(
        team1=[CROATIA, 5],
        team2=[BRAZIL, 3],
        quanto_in_giu=SPAZIO_LATERALE+48
    )

    QuartoFinaleDestra(
        team1=[ENGLAND, 1],
        team2=[FRANCE, 2],
        quanto_in_giu=SPAZIO_LATERALE
    )

    QuartoFinaleDestra(
        team1=[MOROCCO, 1],
        team2=[PORTUGAL, 0],
        quanto_in_giu=SPAZIO_LATERALE+48
    )





pyxel.init(width=WIDTH_TOTALE, height=HEIGHT_TOTALE, title="Hello Pyxel")
# pyxel.image(0).load(0, 0, 'assets/pyxel_logo_38x16.png')
pyxel.load('assets/carumoon.pyxres')
pyxel.run(UpdateKeys, DrawStuff)
