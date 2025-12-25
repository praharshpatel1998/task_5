"""
create a dictionary with key student and marks
if the user enters the student name if it will available in the dictionary
print student name with marks  "CARLO 94"
ELSE  print student not found
"""
data = {'Alice' :89 ,'carlo':94,'jordan':81}
Student_name = input("Enter the student name: ")

if Student_name in data:
    print(F'{Student_name}  marks : {data[Student_name]}')
else:
    print("student not found")



