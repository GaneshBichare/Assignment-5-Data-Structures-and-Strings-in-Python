student_marks = {
    "Ram": 55,
    "Sham": 58,
    "Ron": 62,
    "Raj": 74,
    "Arjun": 98
}


student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")