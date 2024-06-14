### Lists ###

my_list = list()
my_other_list = [] 

print(len(my_list))

my_list = [30, 20, 58, 59, 22, 90, 22]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.85, "Esqueletinho", "Macaquinho"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
# print(my_other_list[-3]) IndexError
# print(my_other_list[-4]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("Macaquinho S.L.")
print(my_other_list)

my_other_list.insert(1, "Morado")
print(my_other_list)

my_other_list[1] = "Rosa"
print(my_other_list)

my_other_list.remove("Rosa")
print(my_other_list)

my_list.remove(22)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop = my_list.pop(2)
print(my_pop)
print(my_list)

print(my_list)
del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = "Hola Python"

print(my_list)
print(type(my_list))