### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
  "Nombre": "Pedro",
  "Apellido": "Moure",
  "Edad": 35,
  "Lenguajes": {"Python", "Swift", "Kotlin"},
  1: 1.77
}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["Nombre"] = "Brais"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Corrida"
print(my_dict)

# Esto funciona porque estamos accediendo a un valor del diccionario. Si no accediéramos a uno, nos cargaríamos la variable
del my_dict["Calle"]
print(my_dict)

print("Moure" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

# Crea un diccionario nuevo sin valores
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, )

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))