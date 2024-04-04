
def calculate_gpa(high_school_grade, cognitive_test_grade, achievement_test_grade):
    # Weights for each component
    high_school_weight = 0.4
    cognitive_test_weight = 0.3
    achievement_test_weight = 0.3

    # Calculate weighted average
    weighted_average = (
        (high_school_grade * high_school_weight)
        + (cognitive_test_grade * cognitive_test_weight)
        + (achievement_test_grade * achievement_test_weight)
    )

    return weighted_average


def suggested_specifications(gpa):
    specifications = {
        "Computer Science": 80,
        "Manager": 75,
        "Medicine and Surgery": 98.6,
        "Designing": 73,
        "AI": 78,
    }

    # Filter specifications based on GPA
    suggested = {spec: grade for spec, grade in specifications.items() if grade <= gpa}

    # Sort the suggested specifications by their acceptable grade in ascending order
    sorted_suggested = sorted(suggested.items(), key=lambda x: x[1], reverse=True)

    return sorted_suggested


def main():
    # Get user input for grades
    high_school_grade = float(input("Enter your high school grade: "))
    cognitive_test_grade = float(input("Enter your cognitive test grade: "))
    achievement_test_grade = float(input("Enter your achievement test grade: "))

    # Calculate GPA
    gpa = calculate_gpa(high_school_grade, cognitive_test_grade, achievement_test_grade)

    print("Your GPA is:", gpa)

    # Get suggested specifications based on GPA
    suggested = suggested_specifications(gpa)

    if suggested:
        print("Suggested specifications:")
        for spec, grade in suggested:
            print(f"{spec}: {grade}%")
    else:
        print("Sorry, your GPA does not meet the criteria for any specification.")


if __name__ == "__main__":
    main()
