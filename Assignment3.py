info = """
Assignment # 2: List Attributes:
Student: Muhammad Saleem Raza
Rollno: AIC000616
Teacher: Engg. Muhammad Qasim
Ta: Hamza, Mansoor and others
Location: Sindh Boys Scout (6:45 - 9:45)
"""
print(info)

print()

# String Attributes:

my_str = ''

for x in dir(my_str)[:33]:
   print(f'{my_str.__getattribute__(x)}')


print()

# List Attributes:

my_list = []

for x in dir(my_list)[:35]:
    print(f'{my_list.__getattribute__(x)}')


print()

# Tuple Attributes:

my_tuple = ()

for x in dir(my_tuple)[:31]:
    print(f'{my_tuple.__getattribute__(x)}')


print()

# Tuple Methods:

my_tuple2 = ('Ali', 'Ahmed', 'Saleem')

# Returns the no of times a specified value occurs in a tuple
print("1_count():",my_tuple2.count('Ali'))

# Searches the tuple for a specified value and returns the position 
# of where it was found
print("2_index():", my_tuple2.index('Ahmed'))

print()

# Dict Attributes
my_dict = {}

for x in dir(my_dict)[:29]:
    print(f'{my_dict.__getattribute__(x)}')


print()

# Dict Methods
my_dict2 = {'name': 'Saleem', 'city': 'Karachi'}

# Returns the value of the specified key
print("1_get():",my_dict2.get('name'))

# Returns a list containing a tuple for each key value pair
print("2_items():",my_dict2.items())

# Returns a list containing the dictionary's keys
print("3_keys():",my_dict2.keys())

# Returns a list of all the values in the dictionary
print("4_values()", my_dict2.values())

# Updates the dictionary with the specified key-value pairs
my_dict2.update({'country': 'PAK'})
print("5_update():", my_dict2)

# Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value
print('6_setdefault():', my_dict2.setdefault('country', 'Lahore'))

# Returns a dictionary with the specified keys and values
my_dict3 = {}
keys = ('time', 'day')
value = 'infinite'
print("7_fromkeys()", my_dict3.fromkeys(keys, value))

# Returns a copy of the dictionary
print("8_copy():", my_dict2.copy())

# Removes the element with the specified key
my_dict2.pop('country')
print("9_pop()", my_dict2)

# Removes the last inserted key-value pair
print("10_ popitem:", my_dict2.popitem())

# Removes all the elements from the dictionary
my_dict2.clear()
print("11_clear(): ", my_dict2)












