class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.data = []
        self.children = []

class BTree:
    def __init__(self, order):
        self.order = order
        self.max_entries = order - 1  # จำนวนคีย์สูงสุด
        self.min_entries = (order // 2) - 1  # จำนวนคีย์ต่ำสุด
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return

        if len(self.root.keys) == self.max_entries:
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

            if len(node.children[i].keys) == self.max_entries:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key, data)

    def _split_child(self, parent, i):
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = self.order // 2

        new_node.keys = child.keys[mid + 1:]
        new_node.data = child.data[mid + 1:]

        if not child.leaf:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

        parent.keys.insert(i, child.keys[mid])
        parent.data.insert(i, child.data[mid])
        parent.children.insert(i + 1, new_node)

        child.keys = child.keys[:mid]
        child.data = child.data[:mid]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        for child in node.children:
            self.print_tree(child, level + 1)

# สร้าง B-Tree โดยกำหนด order เป็น 3
btree = BTree(order=3)

# รับข้อมูลนักศึกษา 5 คนจากผู้ใช้
students = []
for _ in range(5):
    sid = int(input("ป้อนรหัสนักศึกษา: "))
    name = input("ป้อนชื่อนักศึกษา: ")
    students.append((sid, name))

for sid, name in students:
    btree.insert(sid, name)

# แสดงโครงสร้างของ B-Tree
btree.print_tree()
