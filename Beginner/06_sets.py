### Sets ###

my_set = set() 
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Brais', 'Moure', 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('MoureDev')  # Un set NO es una estructura ordenada
print(my_other_set)

my_other_set.add('MoureDev') # Un set NO admite repetidos
print(my_other_set)

print("Moure" in my_other_set)
print("Moura" in my_other_set)

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear() 
print((len(my_other_set)))

my_set = {'Brais', 'Moure', 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Python', 'Swift'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set))