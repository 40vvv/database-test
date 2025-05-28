def login_password():
  print ('')
  print ('  Password:')
  print ('')
  password = input ('>> ')
  
  if password == 'admin':
    print ('')
    print ('Bem Vindo, Admin')
    input ('Pressione Enter para continuar...')

def login():
  login = '''

  ╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╦  ┌─┐┌─┐┬┌┐┌  ╔═╗┌─┐┌─┐┌─┐
  ╚═╗││││├─┘│  ├┤   ║  │ ││ ┬││││  ╠═╝├─┤│ ┬├┤ 
  ╚═╝┴┴ ┴┴  ┴─┘└─┘  ╩═╝└─┘└─┘┴┘└┘  ╩  ┴ ┴└─┘└─┘

  Username:
  '''
  print (login)
  user = input ('>> ')

  if user == 'admin':
    login_password()
  

def menu_app():
  menu = '''
  ╔╦╗┬ ┬  ╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╔═╗┌─┐┌─┐ 
  ║║║└┬┘  ╚═╗││││├─┘│  ├┤   ╠═╣├─┘├─┘
  ╩ ╩ ┴   ╚═╝┴┴ ┴┴  ┴─┘└─┘  ╩ ╩┴  ┴  
    *Aplicativo de Teste* Feito por: Ed.exe & 4.0.v    

  Test Apps:
    test_login

'''
  print (menu)
  escolha_login = input ('>> ')
  
  if escolha_login == 'test_login':
    login()

menu_app()