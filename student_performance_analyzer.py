# ANALYZER CONFIGURATION
MIN_PASSING_MARK = 40

# A list to store all student records (each record is a dictionary)
student_records = []

def get_student_data():
    """Reads student name and three subject marks from the user."""
    
    # 1. Reading from the keyboard and Using variables
    name = input("\nEnter student name: ")
    
    # Simple input validation for marks
    while True:
        try:
            # 2. Reading from the keyboard and Math expressions
            mark1 = float(input("Enter marks for Subject 1 (0-100): "))
            mark2 = float(input("Enter marks for Subject 2 (0-100): "))
            mark3 = float(input("Enter marks for Subject 3 (0-100): "))
            
            # Check if marks are within a valid range (0-100)
            if 0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100:
                break
            else:
                print("\n**Marks must be between 0 and 100. Please try again.**")
        except ValueError:
            # Using the interpreter interactively/Writing to the screen
            print("\n**Invalid input. Please enter a number for the marks.**")

    # 3. Using Dictionaries
    student_record = {
        "name": name,
        "marks": [mark1, mark2, mark3]
    }
    
    # 4. Using List
    student_records.append(student_record)
    print(f"\n✅ Record for {name} added successfully.")

def calculate_stats(student):
    """Calculates total, average, and determines the grade."""
    
    # 5. Math operators and expressions
    total_marks = sum(student["marks"])
    num_subjects = len(student["marks"])
    average_percent = total_marks / num_subjects
    
    # 6. The if and elif statements
    if average_percent >= 90:
        grade = "A+"
    elif average_percent >= 80:
        grade = "A"
    elif average_percent >= 70:
        grade = "B"
    elif average_percent >= 60:
        grade = "C"
    elif average_percent >= MIN_PASSING_MARK:
        grade = "D"
    else:
        grade = "F (Fail)"

    # Check for failure in individual subjects
    # 7. Using the for statement and Indenting is significant
    for mark in student["marks"]:
        # Indenting is significant: This check happens for every mark.
        if mark < MIN_PASSING_MARK:
            grade = f"F (Failed in one or more subjects)"
            break # Exit loop as soon as one failure is found

    return total_marks, average_percent, grade

def analyze_and_display_results():
    """Analyzes and prints results for all stored students."""
    
    # 8. Writing to the screen
    print("\n" + "="*50)
    print("           📊 STUDENT MARK ANALYSIS 📊")
    print("="*50)

    if not student_records:
        print("\nNo student records to analyze.")
        return

    # 9. Using the for statement (to loop over the list of student dictionaries)
    for record in student_records:
        total, average, grade = calculate_stats(record)
        
        # 10. String operators and expressions (f-strings for easy formatting)
        # Using the interpreter interactively/Writing to the screen
        print(f"\nName:      {record['name']}")
        print(f"Marks:     {record['marks']}")
        print(f"Total:     {total}")
        print(f"Average:   {average:.2f}%") # .2f formats to two decimal places
        print(f"Grade:     **{grade}**")
        print("-" * 50)
        
def main_menu():
    """Main loop for the program."""
    
    # 11. While Loops
    while True:
        print("\n=== Student Analyzer Menu ===")
        print("1. Add New Student Record")
        print("2. Display Analysis Report")
        print("3. Exit Program")
        
        choice = input("Enter your choice (1-3): ")
        
        # 12. The if and elif statements
        if choice == '1':
            get_student_data()
        elif choice == '2':
            analyze_and_display_results()
        elif choice == '3':
            print("\n👋 Exiting Student Marks Analyzer. Goodbye!")
            break
        else:
            print("\n**Invalid choice. Please enter 1, 2, or 3.**")

if __name__ == "__main__":
    main_menu()
