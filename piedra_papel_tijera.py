import random

rounds = 1
wins = 0
losses = 0

while (wins < 3) and (losses < 3):
  print("*" * 10)
  print("Round: ", rounds)
  print("*" * 10)
  rounds += 1

  def get_user_choice():
    print('Juego de piedra, papel o tijera')
    user_choice = int(
        input('''
      ingrese: 
      1) para Piedra 
      2) para Papel 
      3) para Tijera
      '''))
    return user_choice

  def choice(a):
    choices = {1: 'Piedra', 2: 'Papel', 3: 'Tijeras'}
    return choices.get(a, 'Perder')

  def tex(user, pc):
    print(f'Has elegido: {choice(user)}')
    print(f'El enemigo ha elegido: {choice(pc)}')

  def main():
    global wins, losses
    user = get_user_choice()
    pc = random.randint(1, 3)

    tex(user, pc)

    if pc == user:
      print('Es un empate')
    elif (user, pc) in [(1, 3), (2, 1), (3, 2)]:
      print('Has ganado 😎')
      wins += 1
    else:
      print('Has perdido 😭')
      losses += 1

  if __name__ == "__main__":
    main()