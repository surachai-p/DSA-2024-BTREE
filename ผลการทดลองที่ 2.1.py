students = []

for i in range(5):
    print(f"กรุณากรอกข้อมูลนักศึกษาคนที่ {i+1}:")
    name = input("ชื่อ: ")
    StudentID = input("รหัสนักศึกษา: ")
    
    
    student = {"name": name, "StudentID": StudentID, }
    students.append(student)


print("\nข้อมูลนักศึกษาทั้งหมด:")
for student in students:
    print(f"ชื่อ: {student['name']}, รหัสนักศึกษา: {student['StudentID']}")
