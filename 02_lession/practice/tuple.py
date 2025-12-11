students = {}

key1 = ("Nguyen", "An")
key2 = ("Nguyen", "An")

students[key1] = 8.5
students[key2] = 9.0

print(students[("Nguyen", "An")])  # 8.5

for key, value in students.items():
    print(key, value)