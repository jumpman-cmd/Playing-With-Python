def find_second_lowest_students():
    students = []
    
    for _ in range(int(input().strip())):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
    
    # Sort the list based on grades
    students.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    lowest_grade = students[0][1]
    second_lowest_grade = None
    
    for student in students:
        if student[1] > lowest_grade:
            second_lowest_grade = student[1]
            break
    
    # Get the names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    second_lowest_students.sort()
    
    # Print the names
    for student in second_lowest_students:
        print(student)

if __name__ == "__main__":
    find_second_lowest_students()