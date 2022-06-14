
##! ACTIVITY 2 OOP ##

# Create a character.py file and a game.py file.
# In character.py, create a class called Character.
# Give the character real_name and superhero_name attributes in the constructor, e.g. Clark Kent and Superman.
# Create a setter method to set a superhero power.
# Create a getter method to print out the superhero power.
# Have fun with it - what other methods and attributes could you add?

class Hero():
    def __init__(self, hero_alias):
        self.alias = hero_alias
    def set_name(self, hero_name):
        self.name = hero_name
    def get_name(self):
        print(self.name)

