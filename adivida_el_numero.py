import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numer_elegido = int(input('Elige un número del 1 al 100: '))
    
    while numer_elegido != numero_aleatorio:
        if numer_elegido < numero_aleatorio:
            print('Busca un número más grande: ')
        else:
            print('Busca un número más pequeño: ')
        numer_elegido = int(input('Elige otro número'))
    print('Ganaste!')


if __name__ == '__main__':
    run()