from math import sqrt


def distancia(branca, bolan):
    return sqrt((int(bolan[1]) -
                 int(branca[1])) ** 2 +
                (int(bolan[0]) -
                 int(branca[0])) ** 2)

for i in range(0, int(input())):
    lista_bolas = []
    for j in range(0, int(input())+1):
        # print('j')
        lista_bolas.append(input().split())
        # print(lista_bolas)

    branca = lista_bolas.pop(0)
    # print(branca, lista_bolas)
    distancias = []

    # print(lista_bolas)
    # time.sleep(30)

    for bola in range(0, len(lista_bolas)):
        # print('distancia')
        distancias.append([bola+1, distancia(branca, lista_bolas[bola])])

    distancias = sorted(distancias, key=lambda distancias: distancias[1])

    print(distancias[0][0])

    # for i in distancias:
    #     print(i[0])