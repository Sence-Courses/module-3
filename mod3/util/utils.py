import os, random

game_id_range = 1000

def find_element(key, key_value, datalist):
  """
  Busca un elemento en una lista a partir de una llave y un valor dados.
  Args:
    key (str): Llave que indica el campo que se desea evaluar.
    key_value (any): Valor que se busca para la llave ingresada.
    datalist (list): Lista en la que se busca el valor dado.
  Returns:
    any, bool: El item buscado o False si no se encuentra.
  """
  found_item = next((i for i in datalist if i[key] == key_value), None)
  return found_item if found_item else False
  
def filter_col(key, key_value, datalist):
  """
  Filtra uno o mas elementos de una lista.
  Args:
    key (str): Llave que indica el campo a comparar.
    key_value (any): Valor que indica el criterio del filtro.
    datalist: Lista que contiene los elementos a evaluar.
  Returns:
    list(any): Lista que retorna los elementos no coincidentes con la Llave-Valor.
  """
  iter = filter(lambda c: c[key] != key_value, datalist)
  return list(iter)

def get_list_by_match(key, key_value, datalist):
  """
  Retorna una lista filtrada por el campo seleccionado.
  Args:
    key (string): Campo a comparar.
    key_value (any): Valor del campo a comparar.
    datalist (list): Lista a la que se le aplicara el filtro.
  Returns:
    list: Lista filtrada por el campo y el valor ingresados.
  """
  iter = filter(lambda e: key_value in e[key], datalist)
  return list(iter)

def order_datalist(datalist, keys, reverse=False):
  """
  Ordena una lista correspondiente a la data de un archivo JSON.
  Args:
    datalist (list): Lista que representa los datos de un archivo JSON.
    keys (list): Lista que contiene las llaves para ordenar la lista JSON.
  Returns:
    list(any): Lista ordenada a partir de las llaves ingresadas.
  """
  return sorted(datalist, key=lambda x: set_keys(x, keys), reverse=reverse)

def set_keys(x, keys):
  """
  Genera una tupla con los campos que indican el criterio de orden de la lista.
  Args:
    x (any): Elemento de una lista al que se aplicara el orden.
    keys (list): Llaves asociadas un elemento de una lista.
  Returns:
    tupla: Tupla que contiene elementos de tipo elemento[key]. (x[key])
  """
  k_lst = []
  for key in keys:
    k_lst.append(x[key])
  return tuple(k_lst)

def generate_game_id():
  """
  Genera un id aleatorio entre 1 y el rango maximo definido.
  Returns:
    int: id generado aleatoriamente.
  """
  return random.randint(1, game_id_range + 1);

def get_formatted_time(minutes):
  """
  Retorna un mensaje con la hora a partir de los minutos ingresados.
  Args:
    minutes (int): Valor que indica los minutos.
  Returns:
    str: Mensaje que retorna hoas y minutos a partir de los minutos ingresados.
  """
  hours, minutes = divmod(minutes, 60)
  return f'{hours} horas y {minutes} minutos.'

def clear_screen():
  """ Limpia la pantalla de la consola. """
  os.system('cls' if os.name == 'nt' else 'clear')