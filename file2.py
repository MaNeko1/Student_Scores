import pandas as pd
student_name_list = []
student_score_list = []
student_grade = []

student_count = 2 # YOUR STUDENT
for i in range(student_count):
    student_name = input("Enter student name: ")
    while True:
        student_score = input(f"Enter {student_name} score: ")
        if student_score.isdigit():
            student_score = int(student_score)
            break
        else:
            print("Please enter number.")
    student_name_list.append(student_name)
    student_score_list.append(student_score)

# NAME SCORE GRADE
for i in range(student_count):
    if 80 <= student_score_list[i] <= 100:
        student_grade.append("A")
    elif 70 <= student_score_list[i] <= 79:
        student_grade.append("B")
    elif 60 <= student_score_list[i] <= 69:
        student_grade.append("C")
    elif 50 <= student_score_list[i] <= 59:
        student_grade.append("D")
    elif student_score_list[i] < 50:
        student_grade.append("F")
        
    print(student_name_list[i], student_score_list[i], student_grade[i])

df = pd.DataFrame({
    "name" : student_name_list,
    "score" : student_score_list,
    "grade" : student_grade
})

df.to_excel('File2.xlsx', index=False)