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

 def display(self):
     def _display(node, level):
         if node:
             print('  ' * level + f"Keys: {node.keys}")
             print('  ' * level + f"Data: {node.data}")
             print('  ' * level + f"Is Leaf: {node.leaf}")
             print('  ' * level + f"Number of children: {len(node.children)}")
             print()
             for child in node.children:
                 _display(child, level + 1)
 
     print("B-Tree Structure:")
     _display(self.root, 0)

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
 "name": "เอย",
 "gpa": 3.75,
 "courses": ["CS101", "CS102"]
})

register_student(6302, {
 "name": "อารีน่า",
 "gpa": 3.85,
 "courses": ["CS101", "MATH101"]
})

register_student(6303, {
 "name": "อัง",
 "gpa": 3.50,
 "courses": ["CS102", "ENG101"]
})

register_student(6304, {
 "name": "เนย",
 "gpa": 3.95,
 "courses": ["CS103", "CS104"]
})

register_student(6305, {
 "name": "ตุรกี",
 "gpa": 3.60,
 "courses": ["MATH102", "ENG101"]
})

# แสดงโครงสร้างของ B-Tree
registration_system.display()