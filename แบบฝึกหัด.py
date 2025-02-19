class BTreeNode:
    def __init__(self, is_leaf=True, max_entries=3):
        self.is_leaf = is_leaf
        self.max_entries = max_entries
        self.min_entries = (max_entries + 1) // 2
        self.keys = []
        self.values = []
        self.children = []

    def is_full(self):
        return len(self.keys) >= self.max_entries

class BTree:
    def __init__(self, max_entries=3):
        self.root = BTreeNode(max_entries=max_entries)
        self.max_entries = max_entries
        self.min_entries = (max_entries + 1) // 2

    def insert(self, key, value):
        root = self.root
        if root.is_full():
            new_root = BTreeNode(is_leaf=False, max_entries=self.max_entries)
            new_root.children.append(self.root)
            self.root = new_root
            self.split_child(new_root, 0)
        self.insert_non_full(self.root, key, value)

    def split_child(self, parent, index):
        child = parent.children[index]
        mid_index = len(child.keys) // 2
        mid_key = child.keys[mid_index]
        mid_value = child.values[mid_index]

        new_child = BTreeNode(is_leaf=child.is_leaf, max_entries=self.max_entries)
        new_child.keys = child.keys[mid_index + 1:]
        new_child.values = child.values[mid_index + 1:]
        child.keys = child.keys[:mid_index]
        child.values = child.values[:mid_index]

        if not child.is_leaf:
            new_child.children = child.children[mid_index + 1:]
            child.children = child.children[:mid_index + 1]

        parent.keys.insert(index, mid_key)
        parent.values.insert(index, mid_value)
        parent.children.insert(index + 1, new_child)

    def insert_non_full(self, node, key, value):
        if node.is_leaf:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            node.keys.insert(index, key)
            node.values.insert(index, value)
        else:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            if node.children[index].is_full():
                self.split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key, value)

    def print_tree(self, node=None, level=0, indent="    "):
        if node is None:
            node = self.root
        print(indent * level + f"Level {level} Keys: {node.keys}")
        for child in node.children:
            self.print_tree(child, level + 1, indent)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        for i in range(len(node.keys)):
            if not node.is_leaf:
                result.extend(self.inorder_traversal(node.children[i]))
            result.append((node.keys[i], node.values[i]))
        if not node.is_leaf:
            result.extend(self.inorder_traversal(node.children[-1]))
        return result

    def update(self, key, new_value, node=None):
        if node is None:
            node = self.root
        for i in range(len(node.keys)):
            if node.keys[i] == key:
                node.values[i] = new_value
                return True
            elif key < node.keys[i] and not node.is_leaf:
                return self.update(key, new_value, node.children[i])
        if not node.is_leaf:
            return self.update(key, new_value, node.children[-1])
        return False

    def range_search(self, low, high, node=None):
        if node is None:
            node = self.root
        result = []
        for i in range(len(node.keys)):
            if not node.is_leaf:
                result.extend(self.range_search(low, high, node.children[i]))
            if low <= node.keys[i] <= high:
                result.append((node.keys[i], node.values[i]))
        if not node.is_leaf:
            result.extend(self.range_search(low, high, node.children[-1]))
        return result

btree = BTree(max_entries=3)
students = []

for i in range(5):
    print(f"กรุณากรอกข้อมูลนักศึกษาคนที่ {i+1}:")
    name = input("ชื่อ: ")
    student_id = int(input("รหัสนักศึกษา: "))
    student = {"name": name, "StudentID": student_id}
    students.append(student)
    btree.insert(student_id, student)


print("\nโครงสร้าง B-Tree:")
btree.print_tree()


print("\nข้อมูลนักศึกษาทั้งหมดเรียงตามรหัส:")
for key, value in btree.inorder_traversal():
    print(f"รหัสนักศึกษา: {key}, ชื่อ: {value['name']}")


update_key = int(input("\nกรุณากรอกรหัสนักศึกษาที่ต้องการอัปเดต: "))
new_name = input("ชื่อใหม่: ")
if btree.update(update_key, {"name": new_name, "StudentID": update_key}):
    print("อัปเดตสำเร็จ")
else:
    print("ไม่พบรหัสนักศึกษา")


low = int(input("\nกรุณากรอกรหัสนักศึกษาต่ำสุดของช่วง: "))
high = int(input("กรุณากรอกรหัสนักศึกษาสูงสุดของช่วง: "))
print("\nผลลัพธ์การค้นหาช่วง:")
for key, value in btree.range_search(low, high):
    print(f"รหัสนักศึกษา: {key}, ชื่อ: {value['name']}")
