### Variables ###

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print

print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema

print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!

name, surname, alias, age = "Esqueletinho", "Macaquinho", "Terrorista Turismofóbico", 1000
print('Me llamo:', name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs

"""
first_name = input('¿Cómo te llamas?: ' ) 
age = input('¿Qué edad tienes?: ' )

print(first_name)
print(age)
"""

# Cambiamos su tipo

name = 1000
age = "Esqueletinho"

print(name)
print(age)

# Forzamos el tipo

address : str = 'Mi dirección'
address = 32
print(address)
print(type(address))