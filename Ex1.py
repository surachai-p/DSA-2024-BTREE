class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []  # เก็บเป็น Tuple (key, value)
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
            while i >= 0 and key < node.keys[i][0]:
                i -= 1
            node.keys.insert(i + 1, (key, data))
        else:
            while i >= 0 and key < node.keys[i][0]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.max_keys:
                self._split_child(node, i)
                if key > node.keys[i][0]:
                    i += 1
            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = len(child.keys) // 2
        mid_key = child.keys[mid]
        new_node.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]

        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

        parent.keys.insert(i, mid_key)
        parent.children.insert(i + 1, new_node)

    def search(self, key):
        node = self.root
        while node:
            i = 0
            while i < len(node.keys) and key > node.keys[i][0]:
                i += 1
            if i < len(node.keys) and key == node.keys[i][0]:
                return node.keys[i][1]
            if node.leaf:
                return None
            node = node.children[i]
        return None

    def delete(self, key):
        """ลบ key และข้อมูลออกจาก B-Tree"""
        if not self.root:
            return
        self._delete_recursive(self.root, key)
        if not self.root.keys and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete_recursive(self, node, key):
        """ลบ key ออกจากโหนดที่กำหนด"""
        i = 0
        while i < len(node.keys) and key > node.keys[i][0]:
            i += 1
        
        if i < len(node.keys) and node.keys[i][0] == key:
            if node.leaf:
                node.keys.pop(i)
            else:
                node.keys[i] = self._get_predecessor(node.children[i])
                self._delete_recursive(node.children[i], node.keys[i][0])
        elif not node.leaf:
            if len(node.children[i].keys) <= self.min_keys:
                self._merge_nodes(node, i)
            self._delete_recursive(node.children[i], key)

    def _get_predecessor(self, node):
        """ดึง key ก่อนหน้า (predecessor)"""
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _merge_nodes(self, parent, i):
        """รวมโหนดเมื่อมี key น้อยเกินไป"""
        child = parent.children[i]
        sibling = parent.children[i + 1] if i + 1 < len(parent.children) else parent.children[i - 1]
        child.keys.append(parent.keys.pop(i))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        parent.children.pop(i + 1 if i + 1 < len(parent.children) else i)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", [f"({k}, {v})" for k, v in node.keys])
        for child in node.children:
            self.print_tree(child, level + 1)

# ---- ระบบทะเบียนนักศึกษา ----
btree = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
students = [
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie"),
    (104, "David"),
    (105, "Emma"),
]

for student_id, student_name in students:
    btree.insert(student_id, student_name)

print("\nB-Tree Structure BEFORE delete:")
btree.print_tree()

# ลบข้อมูลนักศึกษา
print("\n--- Deleting ID 103 ---")
btree.delete(103)

print("\nB-Tree Structure AFTER delete:")
btree.print_tree()

# ทดสอบการค้นหาข้อมูล
print("\nTesting Search Function")
test_keys = [102, 103, 105]
for search_key in test_keys:
    result = btree.search(search_key)
    if result:
        print(f"Found: ID {search_key} -> Name: {result}")
    else:
        print(f"Not Found: ID {search_key}")
