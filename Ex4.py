class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, order):
        self.root = BTreeNode(leaf=True)
        self.order = order

    def search(self, key, node=None):
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and key > node.keys[i][0]:
            i += 1
        
        if i < len(node.keys) and node.keys[i][0] == key:
            return node.keys[i][1]
        
        if node.leaf:
            return None
        
        return self.search(key, node.children[i])
    
    def insert(self, key, value):
        root = self.root
        
        if len(root.keys) == (2 * self.order) - 1:
            new_node = BTreeNode()
            new_node.children.append(self.root)
            self.root = new_node
            self.split_child(new_node, 0)
            self._insert_non_full(new_node, key, value)
        else:
            self._insert_non_full(root, key, value)
    
    def split_child(self, parent, i):
        order = self.order
        child = parent.children[i]
        new_child = BTreeNode(leaf=child.leaf)
        
        mid = order - 1
        parent.keys.insert(i, child.keys[mid])
        parent.children.insert(i + 1, new_child)
        
        new_child.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]
        
        if not child.leaf:
            new_child.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]
    
    def _insert_non_full(self, node, key, value):
        if node.leaf:
            node.keys.append((key, value))
            node.keys.sort(key=lambda x: x[0])
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i][0]:
                i -= 1
            i += 1
            
            if len(node.children[i].keys) == (2 * self.order) - 1:
                self.split_child(node, i)
                if key > node.keys[i][0]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)
    
    def range_search(self, low, high, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and node.keys[i][0] < low:
            i += 1
        
        while i < len(node.keys) and node.keys[i][0] <= high:
            if not node.leaf:
                self.range_search(low, high, node.children[i], result)
            result.append(node.keys[i])
            i += 1
        
        if not node.leaf:
            self.range_search(low, high, node.children[i], result)
        
        return result

# สร้าง B-Tree สำหรับระบบทะเบียน
registration_system = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })

# เพิ่มข้อมูลตัวอย่าง
register_student(6301, {
    "name": "สมชาย ใจดี",
    "gpa": 3.75,
    "courses": ["CS101", "CS102"]
})

register_student(6302, {
    "name": "สมหญิง รักเรียน",
    "gpa": 3.85,
    "courses": ["CS101", "MATH101"]
})

# ค้นหาข้อมูลนักศึกษา
def get_student_info(student_id):
    student = registration_system.search(student_id)
    if student:
        print(f"รหัสนักศึกษา: {student_id}")
        print(f"ชื่อ: {student['name']}")
        print(f"เกรดเฉลี่ย: {student['gpa']}")
        print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
    else:
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

# ค้นหานักศึกษาในช่วงรหัสที่กำหนด
def get_students_in_range(low, high):
    students = registration_system.range_search(low, high)
    for student_id, info in students:
        print(f"รหัสนักศึกษา: {student_id}")
        print(f"ชื่อ: {info['name']}")
        print(f"เกรดเฉลี่ย: {info['gpa']}")
        print(f"วิชาที่ลงทะเบียน: {', '.join(info['courses'])}")
        print("-")

# ทดสอบค้นหาแบบช่วง
get_students_in_range(6301, 6302)