class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.data = []
        self.children = []

class BTree:
    def __init__(self, order):
        self.root = BTreeNode()
        self.order = order
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

    def insert(self, key, data):
        if len(self.root.keys) == self.max_keys:
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
            i += 1
            node.keys.insert(i, key)
            node.data.insert(i, data)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.max_keys:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = len(child.keys) // 2  
        mid_key = child.keys[mid]
        mid_data = child.data[mid]

        new_node.keys = child.keys[mid + 1:]
        new_node.data = child.data[mid + 1:]
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]

        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

        parent.keys.insert(i, mid_key)
        parent.data.insert(i, mid_data)
        parent.children.insert(i + 1, new_node)

    def search(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]  
        
        if node.leaf:
            return None  
    
        return self._search_node(node.children[i], key)
    
    def update(self, key, new_data):
        node = self.root
        while node:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            
            if i < len(node.keys) and key == node.keys[i]:
                node.data[i] = new_data  # อัปเดตข้อมูลใหม่
                return True
            
            if node.leaf:
                return False  # ไม่พบ key
            
            node = node.children[i]
        return False

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

# ฟังก์ชันอัปเดตข้อมูล
def update_student(student_id, new_info):
    success = registration_system.update(student_id, new_info)
    if success:
        print(f"อัปเดตข้อมูลของนักศึกษารหัส {student_id} สำเร็จ")
    else:
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

# อัปเดตข้อมูลตัวอย่าง
update_student(6301, {
    "name": "สมชาย สุขใจ",
    "gpa": 3.90,
    "courses": ["CS201", "CS202"]
})