from การทดลองที่5 import register_student, get_student_info, display_registration_system


display_registration_system()

# เพิ่มข้อมูลนักศึกษา 5 คน
students = [
    (66030040, {"name": "ชับวัตร", "gpa": 3.82, "courses": ["CS103", "ENG101"]}),
    (666030080, {"name": "นรเดช", "gpa": 3.75, "courses": ["MATH101", "PHY101"]}),
    (666030083, {"name": "นวพล", "gpa": 3.90, "courses": ["CS102", "BIO101"]}),
    (666030094, {"name": "เนตรชนก", "gpa": 3.85, "courses": ["CS104", "HIST101"]}),
    (660300116, {"name": "พงศตะวัน", "gpa": 3.80, "courses": ["CS101", "CHEM101"]})
]

for student_id, info in students:
    register_student(student_id, info)

# แสดงข้อมูลนักศึกษาแต่ละคน
for student_id, _ in students:
    get_student_info(student_id)
    print("-" * 40)

# แสดงโครงสร้างของ B-Tree
display_registration_system()