import random


def generar_contrasena():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres = mayus + minus + nums + chars
    
    contrasena = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        # con esta funcion .choise(caracteres) de random, escojo un caracter random de la lista caracteres y lo agregamos a caracter_random
        contrasena.append(caracter_random)
        # con .append agregamos el caracter de (random_caracter) a contrasena
        
    contrasena = ''.join(contrasena)
    # con este metodo ''.join convertimos la lista en un string
    return contrasena
    


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()