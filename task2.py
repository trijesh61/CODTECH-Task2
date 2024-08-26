def get_grade_input():
    grades = {}
    while True:
        subject = input("Enter the subject or assignment name (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= 100:
                grades[subject] = grade
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(letter_grade):
    gpa_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return gpa_scale[letter_grade]

def display_results(grades, average, letter_grade, gpa):
    print("\n--- Grade Summary ---")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

def main():
    print("Welcome to the Student Grade Tracker!")
    
    grades = get_grade_input()
    
    if not grades:
        print("No grades entered. Exiting program.")
        return
    
    average = calculate_average(grades)
    letter_grade = determine_letter_grade(average)
    gpa = calculate_gpa(letter_grade)
    
    display_results(grades, average, letter_grade, gpa)

if __name__ == "__main__":
    main()
