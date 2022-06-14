

variable_one = 10
print(type(variable_one))
# displays that its an INT

##! CLASS ##

class Person():
    def __init__(self, name):
        self.name = name

new_person = Person("Will")
print(new_person.name)

class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

new_person = Person("Alice", 36, "6 foot")
print(new_person.age)




