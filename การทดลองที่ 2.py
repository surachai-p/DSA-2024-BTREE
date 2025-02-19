from การทดลองที่5 import register_student, get_student_info, display_registration_system


display_registration_system()

# เพิ่มข้อมูลนักศึกษา 5 คน
students = [
    (666030067, {"name": "ธนกฤษ พิมพ์อรัญ", "gpa": 3.90, "courses": ["CS103", "ENG101"]}),
    (666030083, {"name": "นวพล คำแก้ว", "gpa": 3.70, "courses": ["MATH101", "PHY101"]}),
    (666030094, {"name": "เนตรชนก สุริโย", "gpa": 3.80, "courses": ["CS102", "BIO101"]}),
    (666030194, {"name": "สุภาวดี เจริญไชย", "gpa": 3.95, "courses": ["CS104", "HIST101"]}),
    (660300000, {"name": "ใครไม่รู้ จำไม่ได้", "gpa": 3.65, "courses": ["CS101", "CHEM101"]})
]

for student_id, info in students:
    register_student(student_id, info)

# แสดงข้อมูลนักศึกษาแต่ละคน
for student_id, _ in students:
    get_student_info(student_id)
    print("-" * 40)

# แสดงโครงสร้างของ B-Tree
display_registration_system()
