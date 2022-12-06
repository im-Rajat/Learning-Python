students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in add_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not open file")


def add_students(f):
    for line in f:
        yield line


read_file()
print(students)
