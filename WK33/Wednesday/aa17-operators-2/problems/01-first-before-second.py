# You are given three inputs: a string, one letter, and a second letter.

# Write a function that returns `True` if every instance of the first letter
# occurs before every instance of the second letter.

# Look at the String Methods to possibly help you find some methods that can
# make this easier.
# https://docs.python.org/3.9/library/stdtypes.html?highlight=strings#string-methods

# Write your function here.

def first_before_second(string, char1, char2):
    # Find the index of the last occurrence of char1
    last_index_char1 = string.rfind(char1)
    # Find the index of the first occurrence of char2
    first_index_char2 = string.find(char2)
    
    # Check if the last occurrence of char1 is before the first occurrence of char2
    return last_index_char1 < first_index_char2


print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

print(first_before_second("what about this sentence a jackrabbit along a joyfull alley joy.", "a", "j"))
