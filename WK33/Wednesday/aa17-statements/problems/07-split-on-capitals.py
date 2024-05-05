# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

# Write your function here.

def cap_space(txt):
    result = ""
    for char in txt:
        # Check if the character is uppercase
        if char.isupper():
            # Append a space before the character if it's uppercase
            result += ' ' + char
        else:
            # Simply append the character if it's not uppercase
            result += char
    # Return the modified string in lowercase
    return result.lower()


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"