"""
Assignment # 1: String & List Methods:
Student: Muhammad Saleem Raza
Rollno: AIC000616
Teacher: Engg. Muhammad Qasim
Ta: Hamza, Mansoor ...
Location: Sindh Boys Scout (6:45 - 9:45)
"""
print(__doc__)

# String Methods:
text = " i am a Pakistani "

print('text:', text)

print("1_text.capitalize():", text.capitalize())
# turns first alphabet to capital.

print("2_text.upper():", text.upper())
# turns all text into upper case.

print("3_text.lower():", text.lower())
# turns all text into lower case.

print("4_text.title():", text.title())
# turns first alphabet to capital of each word.

print("5_text.split():", text.split())
# turns each word into list.

print("6_text.strip():", text.strip())
# remove whitespaces from text.

print("7_', '.join(text.split()):", ', '.join(text.split()))
# turns collection into String.

print("8_text.find('am'):", text.find('am'))
# return expected string index no.

print("9_text.casefold():", text.casefold())
# similar to lowercase.

print("10_text.center(22, '$'):", text.center(22, '$'))
# center align string into given char.

print("11_text.count('a'):", text.count('a'))
# count the no of char.

print("12_text.endswith('i'):", text.endswith('i'))
# return True if end at given char o/w False.

print("13_text.encode():", text.encode())
# return encoded string.

t = '14_H\te\tl\tl\to'

print("15_t.expandtabs(2):", t.expandtabs(2))
# specified tab whitespace size.

print("16_text.index('am'):", text.index('am'))
# similar to find().

print("17_text.isdigit():", text.isdigit())
# return True if string is digit.

print("18_text.isdecimal():", text.isdecimal())
# return True if string is decimal.

print("19_text.isalpha()", text.isalpha())
# return True if string is alphabets having no space.

print("20_text.isalnum():", text.isalnum())
# return True if string is alphabets and num having no space.

print("21_text.isidentifier():", text.isidentifier())
# return True if string is a valid identifier if it (a-z) and (0-9), or (_).

print("22_text.islower():", text.islower())
# return True if str is lowercase

print("23_text.isupper():", text.isupper())
# return True if str is uppercase

print("24_text.isnumeric():", text.isnumeric())
# return True if str is numeric

print("25_text.isprintable()", text.isprintable())
# return True if str is printable

print("26_text.isspace():", text.isspace())
# return True if str is space

print("27_text.istitle():", text.istitle())
# return True if str is titled.

t = 'I am {}'
print("28_t.format('Saleem'):", t.format('Saleem'))
# insert given str.

x = {'name': 'Saleem'}
y = 'I am {name}'
print("29_y.format_map(x):", y.format_map(x))
# insert from given dict.

print("30_text.replace(' am', ''m'):", text.replace(" am", "'m"))
# replace chars to another chars.

print("31_text.partition('am'):", text.partition('am'))
# replace chars to another chars.

print("32_text.rfind('am'):", text.rfind('am')) # similar to find().

print("33_text.startswith('Pakistan'): ", text.startswith('Pakistan'))
# return true if given char start with that.

print("34_text.rfind('am'):", text.splitlines())
# turn each line into list.

print("35_text.swapcase():", text.swapcase())
# swap the case of str.

print(end='\n\n\n')


#List Method:

my_list = ['Salim', 'Raza', 'Attari']
print('my_list', my_list)

my_list.append('Qadri')
# Adds an element at the end of the list
print('1_Append: ', my_list)

my_list.reverse()
# Reverses the order of the list
print('2_Reverse: ', my_list)

my_list.sort()
# Sorts the list
print('3_Sorts: ', my_list)

print('4_Index: ', my_list.index('Attari'))
# Returns the index of the first element with the specified value

my_list.insert(2,'Madani')
# Adds an element at the specified position
print('5_Insert: ', my_list)

print('6_Count: ', my_list.count('Salim'))
# Returns the number of elements with the specified value

my_list.extend(my_list)
# Add the elements of a list (or any iterable), to the end of the current list
print('7_Extend: ', my_list)

print('8_Copy: ', my_list.copy())
# Returns a copy of the list

my_list.pop(3)
# Removes the element at the specified position
print('9_Pop: ', my_list)

my_list.remove('Raza')
# Removes the first item with the specified value
print('10_Remove: ', my_list)

my_list.clear()
# Removes all the elements from the list
print('11_Clear: ', my_list)






