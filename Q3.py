# # Implement Student/Product/Employee Management System

# -> Create a Student Management System that allows administrators (like functionality) 
#     to manage student records including their scores and skills.

# -> System Setup

#     -> Create system information which is fixed and shouldn’t be modified 

#         -> System name: Edify Student Management Portal
#         -> Version: v1
#         -> Year: 2025
#         -> Institution: Edify University 

#     -> Create admin contact information which shouldn’t be modified 

#         -> Email: admin@edify.com
#         -> Phone: 9808080
#         -> Room No: 201
    
#     -> Display System Info At Startup

# -> Core functionalities

#     -> Adding Student (CRUD - C)

#         -> Prompt for Student ID and check if it already exists(ID's should be unique)
#         -> Get Student Name and Format it using (Ravi Krishna)
#         -> Store Multiple Scores 
#             -> Accept scores one by one until the user types done
#             -> Validate scores entered, should be in between 0-100
#             -> Scores can be duplicates 
#         -> Store Skills 
#             -> Accept skills one by one until the user types done
#             -> Skills cannot be duplicates(Unique Skills)
    
#     -> Modifying Student (CRUD - U)

#         -> Search Student By ID
#         -> Update Name Of Student, if ID exists 
#         -> If Student ID doesn't exist, show appropriate error Student Not Found 

#     -> Delete Student (CRUD - D)

#         -> Remove Student By ID
#         -> If Student ID doesn't exist, show appropriate error Student Not Found 
    
#     -> List All Students (CRUD - R)

#         -> Display all the students information in a formatted way 
        
#         -> For each student show
#             -> ID
#             -> Name
#             -> All Scores 
#             -> Average Score
#             -> Highest Score 
#             -> All Skills 
#             -> Count Of Skills 

#     -> Exit System 

#         -> When system exits, show admin details to contact 


    
# -> Solution Approach 

#     -> Menu Based System 

#     -> System Setup (Fixed) : Using Tuples is good choice (Immutable)
    
#     -> Student Info : Using Dictionary

#     -> Scores : Lists 

#     -> Skills : Sets 

# ____________________________________________________________________________________________________________________

# System Setup (Fixed)
system_info = (
    "Edify Student Management Portal", 
    "v1", 
    2025, 
    "Edify University"
)

admin_contact = {
    "Email": "admin@edify.com",
    "Phone": "9808080",
    "Room No": "201"    
    }

# Display System Info At Startup

print('=' * 50)
print(f" Welcome to {system_info[0]} )")
print(f" Developed By Students : {admin_contact[3]}")
print("=" * 50)

# Student Info : Using Dictionary

students = {}

# Build the menu based system

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Modify Student")
    print("3. Delete Student")
    print("4. List All Students")
    print("5. Exit System")

    choice = input("Enter your choice (1-5): ")     

    if choice == '1':
        # Adding student
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("student ID already exists. Please use a unique ID.")
            continue
        else:
            name=input("Enter Student Name: ").title()
            scores = []
            while True:
                score_input= input("Enter Score (or type 'done' to finish): ")
                if score_input.lower() == 'done':
                    break
