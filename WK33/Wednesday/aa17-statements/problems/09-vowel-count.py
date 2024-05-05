# Create a function called `vowel_count` that takes in a string and returns a
# count of how many vowels are in the string.

# Write your solution here.

def vowel_count(txt):
    vowels = "aeiou"  # Define the vowels
    count = 0  # Initialize a counter
    for char in txt.lower():  # Convert the string to lowercase to make the check case-insensitive
        if char in vowels:
            count += 1  # Increment the counter if the character is a vowel
    return count


print(vowel_count("App Academy"))         #> 4
print(vowel_count("Coding Expert"))       #> 4
print(vowel_count("Supreme"))             #> 3
print(vowel_count("Chamber of Secrets"))  #> 5