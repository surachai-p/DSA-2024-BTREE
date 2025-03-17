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
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2
        self.max_keys = order - 1
    
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
        
        if not child.leaf:
            new_node.children = child.children[mid + 1:]
        
        parent.keys.insert(i, child.keys[mid])
        parent.data.insert(i, child.data[mid])
        parent.children.insert(i + 1, new_node)
        
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]
        if not child.leaf:
            child.children = child.children[:mid + 1]
    
    def search(self, key, node=None):
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]
        
        if node.leaf:
            return None
        
        return self.search(key, node.children[i])
    
    def update(self, key, new_data, node=None):
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            node.data[i] = new_data
            return True
        
        if node.leaf:
            return False
        
        return self.update(key, new_data, node.children[i])
    
    def delete(self, key, node=None):
        if node is None:
            node = self.root
        
        if node is None:
            return
        
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and node.keys[i] == key:
            if node.leaf:
                del node.keys[i]
                del node.data[i]
            else:
                node.keys[i] = node.children[i + 1].keys[0]
                node.data[i] = node.children[i + 1].data[0]
                self.delete(node.keys[i], node.children[i + 1])
        elif not node.leaf:
            self.delete(key, node.children[i])
    
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
    
    def print_tree(self, node=None):
        if node is None:
            node = self.root
        
        print("Keys:", node.keys, "Data:", node.data)
        for child in node.children:
            self.print_tree(child)

# สร้าง B-Tree ที่มี order = 3
btree = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
students = [
    (1, "กรรณิการ์"),
    (2, "อัศวิน"),
    (3, "ปราบปราม"),
    (4, "ข้าวเกรียบ"),
    (5, "ปากหม้อ")
]

for student_id, name in students:
    btree.insert(student_id, name)

# แสดงผลต้นไม้
btree.print_tree()

# ทดสอบการค้นหาข้อมูล
search_keys = [1, 3, 5, 6]
for key in search_keys:
    result = btree.search(key)
    if result:
        print(f"พบข้อมูลสำหรับรหัส {key}: {result}")
    else:
        print(f"ไม่พบข้อมูลสำหรับรหัส {key}")

# ทดสอบการแสดงโครงสร้าง B-Tree
btree.display()

# ทดสอบการอัปเดตข้อมูล
update_entries = [(3, "นักรบ"), (5, "ขนมจีบ")]
for key, new_data in update_entries:
    if btree.update(key, new_data):
        print(f"อัปเดตข้อมูลรหัส {key} เป็น {new_data}")
    else:
        print(f"ไม่พบข้อมูลรหัส {key} สำหรับอัปเดต")
    btree.display()

# ทดสอบการลบข้อมูล
delete_keys = [3, 5]
for key in delete_keys:
    print(f"\nลบข้อมูลรหัส {key}")
    btree.delete(key)
    btree.display()
