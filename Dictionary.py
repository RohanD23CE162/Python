dog = {}

dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}
print("Dog Dictionary:", dog)


student_length = len(student)
print("\nStudent Dictionary Length:", student_length)

skills_value = student['skills']
skills_type = type(skills_value)
print("Skills Data Type:", skills_type)


student['skills'].extend(['HTML', 'CSS'])
print("Modified Skills:", student['skills'])


keys_list = list(student.keys())
values_list = list(student.values())
items_list = list(student.items())
print("Dictionary Keys:", keys_list)
print("Dictionary Values:", values_list)
print("List of Tuples:", items_list)

del student['marital_status']

del student
