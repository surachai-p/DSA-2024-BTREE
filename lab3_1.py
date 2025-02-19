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
        """ค้นหาข้อมูลจาก key ที่กำหนด"""
        node = self.root
        while node:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return node.data[i]
            if node.leaf:
                return None
            node = node.children[i]
        return None

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        for child in node.children:
            self.print_tree(child, level + 1)

# สร้าง B-Tree ที่มี order = 3
btree = BTree(order=3)

# เพิ่มข้อมูลนักศึกษาแบบกำหนดเอง
students = [
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie"),
    (104, "David"),
    (105, "Eve"),
]

for student_id, student_name in students:
    btree.insert(student_id, student_name)

# แสดงโครงสร้างของ B-Tree
print("\nB-Tree Structure:")
btree.print_tree()

# ทดสอบการค้นหาข้อมูล
print("\nTesting Search Function")
while True:
    search_key = int(input("\nEnter Student ID to search (or -1 to quit): "))
    if search_key == -1:
        break
    result = btree.search(search_key)
    if result:
        print(f"Found: ID {search_key} -> Name: {result}")
    else:
        print(f"Not Found: ID {search_key}")
