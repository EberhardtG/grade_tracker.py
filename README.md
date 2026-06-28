# Student Grade Analyzer
A Python application that reads student records from a CSV file, analyzes grades, calculates statistics, and generates a formatted report.
## Features
- Load student data using Python CSV module
- Handle missing files with error messages
- Process Math, Science, English, and History grades
- Skip missing or invalid grade values
- Calculate student averages
- Assign letter grades
- Generate:
  - Total students
  - Class average
  - Highest/lowest averages
  - Grade distribution
  - Individual student summaries
- Export results to a text report
## Technologies
- Python 3
- CSV
- Lists & Dictionaries
- Functions
- Exception Handling
- File Handling
## Usage
Run:

```bash
python main.py
```
The program reads `data/students.csv` and creates:

```
grade_report.txt
```

## Error Handling
Handles:
- Missing CSV files
- Empty grade values
- Students with no valid grades

Students with no grades receive:
```
Average: None
Grade: N/A
```

## Project Skills Demonstrated
- Data processing
- File I/O
- Problem solving
- Modular Python design
- Report automation

## Author
Grant Eberhardt
Software Engineering Portfolio Project
