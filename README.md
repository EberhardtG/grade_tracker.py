# Student Grade Analyzer

A Python-based student grade analysis application that reads student records from a CSV file, processes academic performance data, calculates statistics, and generates a formatted grade report.

This project demonstrates practical Python programming concepts including file handling, CSV processing, data validation, functions, dictionaries, exception handling, and report generation.

---

## Features

- Load student records from a CSV file
- Handle missing files gracefully with helpful error messages
- Process grades for multiple subjects:
  - Math
  - Science
  - English
  - History
- Calculate individual student averages
- Skip missing or invalid grade values
- Assign letter grades based on student averages
- Generate class-level statistics:
  - Total number of students
  - Class average
  - Highest student average
  - Lowest student average
- Generate grade distribution reports
- Create individual student summaries
- Export a formatted text report

---

## Technologies Used

- Python 3
- CSV Module
- File Handling
- Lists
- Dictionaries
- Functions
- Exception Handling
- String Formatting

---

## Project Structure

```
student-grade-analyzer/
│
├── main.py
│
├── data/
│   └── students.csv
│
├── grade_report.txt
│
└── README.md
```

---

## How It Works

### 1. Load Student Data

The application reads student information from a CSV file using Python's built-in `csv` module.

Example:

```csv
student_name,math,science,english,history
John Smith,85,90,88,92
Sarah Jones,90,,95,87
```

The CSV data is converted into a list of dictionaries for processing.

---

### 2. Calculate Student Averages

Each student's grades are analyzed individually.

Example:

```
Math: 85
Science: 90
English: 88
History: 92

Average: 88.8
```

Missing grades are skipped instead of causing the program to crash.

---

### 3. Assign Letter Grades

Students receive a letter grade based on their average:

| Average | Grade |
|---|---|
| 90+ | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |
| No valid grades | N/A |

---

## Report Generation

The application creates a report containing:

- Class summary statistics
- Grade distribution
- Individual student results

Example:

```
============================
STUDENT GRADE REPORT
============================

Total Students: 25
Class Average: 84.6
Highest Average: 98.5
Lowest Average: 62.0


Grade Distribution:
------------------
A: 8
B: 10
C: 5
D: 1
F: 1


Name: John Smith
Average: 88.8
Grade: B
```

The final report is saved as:

```
grade_report.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/student-grade-analyzer.git
```

Navigate into the project folder:

```bash
cd student-grade-analyzer
```

---

## Running the Application

Run the program:

```bash
python main.py
```

The application will:

1. Load student data from the CSV file
2. Process grades
3. Calculate statistics
4. Display a summary
5. Create a formatted grade report

---

## Error Handling

The application handles common issues including:

### Missing CSV File

If the student data file is missing:

```
Error: The file 'data/students.csv' was not found.
```

The program does not crash and returns an empty dataset.

### Missing Grades

Empty grade values are ignored during calculations.

Example:

```
Grades:
90, "", 85, 95

Average:
90
```

### Students With No Valid Grades

Students without valid grades receive:

```
Average: None
Grade: N/A
```

---

## Challenges Solved

- Built a CSV data processing workflow
- Converted raw CSV data into structured Python objects
- Implemented reusable functions
- Created grade calculation logic
- Added error handling for missing files and invalid data
- Generated automated text reports
- Organized code into separate processing stages

---

## Future Improvements

Potential enhancements:

- Add database storage
- Create a graphical user interface
- Add automated testing with pytest
- Export reports to CSV or PDF
- Add student performance sorting
- Create a web-based dashboard

---

## Author

Grant Eberhardt

Software Engineering Portfolio Project
