# Initialize different list types to demonstrate Python's type system and sorting behaviors
# String representations of numbers for string vs numeric sorting comparison
num_strings = ["15","100","55","42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

# Display type information and contents for each list structure
# This helps visualize how Python handles different data types internally
print(f"\nThe variable num_strings is a {type(num_strings)}")
print(f"It contains the elements {num_strings}")
print(f"The element {num_strings[1]} is a {type(num_strings[1])}")

print(f"\nThe variable num_ints is a {type(num_ints)}")
print(f"It contains the elements {num_ints}")
print(f"The element {num_ints[1]} is a {type(num_ints[1])}")

print(f"\nThe variable num_floats is a {type(num_floats)}")
print(f"It contains the elements {num_floats}")
print(f"The element {num_floats[1]} is a {type(num_floats[1])}")

print(f"\nThe variable num_lists is a {type(num_lists)}")
print(f"It contains the elements {num_lists}")
print(f"The element {num_lists[1]} is a {type(num_lists[1])}")

# Demonstrate different sorting behaviors between string and numeric types
print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
num_ints.sort()
# Display sorted results to highlight the difference between string and numeric sorting
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")
# Explain the key difference in sorting behavior
print("\nStrings are sorted alphabetically while integers are sorted numerically")

print("\nThank you for testing my app!")

