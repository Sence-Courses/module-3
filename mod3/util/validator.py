def validateInput(input, n_opt):
  if input == '':
    print('Debe seleccionar una opcion del menu.')
    return False
  elif not input.isdecimal():
    print('La opcion ingresada no es numerica.')
    return False
  elif input not in opt_list(n_opt):
    print('La opcion ingresada no es valida.')
    return False
  else:
    return True

def opt_list(n_opt):
  opt_list = []  
  for n in range(1, n_opt + 1):
    opt_list.append(str(n))
  return opt_list