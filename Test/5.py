class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.data = []

class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        self.order = order

    def insert(self, key, data):
        root = self.root
        if len(root.keys) == (2 * self.order) - 1:
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self.insert_non_full(self.root, key, data)
    
    def insert_non_full(self, node, key, data):
        if node.leaf:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            node.keys.insert(index, key)
            node.data.insert(index, data)
        else:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            if len(node.children[index].keys) == (2 * self.order) - 1:
                self.split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key, data)
    
    def split_child(self, parent, index):
        order = self.order
        node = parent.children[index]
        new_node = BTreeNode(node.leaf)
        mid = order - 1
        
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)
        new_node.keys = node.keys[mid + 1:]
        new_node.data = node.data[mid + 1:]
        node.keys = node.keys[:mid]
        node.data = node.data[:mid]
        
        if not node.leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]
    
    def search(self, key, node=None):
        if node is None:
            node = self.root
        
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
        
        if index < len(node.keys) and key == node.keys[index]:
            return node.data[index]
        
        if node.leaf:
            return None
        
        return self.search(key, node.children[index])
    
    def delete(self, key):
        self.root = self.delete_rec(self.root, key)

    def delete_rec(self, node, key):
        if node is None:
            return node
        if key in node.keys:
            index = node.keys.index(key)
            if node.leaf:
                node.keys.pop(index)
                node.data.pop(index)
            else:
                node.keys.pop(index)
                node.data.pop(index)
                node.children.pop(index + 1)
        else:
            for i, k in enumerate(node.keys):
                if key < k:
                    node.children[i] = self.delete_rec(node.children[i], key)
                    return node
            node.children[-1] = self.delete_rec(node.children[-1], key)
        return node
    
    def update(self, key, new_data):
        node = self.root
        while node:
            for i, k in enumerate(node.keys):
                if key == k:
                    node.data[i] = new_data
                    return True
            if node.leaf:
                return False
            node = node.children[-1]
        return False
    
    def display(self, node=None):
        if node is None:
            node = self.root
        for i, key in enumerate(node.keys):
            if not node.leaf:
                self.display(node.children[i])
            print(f"{key}: {node.data[i]}")
        if not node.leaf:
            self.display(node.children[-1])
    
    def range_search(self, min_key, max_key, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        for i, key in enumerate(node.keys):
            if min_key <= key <= max_key:
                result.append((key, node.data[i]))
            if not node.leaf and key > min_key:
                self.range_search(min_key, max_key, node.children[i], result)
        if not node.leaf:
            self.range_search(min_key, max_key, node.children[-1], result)
        return result

# สร้างระบบทะเบียน
registration_system = BTree(order=3)

def register_student(student_id, info):
    registration_system.insert(student_id, info)

def get_student_info(student_id):
    student = registration_system.search(student_id)
    if student:
        print(f"รหัสนักศึกษา: {student_id}, ชื่อ: {student['name']}, เกรดเฉลี่ย: {student['gpa']}, วิชา: {', '.join(student['courses'])}")
    else:
        print(f"ไม่พบข้อมูลนักศึกษา {student_id}")

def delete_student(student_id):
    registration_system.delete(student_id)

def update_student(student_id, new_info):
    success = registration_system.update(student_id, new_info)
    if not success:
        print("ไม่พบข้อมูลสำหรับอัปเดต")

def show_all_students():
    registration_system.display()

def search_students_in_range(min_id, max_id):
    result = registration_system.range_search(min_id, max_id)
    for key, data in result:
        print(f"รหัสนักศึกษา: {key}, ชื่อ: {data['name']}, เกรดเฉลี่ย: {data['gpa']}")

# ทดสอบการทำงาน
register_student(66030238, {"name": "ณัฐนันท์", "gpa": 4.00, "courses": ["CS101", "CS102"]})
register_student(66030243, {"name": "ณัฏฐณิชชา", "gpa": 3.99, "courses": ["CS101", "MATH101"]})
get_student_info(66030238)
delete_student(66030238)
show_all_students()
search_students_in_range(6300, 6400)
