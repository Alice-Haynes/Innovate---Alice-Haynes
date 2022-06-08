
##! DICTIONARIES ##

# LIST LOOKS LIKE THIS ##
cat_1 = ["Salem", "Black", "Moody"]

# DICTIONARY LOOKS LIKE THIS ##
my_cat = {"name":"Salem", "colour": "black", "mood": "sassy"}
print(my_cat)
# - Expected: {'name': 'Salem', 'colour': 'black', 'mood': 'sassy'}

print(my_cat["name"])
# - Expected: 'Salem'
print(my_cat["colour"])
# - Expected: 'black'
print(my_cat["mood"])
# - Expected: 'sassy'

my_cat["name"] = "Whiskers"
print(my_cat["name"])


###! ACTIVITY 1 ###

# Have a go at making your own dictionary for a pet.
# What key:value pairs will you have - species, name, colour etc?
# Have a go at changing some of your items and print, so you can see how the code works.

cats = {"name":"Catcat",
        "colour": "black and white",
        "character": "gobby",
        "age": 10
}

print(cats.values())

for x in cats.items():
    print(x)

cats.pop("age")
for x in cats.items():
    print(x)

del cats["name"]
for x in cats.keys():
    print(x)

cats["age"] = 11
for x in cats.items():
    print(x)

###! ACTIVITY 2 ###

# Make a countries dictionary to represent these countries and their capital cities;
# United Kingdom, France, Germany, Spain and Italy.
# Now use the .setdefault() method to add any 2 more countries and capitals of your choice
# Print all items using a method previously seen before.
# Make a note of which method you prefer, and why.
# You’ve had a change of heart - 
# - now update all the values with the main language spoken in the countries instead of capitals.

countries= {
    "country_1": {"name":"United Kingdom", "capital": "London"},
    "country_2": {"name":"France", "capital": "Paris"},
    "country_3": {"name":"Germany", "capital": "Berlin"},
    "country_4": {"name":"Spain", "capital": "Madrid"},
    "country_5": {"name":"Italy","capital": "Rome"}
}
# print(countries)
# for x in countries.items():
#     print(x)

countries.setdefault("country_6", {"name":"Portugal", "capital":"Lisbon"})
countries.setdefault("country_7",{"name":"Greece", "capital": "Athens"})

print(countries)
for x in countries.items():
    print(x)
## I PREFER THE LOOP METHOD AS IT DISPLAYS A LOT BETTER ##



###! ACTIVITY 3 ###

# Create a list called fav_songs.
# Each item on the list will be a dictionary with the following keys:
# artist, song_name, genre, release_year
# Look back at our lists recap or do some research to add, remove and update some of the dictionaries.

fave_songs= {
    "song1": {"artist":"Queen", "song_name":"Killer Queen", "genre":"Rock", "release_year":"1974"},
    "song2": {"artist":"Johnny Flynn", "song_name":"Detectorists", "genre":"Folk", "release_year":"2014"},
    "song3": {"artist":"Deee-Lite", "song_name":"Groove is in the Heart", "genre":"Dance", "release_year":"1990"},
    "song4": {"artist":"Sister Nancy", "song_name":"Bam Bam", "genre":"Reggae", "release_year":"1982"},
    "song5": {"artist":"Right Said Fred", "song_name":"Deeply Dippy", "genre":"Pop", "release_year":"1992"}
}

for x in fave_songs.items():
    print(x)
