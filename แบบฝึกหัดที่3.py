from การทดลองที่5 import register_student, get_student_info, display_registration_system

# เพิ่มข้อมูลนักศึกษา
register_student(66030067, {"name": "ธนกฤษ", "gpa": 3.5, "courses": ["Math", "Physics"]})
register_student(66030043, {"name": "ฐาณิดา", "gpa": 3.8, "courses": ["Chemistry", "Biology"]})
register_student(66030204, {"name": "อัครภูมิ", "gpa": 3.2, "courses": ["History", "English"]})

# แสดงโครงสร้างของ B-Tree
display_registration_system()

# ค้นหาข้อมูลนักศึกษา
get_student_info(66030040)
get_student_info(66030083)
get_student_info(66030116)
get_student_info(66030000)  # ทดสอบค้นหาค่าที่ไม่มีใน B-Tree