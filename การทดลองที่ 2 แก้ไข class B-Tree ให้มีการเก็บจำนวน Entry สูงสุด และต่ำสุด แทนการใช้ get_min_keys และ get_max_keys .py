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
        # หาก root เป็น None, สร้าง node ใหม่
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return
        
        # ถ้า root เต็ม, ทำการ split
        if len(self.root.keys) == self.max_keys:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        
        # ทำการแทรกข้อมูลใน node ที่ไม่เต็ม
        self._insert_non_full(self.root, key, data)

    def _insert_non_full(self, node, key, data):
        i = len(node.keys) - 1
        
        if node.leaf:
            # ค้นหาตำแหน่งที่จะแทรก key
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            node.keys.insert(i, key)
            node.data.insert(i, data)
        else:
            # ค้นหาตำแหน่งที่จะแทรก key ใน child node
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            # ถ้า child เต็ม, ต้อง split
            if len(node.children[i].keys) == self.max_keys:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
                    
            # แทรกข้อมูลใน child ที่ไม่เต็ม
            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        child = parent.children[i]
        mid = len(child.keys) // 2  # คำนวณตำแหน่งกลาง
        
        new_node = BTreeNode(child.leaf)
        new_node.keys = child.keys[mid + 1:]  # คัดลอกค่าจากกลางขึ้นไป
        new_node.data = child.data[mid + 1:]
        
        moving_key = child.keys[mid]  # คีย์กลางที่จะย้ายขึ้นไป
        moving_data = child.data[mid]
        
        child.keys = child.keys[:mid]  # เอาคีย์ก่อนกลาง
        child.data = child.data[:mid]
        
        if not child.leaf:
            new_node.children = child.children[mid + 1:]  # ย้ายลูกของ child
            child.children = child.children[:mid + 1]
        
        # เพิ่ม key และ child ใหม่ขึ้นไปใน parent
        parent.keys.insert(i, moving_key)
        parent.data.insert(i, moving_data)
        parent.children.insert(i + 1, new_node)

    def print_tree(self, node, level=0):
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# สร้าง B-Tree และเพิ่มข้อมูลนักศึกษา
btree = BTree(3)  # กำหนด order ของ B-Tree เป็น 3
students = [(101, "Getzy"), (102, "Gartoon"), (103, "Ghimmy"), (104, "Pun"), (105, "Pao")]
for sid, name in students:
    btree.insert(sid, name)

# แสดงผล B-Tree
btree.print_tree(btree.root)
