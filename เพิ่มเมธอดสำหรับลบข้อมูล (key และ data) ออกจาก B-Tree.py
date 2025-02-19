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
        self.max_keys = order - 1  # จำนวน key สูงสุดที่แต่ละโหนดมีได้
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2  # จำนวน key ขั้นต่ำที่โหนดต้องมี

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
            return node.data[i]  # คืนข้อมูลที่ตรงกับ key
        
        if node.leaf:
            return None  # หากไม่เจอ key ในใบ
    
        return self._search_node(node.children[i], key)

    def delete(self, key):
        self._delete(self.root, key)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            if node.leaf:
                del node.keys[i]
                del node.data[i]
            else:
                if len(node.children[i].keys) > self.min_keys:
                    predecessor = self._get_predecessor(node.children[i])
                    node.keys[i], node.data[i] = predecessor
                    self._delete(node.children[i], predecessor[0])
                elif len(node.children[i + 1].keys) > self.min_keys:
                    successor = self._get_successor(node.children[i + 1])
                    node.keys[i], node.data[i] = successor
                    self._delete(node.children[i + 1], successor[0])
                else:
                    self._merge_nodes(node, i)
                    self._delete(node.children[i], key)
        else:
            if node.leaf:
                return  
            if len(node.children[i].keys) <= self.min_keys:
                if i > 0 and len(node.children[i - 1].keys) > self.min_keys:
                    self._borrow_from_sibling(node, i - 1, True)
                elif i < len(node.children) - 1 and len(node.children[i + 1].keys) > self.min_keys:
                    self._borrow_from_sibling(node, i, False)
                else:
                    self._merge_nodes(node, i if i < len(node.keys) else i - 1)
            self._delete(node.children[i], key)

    def _get_predecessor(self, node):
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1], node.data[-1]

    def _get_successor(self, node):
        while not node.leaf:
            node = node.children[0]
        return node.keys[0], node.data[0]

    def _merge_nodes(self, parent, idx):
        child = parent.children[idx]
        sibling = parent.children[idx + 1]
        child.keys.append(parent.keys[idx])
        child.data.append(parent.data[idx])

        child.keys.extend(sibling.keys)
        child.data.extend(sibling.data)
        if not child.leaf:
            child.children.extend(sibling.children)

        del parent.keys[idx]
        del parent.data[idx]
        del parent.children[idx + 1]

    def _borrow_from_sibling(self, parent, idx, left_sibling):
        if left_sibling:
            child = parent.children[idx + 1]
            sibling = parent.children[idx]
            key = sibling.keys.pop()
            data = sibling.data.pop()
            child.keys.insert(0, parent.keys[idx])
            child.data.insert(0, parent.data[idx])
            parent.keys[idx] = key
            parent.data[idx] = data
            if not sibling.leaf:
                child.children.insert(0, sibling.children.pop())
        else:
            child = parent.children[idx]
            sibling = parent.children[idx + 1]
            key = sibling.keys.pop(0)
            data = sibling.data.pop(0)
            child.keys.append(parent.keys[idx])
            child.data.append(parent.data[idx])
            parent.keys[idx] = key
            parent.data[idx] = data
            if not sibling.leaf:
                child.children.append(sibling.children.pop(0))

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        for child in node.children:
            self.print_tree(child, level + 1)

# สร้าง B-Tree
registration_system = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
register_student = lambda sid, info: registration_system.insert(sid, info)
register_student(6301, {"name": "สมชาย", "gpa": 3.75, "courses": ["CS101", "CS102"]})
register_student(6302, {"name": "สมหญิง", "gpa": 3.85, "courses": ["CS101", "MATH101"]})

# ค้นหา
def get_student_info(student_id):
    student = registration_system.search(student_id)
    print(student if student else f"ไม่พบข้อมูล {student_id}")

# ทดสอบลบ
print("\n🔹 ก่อนลบ:")
registration_system.print_tree()

registration_system.delete(6301)

print("\n🔹 หลังลบ:")
registration_system.print_tree()
