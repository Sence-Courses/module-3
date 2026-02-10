from enum import Enum

"""
Coleccion que contiene los criterios de ordenacion para listas.
"""
OrderKeys = Enum('OrderKeys', [
  ('game_def', ['name', 'id']),
  ('game_cat', ['category']),
  ('game_hrs', ['minutes']),
  ('game_cmp', ['completion']),
  ('cat_def', ['name', 'id'])
])