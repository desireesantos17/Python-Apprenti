# Student Grade Tracker 

# Define the grade score into letter grade value 
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Student Grade Tracker")
    students = []

    while True:
        # Ask for student name
        name = input("\nEnter student's full name: ")
        name = name.title()  # Capitalize each word in the name

        # Validating the input for grades
        while True:
            score_input = input("Enter student's grade (0-100): ")
            try:
                score = float(score_input)
                if 0 <= score <= 100:
                    break
                else:
                    print("Please enter a valid grade between 0-100.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 0-100.")

        # Calculate letter grade
        letter_grade = get_letter_grade(score)

        # Store student data
        students.append((name, score, letter_grade))

        # Display the result
        print(f"\nStudent: {name}")
        print(f"Score: {score}")    
        print(f"Letter Grade: {letter_grade}")

        # Ask to add another
        while True:
            again = input("Add another student? (yes/no): ").strip().lower()
            if again == "yes":
                break  # Go back to start of the main while loop
            elif again == "no":
                # Save all student data to a file before exiting
                with open("students.txt", "a") as file:
                    for student in students:
                        file.write(f"{student[0]}, {student[1]}, {student[2]}\n")
                print("Student data saved to students.txt")
                return
            else:
                print("Please enter 'yes' or 'no'.")

# Run the main loop
main()
