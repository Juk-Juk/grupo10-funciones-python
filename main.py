# Archivo principal del grupo
# Cada integrante deberá agregar su función en un archivo independiente
# import os
# import importlib
# import sys

# folder_path = "funciones"
# files = os.listdir(folder_path)

# for filename in files:
#   if filename.endswith(".py") and not filename.startswith("__"):
#     module_name = filename[:-3]
#     package_name = folder_path
#     full_module_path = f"{package_name}.{module_name}"
#     try:
#       module = importlib.import_module(full_module_path)
#       print(f"Successfully imported: {full_module_path}")
#     except ImportError as e:
#       print(f"Failed to import {full_module_path}: {e}")

from funciones import *

if __name__ == "__main__":
  print("Ejecución de pruebas de las funciones del grupo")
