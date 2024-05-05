# Create a function `add_upper` that takes a string and returns all of the
# uppercase characters in the string.

# Write your solution here.

def add_upper(txt):
    result = ""  # Initialize an empty string to store the result
    for char in txt:
        if char.isupper():  # Check if the character is uppercase
            result += char  # Append the character to the result string
    return result

print(add_upper("ApPlE"))        #> APE
print(add_upper("Coding"))       #> C
print(add_upper("PIano"))        #> PI
print(add_upper("SUPREME"))      #> SUPREME