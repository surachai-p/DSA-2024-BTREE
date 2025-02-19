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

    def delete(self, key):
        """ลบข้อมูลจาก B-Tree โดยใช้ key"""
        if self.root is None:
            print("B-Tree is empty.")
            return

        self._delete(self.root, key)

    def _delete(self, node, key):
        index = self._find_key(node, key)
        
        if index is not None:
            # ถ้าโหนดเป็นใบ
            if node.leaf:
                node.keys.pop(index)
                node.data.pop(index)
            else:
                self._delete_internal_node(node, key, index)
        else:
            if node.leaf:
                print(f"ไม่พบข้อมูลที่ต้องการลบ (key: {key})")
                return

            child = node.children[index]
            if len(child.keys) > self.min_keys:
                self._delete(child, key)
            else:
                self._handle_underflow(node, index)
                self._delete(node.children[index], key)

    def _find_key(self, node, key):
        """ค้นหาคีย์ในโหนด"""
        for i, k in enumerate(node.keys):
            if k == key:
                return i
            elif k > key:
                break
        return None

    def _delete_internal_node(self, node, key, index):
        child = node.children[index]
        
        if len(child.keys) > self.min_keys:
            self._delete(child, key)
        else:
            self._handle_underflow(node, index)
            self._delete(node.children[index], key)

    def _handle_underflow(self, node, index):
        """จัดการเมื่อโหนดลูกมีจำนวนคีย์ต่ำเกินไป"""
        child = node.children[index]
        sibling = node.children[index + 1] if index + 1 < len(node.children) else node.children[index - 1]
        
        if len(sibling.keys) > self.min_keys:
            self._borrow_from_sibling(node, index)
        else:
            self._merge_nodes(node, index)

    def _borrow_from_sibling(self, node, index):
        """ยืมคีย์จาก sibling"""
        child = node.children[index]
        sibling = node.children[index + 1] if index + 1 < len(node.children) else node.children[index - 1]
        
        if index + 1 < len(node.children):
            child.keys.append(node.keys[index])
            child.data.append(node.data[index])
            node.keys[index] = sibling.keys.pop(0)
            node.data[index] = sibling.data.pop(0)
        else:
            sibling.keys.append(node.keys[index - 1])
            sibling.data.append(node.data[index - 1])
            node.keys[index - 1] = child.keys.pop(0)
            node.data[index - 1] = child.data.pop(0)

    def _merge_nodes(self, node, index):
        """รวมโหนดที่อยู่ในสถานะไม่สมบูรณ์"""
        child = node.children[index]
        sibling = node.children[index + 1] if index + 1 < len(node.children) else node.children[index - 1]
        
        child.keys.append(node.keys.pop(index))
        child.data.append(node.data.pop(index))
        child.keys.extend(sibling.keys)
        child.data.extend(sibling.data)
        
        if not child.leaf:
            child.children.extend(sibling.children)
        
        node.children.pop(index + 1 if index + 1 < len(node.children) else index)

    def update(self, key, new_data):
        """อัปเดตข้อมูลที่ตรงกับ key"""
        node, index = self._search_for_update(self.root, key)
        if node:
            node.data[index] = new_data
            print(f"ข้อมูลของคีย์ {key} ได้รับการอัปเดตแล้ว")
        else:
            print(f"ไม่พบข้อมูลสำหรับคีย์ {key}")

    def _search_for_update(self, node, key):
        """ค้นหาคีย์ใน B-Tree เพื่อทำการอัปเดต"""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
            
        # ถ้าเจอ key ที่ตรงกัน
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
            
        # ถ้าเป็นใบและไม่เจอ key
        if node.leaf:
            return None
            
        # ค้นหาในลูกที่เหมาะสม
        return self._search_for_update(node.children[i], key)

    def display(self):
        """แสดงข้อมูล B-Tree ทั้งหมด"""
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

# เพิ่มข้อมูลตัวอย่าง
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })

register_student(6301, {
    "name": "เปา บีตอง",
    "gpa": 3.75,
    "courses": ["CS101", "CS102"]
})

register_student(6302, {
    "name": "กิม เหย",
    "gpa": 3.85,
    "courses": ["CS101", "MATH101"]
})

# อัปเดตข้อมูลนักศึกษารหัส 6301
registration_system.update(6301, {
    "name": "เปา บีตอง",
    "gpa": 3.90,
    "courses": ["CS101", "CS102", "CS201"]
})

# แสดงโครงสร้าง B-Tree หลังการอัปเดต
registration_system.display()
