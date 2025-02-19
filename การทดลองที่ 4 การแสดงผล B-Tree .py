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
        self.max_keys = order - 1  # จำนวนคีย์สูงสุดใน node
        self.min_keys = order // 2  # จำนวนคีย์ต่ำสุดใน node

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

    def search(self, key):
        """ค้นหาข้อมูลจาก key ที่กำหนด"""
        def _search_node(node, key):
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
            return _search_node(node.children[i], key)
        
        if self.root is None:
            return None
            
        result = _search_node(self.root, key)
        if result:
            node, index = result
            return node.data[index]
        return None

    def print_tree(self, node, level=0):
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

    def display(self):
        def _display(node, level):
            if node:
                # แสดง key และ data ในโหนดปัจจุบัน
                print('  ' * level + f"Keys: {node.keys}")
                print('  ' * level + f"Data: {node.data}")
                print('  ' * level + f"Is Leaf: {node.leaf}")
                print('  ' * level + f"Number of children: {len(node.children)}")
                print()
                # แสดงลูกทุกตัวแบบ recursive
                for child in node.children:
                    _display(child, level + 1)
        
        print("B-Tree Structure:")
        _display(self.root, 0)

# ทดสอบการแสดงข้อมูลใน B-Tree
btree = BTree(3)
students = [(101, "Alice"), (102, "Bob"), (103, "Charlie"), (104, "David"), (105, "Eve")]
for sid, name in students:
    btree.insert(sid, name)

# แสดงผลโครงสร้าง B-Tree
btree.display()
