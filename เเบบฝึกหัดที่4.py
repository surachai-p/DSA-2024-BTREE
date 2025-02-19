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
        order = self.order
        child = parent.children[i]
        new_node = BTreeNode(child.leaf)
        mid = order // 2
        
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
        if result:
            node, index = result
            return node.data[index]
        return None

    def delete(self, key):
        if self.root is None:
            print("B-Tree is empty")
            return
        
        self._delete_from_node(self.root, key)
        
        if len(self.root.keys) == 0:
            if not self.root.leaf:
                self.root = self.root.children[0]
            else:
                self.root = None

    def _delete_from_node(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            if node.leaf:
                node.keys.pop(i)
                node.data.pop(i)
            else:
                self._delete_internal_node(node, i)
        elif not node.leaf:
            self._delete_from_node(node.children[i], key)
    
    def _delete_internal_node(self, node, i):
        key = node.keys[i]
        child = node.children[i]
        
        if len(child.keys) > self.min_keys:
            predecessor_key = self._get_predecessor(child)
            node.keys[i] = predecessor_key
            self._delete_from_node(child, predecessor_key)
        elif len(node.children[i+1].keys) > self.min_keys:
            successor_key = self._get_successor(node.children[i+1])
            node.keys[i] = successor_key
            self._delete_from_node(node.children[i+1], successor_key)
        else:
            self._merge_nodes(node, i)
            self._delete_from_node(child, key)

    def _get_predecessor(self, node):
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _get_successor(self, node):
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def _merge_nodes(self, parent, i):
        left = parent.children[i]
        right = parent.children[i+1]
        mid_key = parent.keys[i]
        mid_data = parent.data[i]

        left.keys.append(mid_key)
        left.data.append(mid_data)
        left.keys.extend(right.keys)
        left.data.extend(right.data)
        left.children.extend(right.children)

        parent.keys.pop(i)
        parent.data.pop(i)
        parent.children.pop(i+1)

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

    def update(self, key, new_data):
        """
        อัปเดตข้อมูลสำหรับ key ที่กำหนด
        """
        if self.root is None:
            print("B-Tree is empty")
            return
        
        # ค้นหาคีย์ใน B-Tree
        result = self._search_node(self.root, key)
        
        if result:
            node, index = result
            node.data[index] = new_data  # อัปเดตข้อมูล
            print(f"ข้อมูลของรหัสนักศึกษารหัส {key} ถูกอัปเดตแล้ว.")
        else:
            print(f"ไม่พบรหัสนักศึกษารหัส {key} ใน B-Tree.")

    def _search_node(self, node, key):
        """
        ค้นหาคีย์ในโหนด (จะใช้ในฟังก์ชัน update)
        """
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        
        if node.leaf:
            return None
        
        return self._search_node(node.children[i], key)

    def display_sorted(self):
        """
        แสดงข้อมูลทั้งหมดใน B-Tree เรียงตาม key
        """
        def _in_order_traversal(node):
            result = []
            if node:
                for i in range(len(node.keys)):
                    # แสดงข้อมูลในลูกซ้ายของโหนดก่อน
                    if not node.leaf:
                        result.extend(_in_order_traversal(node.children[i]))
                    # แสดง key และ data ของโหนดนี้
                    result.append((node.keys[i], node.data[i]))
                # แสดงข้อมูลในลูกขวาสุด
                if not node.leaf:
                    result.extend(_in_order_traversal(node.children[len(node.keys)]))
            return result

        # เรียกใช้การ traversal เพื่อให้ได้ผลลัพธ์ที่เรียงลำดับ
        sorted_data = _in_order_traversal(self.root)
        
        print("ข้อมูลทั้งหมดใน B-Tree (เรียงตาม key):")
        for key, data in sorted_data:
            print(f"Key: {key} -> Data: {data}")

    def range_search(self, key1, key2):
        """
        ค้นหาข้อมูลในช่วง [key1, key2]
        """
        result = []

        def _range_search_node(node):
            if node:
                for i in range(len(node.keys)):
                    if key1 <= node.keys[i] <= key2:
                        result.append((node.keys[i], node.data[i]))
                    if not node.leaf:
                        if node.keys[i] > key1:
                            _range_search_node(node.children[i])
                if not node.leaf:
                    _range_search_node(node.children[len(node.keys)])
        
        _range_search_node(self.root)
        
        return result


# ตัวอย่างการใช้งาน
btree = BTree(order=3)

# เพิ่มข้อมูลนักศึกษาผ่านฟังก์ชัน
btree.insert(6301, {"name": "สมชาย ใจดี", "gpa": 3.75, "courses": ["CS101", "CS102"]})
btree.insert(6302, {"name": "สมหญิง รักเรียน", "gpa": 3.85, "courses": ["CS101", "MATH101"]})
btree.insert(6303, {"name": "สุนารี สดใส", "gpa": 3.60, "courses": ["CS102", "CS201"]})
btree.insert(6304, {"name": "สมปอง ยิ้มแย้ม", "gpa": 3.90, "courses": ["CS101", "MATH101"]})

# ค้นหาข้อมูลในช่วง
key1 = 6302
key2 = 6304
print(f"ข้อมูลในช่วงจาก {key1} ถึง {key2}:")
result = btree.range_search(key1, key2)
for key, data in result:
    print(f"Key: {key} -> Data: {data}")
