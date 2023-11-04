import random

print('Juego de piedra, papel o tijera')
user = int(input('''
ingrese: 
1 para Piedra 
2 para Papel 
3 para Tijera
'''))

def choice(a):
  if a == 1:
      return ('Piedra')
  elif a == 2:
      return ('papel')
  elif a == 3:
      return ('Tijeras')
  else:
      return ('Perder')

def tex():
  print(f' Has elegido: {choice(user)}')
  print(f'El enemigo ha elegido: {choice(pc)}')

pc = random.randint(1, 3)
if pc == user:
    tex()
    print('Es un empate')
elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
    tex()
    print('Has ganado 😎')
else:
    tex()
    print('Has perdido 😭')