import json

student = {
    "name": "Palak",
    "age": 20,
    "course": "BCA",
    "semester": 3
}

# JSON file me data save
with open("student.json", "w") as file:
    json.dump(student, file)

print("Data saved successfully")
{
    "name": "Palak",
    "age": 20,
    "course": "BCA",
    "semester": 3
}
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["course"])