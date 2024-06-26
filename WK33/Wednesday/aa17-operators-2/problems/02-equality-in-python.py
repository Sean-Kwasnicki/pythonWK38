# Try to explore the difference between equality operators in JavaScript and
# Python. Try comparing primitive data types using `==` and then reference data
# types.

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]
list3 = [2, 3]

# Use "==" to compare these values and see what gets printed! How does this
# compare with JavaScripts "==="?

# Compare "x" with itself
# Compare "x" with "y"
# Compare "list1" with "list2"
# Compare "list1" with "list3"

def compare(val1, val2):
    return val1 == val2

print(compare(x, y))

print(compare(list1, list2))

print(compare(list1, list3))


