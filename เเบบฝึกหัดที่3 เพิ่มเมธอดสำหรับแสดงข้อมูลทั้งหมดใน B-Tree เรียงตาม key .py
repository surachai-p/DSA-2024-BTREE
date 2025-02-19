class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.data = []
        self.children = []

class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        self.order = order
        self.max_keys = order - 1
        self.min_keys = order // 2

    def insert(self, key, data):
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return
        
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
        mid = len(child.keys) // 2
        
        new_node = BTreeNode(child.leaf)
        new_node.keys = child.keys[mid + 1:]
        new_node.data = child.data[mid + 1:]
        
        moving_key = child.keys[mid]
        moving_data = child.data[mid]
        
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]
        
        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]
        
        parent.keys.insert(i, moving_key)
        parent.data.insert(i, moving_data)
        parent.children.insert(i + 1, new_node)

    def display_in_order(self):
        """แสดงข้อมูลทั้งหมดใน B-Tree ตามลำดับ key"""
        result = []
        
        def _in_order_traversal(node):
            if node:
                # เดินทางในลูกซ้ายสุดก่อน
                for i in range(len(node.keys)):
                    if not node.leaf:
                        _in_order_traversal(node.children[i])
                    # เก็บข้อมูล (key, data) ในลำดับที่ถูกต้อง
                    result.append((node.keys[i], node.data[i]))
                if not node.leaf:
                    _in_order_traversal(node.children[-1])

        _in_order_traversal(self.root)
        
        # แสดงผลข้อมูลทั้งหมดที่เก็บไว้ใน result
        for key, data in result:
            print(f"Key: {key}, Data: {data}")

# สร้าง B-Tree สำหรับระบบทะเบียน
registration_system = BTree(order=3)

# เพิ่มข้อมูลตัวอย่าง
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })

register_student(6301, {
    "name": "ณัฐนันท์ ",
    "gpa": 3.75,
    "courses": ["CS101", "CS102"]
})

register_student(6302, {
    "name": "สุวพัชร",
    "gpa": 3.85,
    "courses": ["CS101", "MATH101"]
})

register_student(6303, {
    "name": "จิรสิน",
    "gpa": 3.50,
    "courses": ["CS102", "MATH102"]
})

# แสดงข้อมูลทั้งหมดใน B-Tree เรียงตาม key
registration_system.display_in_order()
