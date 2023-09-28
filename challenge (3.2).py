class Student:

  def_init_(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa =￼ cgpa


def sort￼_students(student_list):
sorted_students =￼ sorted(student_list, key=lambda student:student.cgpa,reverse=True)
#syntax - lambda args:exp
return sorted_students



#Example usage:
student =￼ [Student("Hari","A123",7.8),
student("Srikanth","A124",8.9),
student ("Saumya","A125",9.1),
Student ("Mahidhar","A126",9.9),]

sorted_student =sort_students(students)

#print the sorted list of students
for￼ student￼ in sort￼ed_students:
print("Name: {},Roll Number: {}, cgpa: {}".format(student.name,student.roll_number,student.cgpa))
  