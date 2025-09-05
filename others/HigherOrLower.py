#Juego de cartas Higher or Lower
import random

#Constantes
RANGO_CARTA = ('Diamantes', 'Picas', 'Treboles', 'Naipes')
VALOR_CARTA = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bofon', 'Reyna', 'Rey')
N_CARTAS = 8

def ObtenerCarta(BarajaListIn): 
    CartaActual = BarajaListIn.pop()
    return CartaActual

def Barajear(BarajaListaIn):
    BarajaListaOut = BarajaListaIn.copy()
    random.shuffle(BarajaListaOut)
    return BarajaListaOut

print("Inicia el juego")
print("Tu puntuacion inicial es de 50")
print("Si aciertas tu puntuacion aumenta en 20")
print("De lo contrario tu puntuacion disminuye en 15")

BarajaInicialList = []
for suit in RANGO_CARTA:
    for ValorActual, rank in enumerate(VALOR_CARTA):
        ValorCarta = {'rank':rank, 'suit':suit,'value':ValorActual + 1}
        BarajaInicialList.append(ValorCarta)

puntuacion = 50

while True:
    print()
    BarajaJuegoList = Barajear(BarajaInicialList)
    currenteCardDic = ObtenerCarta(BarajaJuegoList)
    currentRankCard = currenteCardDic['rank']
    currentSuitCard = currenteCardDic['suit']
    currentValueCard = currenteCardDic['value']
    print('Tu carta inicial es: ', currentRankCard + ' de ', currentSuitCard)
    print()

    for numCarta in range(0, N_CARTAS):
        respuesta = input('La siguiente carta sera mas grande o pequeña que ' + currentRankCard + ' de ' + currentSuitCard + '? (Escribe G o P)')
        respuesta = respuesta.casefold()
        nextDictCard = ObtenerCarta(BarajaJuegoList)
        nextRankCard = nextDictCard['rank']
        nextSuitCard = nextDictCard['suit']
        nextValueCard = nextDictCard['value']
        print('La nueva carta es: ' + nextRankCard + ' de ' + nextSuitCard)

        if respuesta == 'g':
            if nextValueCard > currentValueCard:
                print("Correcto, era mas grande\n")
                puntuacion = puntuacion + 20
            else:
                print("Lo siento, era mas pequeña\n")
                puntuacion = puntuacion - 15
        elif respuesta == 'p':
            if nextValueCard < currentValueCard:
                print("Correcto, era mas pequeña\n")
                puntuacion = puntuacion + 20
            else:
                print("Lo siento, era mas grande\n")
                puntuacion = puntuacion - 15

        print("Tu puntuacion actual es: ", + puntuacion)
        currentRankCard = nextRankCard
        currentValueCard = nextValueCard
        reiniciar = input("Presiona Enter para seguir jugando o preciona 'Q' para salir")
        print()

        reiniciar = reiniciar.casefold()
        if reiniciar == 'q':
            print("Hasta luego")
            break

    if puntuacion < 1:
            print("Se te acabaron los puntos\n")
            print("FIN DEL JUEGO")
            break
    