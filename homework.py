grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = ['Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron']
grades = [list(map(int, grade.split())) for grade in grades]
student_grades = dict(zip(students, grades))
average_grades = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}
for student, average in average_grades.items():
    print(f"{student}: {average}")
