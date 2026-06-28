"""
Project: Student Grade Tracker
Pre-Work Section C — Python Fundamentals
Estimated time: 45-60 minutes

Objective: Build a data processing script that reads student grades from
a CSV, calculates averages, assigns letter grades, and writes a summary report.

Your job: implement all the functions marked with # TODO.
Do NOT modify the function signatures or the main() function.
"""

import csv


# ============================================================
# FUNCTION 1: Load data from CSV
# ============================================================

def load_students(filepath: str) -> list[dict]:
    student_data = []

    try:
        with open(filepath, newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                #went with .get() to handle missing keys gracefully, returning an empty string if the key is not found
                row["math"] = row.get("math", "")
                row["science"] = row.get("science", "")
                row["english"] = row.get("english", "")
                row["history"] = row.get("history", "")

                student_data.append(row)
        #handle the case where the file is not found and return an empty list with an error message
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    #return the list of student data dictionaries

    return student_data



# ============================================================
# FUNCTION 2: Calculate average, handling missing values
# ============================================================

def calculate_average(grades: list) -> float | None:
    if not grades:
        return None
    total = 0
    count = 0
    for grade in grades:
        try:
            # Convert grade to float and add to total
            total += float(grade)
            count += 1
        except (ValueError, TypeError):
            # Skip invalid grades (empty strings or non-numeric values)
            continue
    if count == 0:
        return None
    return round(total / count, 1)
   



# ============================================================
# FUNCTION 3: Assign letter grade
# ============================================================

def get_letter_grade(average: float | None) -> str:
   
    # average is expected to be a numeric value or None; do not recalc here
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    if average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


# ============================================================
# FUNCTION 4: Generate summary report
# ============================================================

def generate_report(students: list[dict]) -> dict:
    #for loop through each student in the list of students
    averages = []
    student_summaries = []
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    #declare empty lists for averages and student summaries, and a dictionary to track grade distribution
    for student in students:
        #used .get() to retrieve grades for each subject, which allows for missing keys without raising an error
        grades = [
            student.get("math"),
            student.get("science"),
            student.get("english"),
            student.get("history"),
        ]
        average = calculate_average(grades)
        if average is not None:
            averages.append(average)

        letter_grade = get_letter_grade(average)
        student_summary = {
            "name": student.get("student_name", "Unknown"),
            "average": average,
            "grade": letter_grade,
        }
        student_summaries.append(student_summary)
        grade_distribution[letter_grade] += 1

    total_students = len(students)
    class_average = calculate_average(averages) if averages else None

    if averages:
        highest_average = max(averages)
        lowest_average = min(averages)
    else:
        highest_average = None
        lowest_average = None
        #return a dictionary containing the total number of students, class average, highest and lowest averages, grade distribution, and individual student summaries
    return {
        "total_students": total_students,
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_distribution,
        "students": student_summaries,
    }

   
    


# ============================================================
# FUNCTION 5: Write report to a file
# ============================================================

def write_report(report: dict, filepath: str) -> None:
    report_text = "============================\n"
    report_text += "STUDENT GRADE REPORT\n"
    report_text += "============================\n"
    #used report_text to build a formatted string that includes the total number of students, class average, highest and lowest averages, and grade distribution

    report_text += f"Total Students: {report['total_students']}\n"
    report_text += f"Class Average: {report['class_average']}\n"
    report_text += f"Highest Average: {report['highest_average']}\n"
    report_text += f"Lowest Average: {report['lowest_average']}\n\n"

    report_text += "Grade Distribution:\n"  
    report_text += "------------------\n"

    for grade, count in report["grade_distribution"].items():
        report_text += f"{grade}: {count}\n"
#the function write_report() takes a report dictionary and a file path as input. It constructs a formatted string report_text that contains the summary report, including total students, class average, highest and lowest averages, and grade distribution. The function then opens the specified file in write mode and writes the report_text to the file.

    for student in report["students"]:
        report_text += (
            f"Name: {student['name']}\n"
            f"Average: {student['average']}\n"
            f"Grade: {student['grade']}\n\n"
        )

    with open(filepath, "w") as file:
        file.write(report_text)

    print(f"Report written to {filepath}")
 
 

# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
 main()
