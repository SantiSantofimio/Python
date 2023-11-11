import random


def run():
    vidas = 5 
    numero_aleatorio = random.randint(1, 100)
    numer_elegido = int(input('Elige un número del 1 al 100: '))
    
    while (numer_elegido != numero_aleatorio):
        if (numer_elegido < numero_aleatorio) and (vidas > 1):
            vidas -= 1
            print(f'Busca un número más grande, te quedan {vidas} vidas: ')
            numer_elegido = int(input('Elige otro número: '))
        elif (numer_elegido > numero_aleatorio) and (vidas > 1):
            vidas -= 1
            print(f'Busca un número más pequeño, te quedan {vidas} vidas: ')
            numer_elegido = int(input('Elige otro número: '))
        else:
            print(f'Te quedan {vidas - 1}, parece que has perdido. 😭')
            return
    print('Ganaste!')
    
    # while (numer_elegido != numero_aleatorio):
    #     if (numer_elegido < numero_aleatorio) and (vidas > 1):
    #         vidas -= 1
    #         print(f'Busca un número más grande, te quedan {vidas} vidas: ')
    #         numer_elegido = int(input('Elige otro número: '))
    #     elif (numer_elegido > numero_aleatorio) and (vidas > 1):
    #         vidas -= 1
    #         print(f'Busca un número más pequeño, te quedan {vidas} vidas: ')
    #         numer_elegido = int(input('Elige otro número: '))
    #     elif (numer_elegido != numero_aleatorio) or (vidas == 0):
    #         print(f'Te quedan {vidas - 1}, parece que has perdido. 😭')
    #         break
    #     else:
    #         print('Ganaste!')


if __name__ == '__main__':
    run()