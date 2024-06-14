### Tuples ###

# La diferencia con los arrays es que son inmutables, una vez definimos sus datos, no se pueden añadir, eliminar o cambiar, lo único es que se pueden concatenar convirtiéndose en una nueva tupla

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais')
my_other_tuple = ('A', 'B', 'C')

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[1])
#print(my_tuple[4]) IndexError 
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)