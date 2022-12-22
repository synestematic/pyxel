ESPADA = 1
BASTO  = 2
ORO    = 3
COPA   = 4

class Card:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

AnchoEspada = Card(ESPADA, 1)
DosEspada = Card(ESPADA, 2)
TresEspada = Card(ESPADA, 3)
CuatroEspada = Card(ESPADA, 4)
CincoEspada = Card(ESPADA, 5)
SeisEspada = Card(ESPADA, 6)
SieteEspada = Card(ESPADA, 7)
DonnaEspada = Card(ESPADA, 10)
CaballoEspada = Card(ESPADA, 11)
ReyEspada = Card(ESPADA, 12)

AnchoBasto = Card(BASTO, 1)
DosBasto = Card(BASTO, 2)
TresBasto = Card(BASTO, 3)
CuatroBasto = Card(BASTO, 4)
CincoBasto = Card(BASTO, 5)
SeisBasto = Card(BASTO, 6)
SieteBasto = Card(BASTO, 7)
DonnaBasto = Card(BASTO, 10)
CaballoBasto = Card(BASTO, 11)
ReyBasto = Card(BASTO, 12)

AnchoOro = Card(ORO, 1)
DosOro = Card(ORO, 2)
TresOro = Card(ORO, 3)
CuatroOro = Card(ORO, 4)
CincoOro = Card(ORO, 5)
SeisOro = Card(ORO, 6)
SieteOro = Card(ORO, 7)
DonnaOro = Card(ORO, 10)
CaballoOro = Card(ORO, 11)
ReyOro = Card(ORO, 12)

AnchoCopa = Card(COPA, 1)
DosCopa = Card(COPA, 2)
TresCopa = Card(COPA, 3)
CuatroCopa = Card(COPA, 4)
CincoCopa = Card(COPA, 5)
SeisCopa = Card(COPA, 6)
SieteCopa = Card(COPA, 7)
DonnaCopa = Card(COPA, 10)
CaballoCopa = Card(COPA, 11)
ReyCopa = Card(COPA, 12)


VALORES = (
    [AnchoEspada],
    [AnchoBasto],
    [SieteEspada],
    [SieteOro],
    [TresEspada, TresBasto, TresOro, TresCopa],
    [DosEspada, DosBasto, DosOro, DosCopa],
    [AnchoOro, AnchoCopa],
    [ReyEspada, ReyBasto, ReyOro, ReyCopa],
    [CaballoEspada, CaballoBasto, CaballoOro, CaballoCopa],
    [DonnaEspada, DonnaBasto, DonnaOro, DonnaCopa],
    [SieteBasto, SieteCopa],
    [SeisEspada, SeisBasto, SeisOro, SeisCopa],
    [CincoEspada, CincoBasto, CincoOro, CincoCopa],
    [CuatroEspada, CuatroBasto, CuatroOro, CuatroCopa],
)


