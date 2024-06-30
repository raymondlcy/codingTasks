# File student_register.py for Practical Task 2 on T08
# Read total students number from input
total_students = int(input("How many students need to be registered? "))

# Define student id list for storing from user inputs
student_id = []

# Read user input until reaching the total number of students
while total_students > 0:    
    user_input = input("Enter student ID: ")
    student_id.append(user_input)
    total_students -= 1

# Write all student id into reg_form.txt with line seperator
with open('reg_form.txt', 'w') as file:
    file.writelines([line + '..................................\n' for line in student_id])
