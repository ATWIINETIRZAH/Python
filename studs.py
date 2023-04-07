# Assume we have a list of dictionaries called students
students = [
    {"name": "Tirzah", "age": 16, "course": "Robotics"},
    {"name": "Diana", "age": 17, "course": "Cybersecurity"},
    {"name": "Ned", "age": 40, "course": "Web development"},
    {"name": "Moses", "age": 35, "course": "Artificial Intelligence"}
]

# Initialize an empty list called old_students
old_students = []

# Loop through the students list
for student in students:
    # Check if the person is older than 16
    if student["age"] > 16:
        # If the person is older than 16, add them to the old_people list
        old_students.append(student)
    else:
        # If the person is 16 or younger, print their name
        print("Young Student: ")
        print(f"{student['name']} is {student['age']} years old.")

# Print the young_people list
print("Old students:", old_students)
