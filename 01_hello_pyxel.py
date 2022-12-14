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
LEFT_BRACKET_BIG = {'u': 32, 'v': 16, 'w':8, 'h':48}

RIGHT_BRACKET = {'u': 24, 'v': 32, 'w':8, 'h':32}
RIGHT_BRACKET_BIG = {'u': 40, 'v': 16, 'w':8, 'h':48}

UP_BRACKET = {'u': 32, 'v': 0, 'w':16, 'h':4}

TROPHEY = {'u': 16, 'v': 12, 'w':12, 'h':20}

SPAZIO_LATERALE = 6
SMALL_SPACE = 4

WIDTH_FLAG = 16
WIDTH_TOTALE = 200
HEIGHT_TOTALE = 100

META_SCHERMO = WIDTH_TOTALE / 2

BG = 0

def QuartoFinaleSinistra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    teams_x = SPAZIO_LATERALE
    brack_x = teams_x + WIDTH_FLAG + SMALL_SPACE
    score_x = brack_x + LEFT_BRACKET['w']
    pyxel.blt(**team1, img=0, x=teams_x, y=quanto_in_giu)
    pyxel.blt(**team2, img=0, x=teams_x, y=quanto_in_giu+24)
    pyxel.blt(**LEFT_BRACKET, img=0, x=brack_x, y=quanto_in_giu+4)
    pyxel.text(s=str(goals1), x=score_x, y=quanto_in_giu+5, col=15)
    pyxel.text(s=str(goals2), x=score_x, y=quanto_in_giu+30, col=15)
    return winner


def QuartoFinaleDestra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    teams_x = WIDTH_TOTALE - SPAZIO_LATERALE - WIDTH_FLAG
    brack_x = teams_x - SMALL_SPACE - RIGHT_BRACKET['w']
    score_x = brack_x - SMALL_SPACE
    pyxel.blt(**team1, img=0, x=teams_x, y=quanto_in_giu)
    pyxel.blt(**team2, img=0, x=teams_x, y=quanto_in_giu+24)
    pyxel.blt(**RIGHT_BRACKET, img=0, x=brack_x, y=quanto_in_giu+4)
    pyxel.text(s=str(goals1), x=score_x, y=quanto_in_giu+5, col=15)
    pyxel.text(s=str(goals2), x=score_x, y=quanto_in_giu+30, col=15)
    return winner


def SemiFinaleSinistra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    teams_x = SPAZIO_LATERALE + WIDTH_FLAG + SMALL_SPACE + LEFT_BRACKET['w'] + SMALL_SPACE
    brack_x = teams_x + WIDTH_FLAG + SMALL_SPACE
    score_x = brack_x + LEFT_BRACKET['w']
    pyxel.blt(**team1, img=0, x=teams_x, y=quanto_in_giu+12)
    pyxel.blt(**team2, img=0, x=teams_x,  y=quanto_in_giu+12+48)
    pyxel.blt(**LEFT_BRACKET_BIG, img=0, x=brack_x, y=quanto_in_giu+20)
    pyxel.text(s=str(goals1), x=score_x, y=quanto_in_giu+5+12, col=15)
    pyxel.text(s=str(goals2), x=score_x, y=quanto_in_giu+5+12+LEFT_BRACKET_BIG['h'], col=15)
    return winner


def SemiFinaleDestra(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    teams_x = WIDTH_TOTALE - SPAZIO_LATERALE - WIDTH_FLAG - (SMALL_SPACE + RIGHT_BRACKET['w'] + SMALL_SPACE) * 2
    brack_x = teams_x - SMALL_SPACE - RIGHT_BRACKET['w']
    score_x = brack_x - SMALL_SPACE
    pyxel.blt(**team1, img=0, x=teams_x, y=quanto_in_giu+12)
    pyxel.blt(**team2, img=0, x=teams_x,  y=quanto_in_giu+12+48)
    pyxel.blt(**RIGHT_BRACKET_BIG, img=0, x=brack_x, y=quanto_in_giu+20)
    pyxel.text(s=str(goals1), x=score_x, y=quanto_in_giu+5+12, col=15)
    pyxel.text(s=str(goals2), x=score_x, y=quanto_in_giu+5+12+LEFT_BRACKET_BIG['h'], col=15)
    return winner


def Finale(team1, team2, quanto_in_giu):
    team1, goals1 = team1
    team2, goals2 = team2
    if goals1 > goals2:
        winner = team1
    if goals2 > goals1:
        winner = team2
    pyxel.blt(**team1, img=0, x=META_SCHERMO-29, y=quanto_in_giu)
    pyxel.blt(**team2, img=0, x=META_SCHERMO+13, y=quanto_in_giu)
    pyxel.blt(
        **UP_BRACKET, img=0,
        x=WIDTH_TOTALE/2-UP_BRACKET['w']/2,
        y=quanto_in_giu+4
    )
    pyxel.text(s=str(goals1), x=META_SCHERMO-10, y=quanto_in_giu+12, col=15)
    pyxel.text(s=str(goals2), x=META_SCHERMO+8 , y=quanto_in_giu+12, col=15)
    return winner


def Champion(team):
    pyxel.blt(**team, img=0, x=META_SCHERMO-WIDTH_FLAG/2, y=22)


def DrawStuff():
    pyxel.cls(col=BG)
    pyxel.blt(img=0, x=WIDTH_TOTALE/2-TROPHEY['u']/2+1, y=68, **TROPHEY)
    pyxel.text(
        x=51, y=HEIGHT_TOTALE-9, s="FIFA WORLD CUP QATAR 2022", col=pyxel.frame_count % 16
    )

    ####################
    # QUARTI DI FINALE #
    ####################

    WINNER_QF1 = QuartoFinaleSinistra(
        team1=[NETHERLANDS, 5],
        team2=[ARGENTINA, 6],
        quanto_in_giu=SPAZIO_LATERALE
    )

    WINNER_QF2 = QuartoFinaleSinistra(
        team1=[CROATIA, 5],
        team2=[BRAZIL, 3],
        quanto_in_giu=SPAZIO_LATERALE+48
    )

    WINNER_QF3 = QuartoFinaleDestra(
        team1=[ENGLAND, 1],
        team2=[FRANCE, 2],
        quanto_in_giu=SPAZIO_LATERALE
    )

    WINNER_QF4 = QuartoFinaleDestra(
        team1=[MOROCCO, 1],
        team2=[PORTUGAL, 0],
        quanto_in_giu=SPAZIO_LATERALE+48
    )


    ###############
    # SEMI FINALI #
    ###############

    WINNER_SF1 = SemiFinaleSinistra(
        team1=[WINNER_QF1, 3],  # Argentina
        team2=[WINNER_QF2, 0],  # Croatia
        quanto_in_giu=SPAZIO_LATERALE
    )

    WINNER_SF2 = SemiFinaleDestra(
        team1=[WINNER_QF3, 2],  # France
        team2=[WINNER_QF4, 0],  # Morocco
        quanto_in_giu=SPAZIO_LATERALE
    )


    ##########
    # FINALE #
    ##########

    WINNER_FINAL = Finale(
        team1=[WINNER_SF1, 7],  # Argentina
        team2=[WINNER_SF2, 5],  # France
        quanto_in_giu=42
    )

    Champion(WINNER_FINAL)




pyxel.init(width=WIDTH_TOTALE, height=HEIGHT_TOTALE, title="QATAR WORLD CUP")
# pyxel.image(0).load(0, 0, 'assets/pyxel_logo_38x16.png')
pyxel.load('assets/carumoon.pyxres')
pyxel.run(UpdateKeys, DrawStuff)
