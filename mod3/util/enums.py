from enum import Enum

"""
Coleccion que contiene los criterios de ordenacion para listas.
"""
OrderKeys = Enum('OrderKeys', [
  ('game_def', ['name', 'id']),
  ('game_cat', ['category']),
  ('game_hrs', ['minutes', 'name']),
  ('game_cmp', ['completion', 'name']),
  ('cat_def', ['name', 'id']),
  ('game_historial', []),
])