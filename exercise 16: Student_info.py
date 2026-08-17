#Enter student's baic information
name = input("Enter the student's name: ")
prn = input("Enter the student's PRN: ")
# Read marks in three subjects
marks_subject1 = float(input("Enter marks in subject 1: "))
marks_subject2 = float(input("Enter marks in subject 2: "))
marks_subject3 = float(input("Enter marks in subject 3: "))
# Calculate total marks and percentage
total_marks = marks_subject1 + marks_subject2 + marks_subject3
percentage = (total_marks / 300) * 100 
# Display student details and results
print("\nStudent Details:")
print("-----------------")
print(f"Name:{name}")
print(f"PRN: {prn}")
print(f"Marks in Subject 1: {marks_subject1}")
print(f"Marks in Subject 2: {marks_subject2}")
print(f"Marks in Subject 3: {marks_subject3}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
