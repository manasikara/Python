'''
Project
School Grades Program
You're a tutor at a local school and you want to calculate the percentages of the students' grades in total to see if they pass.
'''

student_name = "Sam"
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69
total_grade = (math_grade + science_grade + english_grade + geology_grade)
max_grade = 400
total_percentage = total_grade / max_grade * 100
print(f"Sam's total percentage is {total_percentage}%")
total_percentage = int(total_percentage)
did_student_pass = total_percentage >= 50
#TBC...