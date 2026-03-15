def validateInput(input, n_opt):
  """
  Valida la opcion ingresada.
  Args:
    input (str): Opcion ingresada desde un input.
    n_opt (int): Numero que indica cantidad de opciones en un menu.
  Returns:
    bool: El resultado de la validacion.
  """
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
  """ 
  Genera una lista de opciones a partir de un numero.
  Args:
    n_opt (int): Numero que indica cantidad de opciones en un menu.
  Returns:
    list(str): Lista con las opciones de un menu.
  """
  opt_list = []  
  for n in range(1, n_opt + 1):
    opt_list.append(str(n))
  return opt_list