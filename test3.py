class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.data = []
        self.children = []

class BTree:
    def __init__(self, order):
        self.root = None
        self.order = order
        self.min_entries = (order + 1) // 2 - 1  # จำนวน key ขั้นต่ำ
        self.max_entries = order - 1             # จำนวน key สูงสุด

    def insert(self, key, data):
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return

        if len(self.root.keys) == self.max_entries:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key, data)

    def _insert_non_full(self, node, key, data):
        i = len(node.keys) - 1
        if node.leaf:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.data.insert(i + 1, data)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.max_entries:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        order = self.order
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = len(child.keys) // 2

        parent.keys.insert(i, child.keys[mid])
        parent.data.insert(i, child.data[mid])
        parent.children.insert(i + 1, new_node)

        new_node.keys = child.keys[mid + 1:]
        new_node.data = child.data[mid + 1:]
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]

        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]
            
def search(self, key):
    def _search_node(node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]
        if node.leaf:
            return None
        return _search_node(node.children[i], key)

    return _search_node(self.root, key) if self.root else None

BTree.search = search

def display(self):
    def _display(node, level=0):
        if node:
            print("  " * level + f"Keys: {node.keys}")
            print("  " * level + f"Data: {[d['name'] for d in node.data]}")
            for child in node.children:
                _display(child, level + 1)
    _display(self.root)

BTree.display = display


    
# สร้าง B-Tree
btree = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
students = [
    (6301, {"name": "สมชาย ใจดี", "gpa": 3.75, "courses": ["CS101", "CS102"]}),
    (6302, {"name": "สมหญิง รักเรียน", "gpa": 3.85, "courses": ["CS101", "MATH101"]}),
    (6303, {"name": "ศรสวรรค์ จันทสุวรรณโณ", "gpa": 3.60, "courses": ["CS103", "CS104"]}),
    (6304, {"name": "สายรุ้ง มั่นคง", "gpa": 3.90, "courses": ["CS101", "ENG101"]}),
    (6305, {"name": "มานะ พากเพียร", "gpa": 3.65, "courses": ["CS102", "MATH102"]})
]

for student_id, info in students:
    btree.insert(student_id, info)

def register_student(student_id, info):
    btree.insert(student_id, info)

def get_student_info(student_id):
    student = btree.search(student_id)
    if student:
        print(f"รหัส: {student_id} | ชื่อ: {student['name']} | GPA: {student['gpa']} | วิชา: {', '.join(student['courses'])}")
    else:
        print("ไม่พบข้อมูลนักศึกษา")

get_student_info(6303)