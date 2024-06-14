### Classes ###

class MyEmptyPerson:
  pass

print(MyEmptyPerson)

class Person:
  def __init__(self, name, surname, alias = "Sin alias"):
    self.full_name = f"{name} {surname} ({alias})"

  def walk (self):
    print(f"{self.full_name} Está camninando")

my_person = Person('Brais', 'Moure')

print(my_person.full_name)
my_person.walk() 

my_other_person = Person("Miguel Ángel", "Durán", "Midudev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León El loco de los perros"
print(my_other_person.full_name)