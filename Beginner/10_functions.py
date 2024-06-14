### Functions ###

def my_function ():
  print("Esto es una función")

my_function()


def sum_two_values(first_number, second_number):
  print(first_number + second_number)

sum_two_values(1,2)


def sum_two_values_with_return(first_number, second_number):
  return first_number + second_number

my_result = sum_two_values_with_return(10,5)

print(my_result)


def print_name(name, surname):
  print(f"{name} {surname}")

print_name (surname ="Moure", name = "Brais")


def print_name_with_default(name, surname, alias = "Sin alias"):
  print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")
print_name_with_default("Brais", "Moure")


def print_texts(*text): # El asterisco sirve para aplicar parámetros dinámicos
  print(text)

print_texts("Hola", "Python", "MoureDev")