# Python Dictionary

student = {
    "name": "Palak",
    "age": 18,
    "course": "BCA"
}

print("Dictionary:", student)

# Accessing value
print("Name:", student["name"])

# Adding a new item
student["city"] = "Meerut"
print("After adding:", student)

# Updating a value
student["age"] = 19
print("After updating:", student)

# Removing an item
student.pop("city")
print("After removing:", student)

# Length of dictionary
print("Length:", len(student))