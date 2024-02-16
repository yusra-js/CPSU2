def calculate_gpa(high_school_grade, cognitive_test_grade, achievement_test_grade):
    # Weights for each component
    high_school_weight = 0.4
    cognitive_test_weight = 0.3
    achievement_test_weight = 0.3

    # Calculate weighted average
    weighted_average = (high_school_grade * high_school_weight) + \
                       (cognitive_test_grade * cognitive_test_weight) + \
                       (achievement_test_grade * achievement_test_weight)
    
    return weighted_average

def main():
    # Get user input for grades
    high_school_grade = float(input("Enter your high school grade: "))
    cognitive_test_grade = float(input("Enter your cognitive test grade: "))
    achievement_test_grade = float(input("Enter your achievement test grade: "))

    # Calculate GPA
    gpa = calculate_gpa(high_school_grade, cognitive_test_grade, achievement_test_grade)

    print("Your GPA is:", gpa)

if __name__ == "__main__":
    main()