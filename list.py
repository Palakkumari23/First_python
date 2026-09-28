
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Accessing elements
print("First element:", numbers[0])

# Adding an element
numbers.append(60)
print("After append:", numbers)

# Inserting an element
numbers.insert(2, 25)
print("After insert:", numbers)

# Removing an element
numbers.remove(40)
print("After remove:", numbers)

# Length of list
print("Length:", len(numbers))

# Sorting
numbers.sort()
print("Sorted list:", numbers)