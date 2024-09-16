student_list = {}

def add_student(student_name, student_id, marks, grade):
    key = (student_name, student_id, grade)  
    student_list[key] = {
        "marks": marks,
        "grade": grade
    }

def display_student(student_name, student_id):
    for key in student_list:
        if key[0] == student_name and key[1] == student_id:
            student = student_list[key]
            print(f"Student Details for {key}:")
            print(f"Marks: {student['marks']}")
            print(f"Grade: {student['grade']}")
            return
    print(f"No student found for {student_name} with ID {student_id}.")

def update_marks(student_name, student_id, new_marks):
    for key in student_list:
        if key[0] == student_name and key[1] == student_id:
            student_list[key]['marks'] = new_marks
            print(f"Updated marks for {key} to {new_marks}.")
            return
    print(f"No student found for {student_name} with ID {student_id} to update.")

if __name__ == "__main__":
    add_student("Christine Akinyi", 101, 90, "A")
    add_student("Megan Otieno", 102, 85, "A-")
    add_student("Bridget Kathure", 201, 92, "A")

    display_student("Christine Akinyi", 101)  
    display_student("Megan Otieno", 102)      
    update_marks("Christine Akinyi", 101, 95) 
    display_student("Christine Akinyi", 101)   
    display_student("Mick Miuriki", 201)
    update_marks("Nathalia Ayoti", 101, 95)
    display_student("Brenda Khamali", 101)