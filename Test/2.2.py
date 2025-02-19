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
        self.MIN_KEYS = (order // 2) - 1 if order % 2 == 0 else order // 2
        self.MAX_KEYS = order - 1

    def insert(self, key, data):
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return
        
        if len(self.root.keys) == self.MAX_KEYS:
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
            
            if len(node.children[i].keys) == self.MAX_KEYS:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
                    
            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = self.order // 2
        
        mid_key = child.keys[mid]
        mid_data = child.data[mid]
        
        new_node.keys = child.keys[mid+1:]
        new_node.data = child.data[mid+1:]
        
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]
        
        if not child.leaf:
            new_node.children = child.children[mid+1:]
            child.children = child.children[:mid+1]
        
        parent.keys.insert(i, mid_key)
        parent.data.insert(i, mid_data)
        parent.children.insert(i + 1, new_node)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

# สร้าง B-Tree ที่มี order 3
btree = BTree(order=3)

# รับข้อมูลนักศึกษาจากผู้ใช้
num_students = int(input("ป้อนจำนวนนักศึกษา: "))
for _ in range(num_students):
    sid = int(input("ป้อนรหัสนักศึกษา: "))
    name = input("ป้อนชื่อนักศึกษา: ")
    btree.insert(sid, name)

# แสดงโครงสร้างของ B-Tree
btree.display()
