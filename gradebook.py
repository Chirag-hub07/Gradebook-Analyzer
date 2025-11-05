# Gradebook Analyzer
# Created by:-
# Name- Chirag Virdi
# Class- Btech CSE (DS)
# Roll no- 2501420017
# Date- 01/11/25


print(' -------------------------------------------------------------')
print('                         GRADEBOOK ANALYZER')
print('- This program allows users to enter or load student marks')
print('- Calculates statistics, assigns grades, shows pass/fail lists')
print('- Displays everything in a neat table')
print(' -------------------------------------------------------------')

def manual_entry():
    print('\n Manual entry selected')
    print('-------------------------- \n')
    marks={}
    while True:
        name=input("Enter student name (or 'done' to finish): ")
        if name.lower()=='done':
            break 
        else:
            score=float(input(f'Enter marks of {name}: '))
            marks[name]= score
            if score<0 or score>100:
                print('INVALID MARKS! PLEASE ENTER VALID MARKS.')
            else:
                continue
    return marks

import csv
def load_csv():
    print('\n CSV File loading selected')
    print('----------------------------- \n')
    filename= input('Enter CSV File name (with .csv extension): ')
    marks={}
    try:
        with open (filename,'r') as file:
            reader= csv.reader(file)
            next(reader)
            for row in reader:
                name=row[0]
                score=row[1]

                if score.replace('.', '', 1).isdigit():
                    marks[name] = float(score)
                else:
                    print(f"Skipping invalid marks for {name}")

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("File not found! Please check the name and try again.")

    return marks

import statistics
def calculate_stats(marks):
    scores = list(marks.values())
    avg = statistics.mean(scores)
    med = statistics.median(scores)
    high_name = max(marks, key=marks.get)
    low_name = min(marks, key=marks.get)

    print("\n --- Statistics ---")
    print(f"Average Marks : {avg:.2f}")
    print(f"Median Marks  : {med:.2f}")
    print(f"Highest Marks : {high_name} ({marks[high_name]})")
    print(f"Lowest Marks  : {low_name} ({marks[low_name]})")

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def pass_fail(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]

    print("\n Passed Students:", ", ".join(passed) if passed else "None")
    print(" Failed Students:", ", ".join(failed) if failed else "None")

def print_table(marks, grades):
    print("\n --- Final GradeBook ---")
    print(f"{'Name':<20}{'Marks':<10}{'Grade':<6}")
    print("-" * 36)
    for name in marks:
        print(f"{name:<20}{marks[name]:<10}{grades[name]:<6}")

def main():
    print(" Welcome to GradeBook Analyzer ")
    while True:
        print("\n===============================")
        print("1  Enter data manually")
        print("2  Load data from CSV file")
        print("3  Exit program")
        print("===============================")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            marks = manual_entry()
        elif choice == '2':
            marks = load_csv()
        elif choice == '3':
            print("\n Thank you for using GradeBook Analyzer!")
            break
        else:
            print("Invalid choice! Please try again.")
            continue

        if not marks:
            print("No data available to analyze!")
            continue

        calculate_stats(marks)
        grades = assign_grades(marks)
        pass_fail(marks)
        print_table(marks, grades)

main()