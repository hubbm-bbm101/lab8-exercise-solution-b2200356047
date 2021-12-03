import sys
with open(sys.argv[1], "r") as my_file:
    students = {}
    for student in my_file.read().splitlines():
        student = student.split(":")
        students[student[0]] = student[1]

for student in sys.argv[2].split(","):
    try:
        print("Name: " + student +", University: " + students[student])
    except KeyError:
        print(f"No record of ‘{student}’ was found!")

