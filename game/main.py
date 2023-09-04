import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('👊 piedra, 🖐 papel o ✌ tijera => ')
  user_option = user_option.lower()  
  
  if not user_option in options:
    print('Esa opción no es válida')
    #continue 
    #exit() #buen tip de los comentarios
    return None, None
  
  computer_option = random.choice(options) #tambien podemos usar una lista en lugar de una tupla
  return user_option, computer_option
  
  print('    User option =>', user_option)
  print('Computer option =>', computer_option)

def check_rules(user_option, computer_option, user_wins, computers_wins):
  if user_option == computer_option:
    print('*' * 16)
    print('*   EMPATE   *')
    print('*' * 16)
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('papel le gana a piedra')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel le gana a piedra')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('*' * 16)
      print('* USUARIO GANO *')
      print('*' * 16)
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('*' * 19)
      print('* COMPUTADORA GANO *')
      print('*' * 19)
      computers_wins += 1
  return user_wins, computers_wins

def run_game():
  computers_wins = 0
  user_wins = 0
  rounds = 1
  while True:  
    #print('*' * 10)
    print('ROUND =>', rounds)
    #print('*' * 10)
  
    print('COMPUTADORA: ', computers_wins)
    print('    USUARIO: ', user_wins)
    rounds += 1
  
    user_option, computer_option = choose_options()
    user_wins, computers_wins = check_rules(user_option, computer_option, user_wins, computers_wins)  
    
    if computers_wins == 2:
      print('------------LA COMPUTADORA GANO--------------')
      break
    if user_wins == 2:
      print('-----------------TU GANASTE------------------')
      break

run_game()