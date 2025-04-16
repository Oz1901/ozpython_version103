#print("Hola a todos")

# estructura de datos dinamicas
# Listas
# Tuplas
# Conjuntos
# Diccionarios

nombres = ["Alberto","Alejandro","Alejandro","Angel","Alicia","Brayan","Carla"]
palabras_sin_duplicados = list(dict.fromkeys(nombres))
for nombre in palabras_sin_duplicados:
    print(nombre)

'''
for nombre in nombres:
    print(nombre)
'''
