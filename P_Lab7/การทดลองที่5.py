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
        new_node = BTreeNode(child.leaf)
        mid = len(child.keys) // 2

        new_node.keys = child.keys[mid+1:]
        new_node.data = child.data[mid+1:]
        mid_key = child.keys[mid]
        mid_data = child.data[mid]
        child.keys = child.keys[:mid]
        child.data = child.data[:mid]

        if not child.leaf:
            new_node.children = child.children[mid+1:]
            child.children = child.children[:mid+1]

        parent.keys.insert(i, mid_key)
        parent.data.insert(i, mid_data)
        parent.children.insert(i + 1, new_node)

    def search(self, key):
        def _search_node(node, key):
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1

            if i < len(node.keys) and key == node.keys[i]:
                return (node, i)

            if node.leaf:
                return None

            return _search_node(node.children[i], key)

        if self.root is None:
            return None

        result = _search_node(self.root, key)
        return result[0].data[result[1]] if result else None

    def delete(self, key):
        """ลบ key และ data ออกจาก B-Tree"""
        def _delete_node(node, key):
            if node is None:
                return None

            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1

            if i < len(node.keys) and node.keys[i] == key:
                if node.leaf:
                    node.keys.pop(i)
                    node.data.pop(i)
                else:
                    # TODO: กรณีโหนดไม่ใช่ใบ
                    pass
            elif not node.leaf:
                node.children[i] = _delete_node(node.children[i], key)

            return node

        if self.root:
            self.root = _delete_node(self.root, key)

    def update(self, key, new_data):
        """อัปเดตข้อมูลของ key ที่กำหนด"""
        node_data = self.search(key)
        if node_data:
            # สมมติว่า new_data เป็น dict ที่ต้องการอัปเดตข้อมูล
            node_data.clear()
            node_data.update(new_data)
        else:
            print(f"ไม่พบข้อมูลของ key {key}")

    def inorder_traversal(self, node=None):
        """แสดงข้อมูลทั้งหมดเรียงตาม key"""
        if node is None:
            node = self.root

        if node:
            for i in range(len(node.keys)):
                if not node.leaf:
                    self.inorder_traversal(node.children[i])
                print(f"Key: {node.keys[i]}, Data: {node.data[i]}")
            if not node.leaf:
                self.inorder_traversal(node.children[-1])

    def range_search(self, key_min, key_max):
        """ค้นหาข้อมูลที่อยู่ในช่วง key_min ถึง key_max"""
        result = []

        def _range_search(node):
            if node:
                for i in range(len(node.keys)):
                    if key_min <= node.keys[i] <= key_max:
                        result.append((node.keys[i], node.data[i]))
                    if not node.leaf and node.keys[i] > key_max:
                        break
                if not node.leaf:
                    _range_search(node.children[-1])

        _range_search(self.root)
        return result

# สร้าง B-Tree สำหรับระบบทะเบียนนักศึกษา
registration_system = BTree(order=3)

# ฟังก์ชันสำหรับเพิ่มข้อมูลนักศึกษา
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })

# ฟังก์ชันสำหรับค้นหาข้อมูลนักศึกษา
def get_student_info(student_id):
    student = registration_system.search(student_id)
    if student:
        print(f"รหัสนักศึกษา: {student_id}")
        print(f"ชื่อ: {student['name']}")
        print(f"เกรดเฉลี่ย: {student['gpa']}")
        print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
    else:
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

# ฟังก์ชันสำหรับแสดงข้อมูลทั้งหมดเรียงตาม key
def display_registration_system():
    registration_system.inorder_traversal()

# Export ฟังก์ชันและตัวแปรที่ต้องการให้ใช้ในไฟล์อื่น
__all__ = [
    "registration_system",
    "register_student",
    "get_student_info",
    "display_registration_system"
]