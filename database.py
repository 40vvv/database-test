import subprocess

def database_test():
  test = '''
  test_user
  test_password
  test_data
  '''
  print (test)
  input ('Press enter to continue...')



def database_users():
    users = '''
    Bolsonaro
    Lula
    Ed.exe
    4.0.v
    
    '''
    print (users)
    input ('Press enter to continue...')


def database_passwords():
    passwords = '''
    bolsonaro-fodao123
    lula-fudido321
    ed-admin
    4.0.v-admin
    
    '''
    print (passwords)
    input ('Press enter to continue...')


def menu():
  menu = '''
        _               _                 _                                    
     ___FJ     ___ _   FJ_      ___ _    FJ___      ___ _     ____      ____   
    F __  L   F __` L J  _|    F __` L  J  __ J    F __` L   F ___J    F __ J  
   | |--| |  | |--| | | |-'   | |--| |  | |--| |  | |--| |  | '----_  | _____J 
   F L__J J  F L__J J F |__-. F L__J J  F L__J J  F L__J J  )-____  L F L___--.
  J\____,__LJ\____,__L\_____/J\____,__LJ__,____/LJ\____,__LJ\______/FJ\______/F
   J____,__F J____,__FJ_____F J____,__FJ__,____F  J____,__F J______F  J______F                                                       
                                                        By: Ed.exe & 4.0.v
  
    
  Databases:
    database_test
    database_users
    database_passwords

  Apps:
    app_test
    
  '''
  print (menu)
  escolha = input ('>> ')
  
  if escolha == 'database_test':
    database_test()

  if escolha == 'database_users':
    database_users()

  if escolha == 'database_passwords':
    database_passwords()

  if escolha == 'app_test':
    subprocess.run(['python', 'app.py'])
    
  else:
    print ('Invalid option')
    input ('Press enter to continue...')

while True:
  menu()

