 # โปรแกรมบันทึกข้อมูลนักศึกษา

students = []

# รับข้อมูลนักศึกษา 5 คน
for i in range(5):
    print(f"นักศึกษาคนที่ {i+1}")
    name = input("ชื่อ: ")
    student_id = input("รหัสนักศึกษา: ")
    
    # เก็บข้อมูลในรูปแบบ Dictionary
    student = {
        "name": name,
        "student_id": student_id
    }
    
    # เพิ่มข้อมูลใน List
    students.append(student)
    print()

# แสดงผลข้อมูลนักศึกษาทั้งหมด
print("ข้อมูลนักศึกษาทั้งหมด:")
for idx, student in enumerate(students, start=1):
    print(f"{idx}. ชื่อ: {student['name']}, รหัสนักศึกษา: {student['student_id']}")