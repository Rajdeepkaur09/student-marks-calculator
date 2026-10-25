# STUDENT MARKS CALCULATOR

total_subject = int(input("Enter total subjects:"))
total_marks = 0
for i in range(1, total_subject + 1):
    marks = int(input(f"Enter marks in subject {i:} : "))
    total_marks = total_marks + marks
average = total_marks / total_subject
percentage = (total_marks / (total_subject * 100)) * 100

print("----- STUDENT REPORT -----")
print("Total Subjects =", total_subject)
print("Total Marks =", total_marks)
print("Average Marks =", average)
print("Percentage =", percentage, "%")
