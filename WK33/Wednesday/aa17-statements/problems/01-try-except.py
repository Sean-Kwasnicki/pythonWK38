# In Python, error handling can be done using a `try`/`except` block. Implement
# `except` blocks to handle the exceptions that will be raised for the following
# `try` blocks:

# Example 1
try:
    str = 'hello'
    str[0] = 'h'
    print(str)
except TypeError as e:
    print("TypeError:", e)
finally:
    print('I happen regardless of any exceptions.')

# Example 2
try:
    print(x)
except NameError as e:
    print("NameError:", e)
finally:
    print('I happen regardless of any exceptions.')