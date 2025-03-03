from การทดลองที่5 import register_student, get_student_info, display_registration_system, registration_system

# ทดสอบการค้นหานักศึกษาจาก B-Tree
def search_student(student_id):
    student_data = registration_system.search(student_id)
    if student_data:
        print(f"ข้อมูลของนักศึกษารหัส {student_id}:")
        print(f"ชื่อ: {student_data['name']}")
        print(f"เกรดเฉลี่ย: {student_data['gpa']}")
        print(f"วิชาที่ลงทะเบียน: {', '.join(student_data['courses'])}")
    else:
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

# เพิ่มข้อมูลนักศึกษา 5 คน
students = [
    (66030040, {"name": "ชับวัตร", "gpa": 3.82, "courses": ["CS103", "ENG101"]}),
    (666030083, {"name": "นวพล", "gpa": 3.75, "courses": ["MATH101", "PHY101"]}),
    (666030094, {"name": "เนตรชนก", "gpa": 3.90, "courses": ["CS102", "BIO101"]}),
    (666030116, {"name": "พงศ์ตะวัน", "gpa": 3.85, "courses": ["CS104", "HIST101"]}),
    (660300147, {"name": "มาติน", "gpa": 3.80, "courses": ["CS101", "CHEM101"]})
]

# ลงทะเบียนนักศึกษาใน B-Tree
for student_id, info in students:
    register_student(student_id, info)

# ทดสอบการค้นหานักศึกษาโดยใช้รหัสนักศึกษา
search_student(666030040)  # ค้นหานักศึกษารหัส 067
search_student(666030083)  # ค้นหานักศึกษารหัส 083
search_student(66030000)  # ทดสอบค้นหานักศึกษารหัสที่ไม่มีในระบบ