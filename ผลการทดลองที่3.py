class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # เป็นใบหรือไม่
        self.keys = []  # คีย์ที่เก็บในโหนด
        self.children = []  # ลูกของโหนดนี้
        self.data = []  # ข้อมูลที่เก็บคู่กับคีย์

class BTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        """ค้นหาข้อมูลจาก key ที่กำหนด"""
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

# สร้าง B-Tree และเพิ่มข้อมูลทดสอบ
btree = BTree()
root = BTreeNode(leaf=True)
root.keys = [10, 20, 30, 40]
root.data = ['a', 'b', 'c','d']  # เก็บข้อมูลคู่กับคีย์
btree.root = root

# ทดสอบการค้นหา
print(btree.search(10))  # ควรได้ 'a'
print(btree.search(20))  # ควรได้ 'b'
print(btree.search(30))  # ควรได้ 'c'
print(btree.search(40))  # ควรได้ 'd'
print(btree.search(25))  # ควรได้ None (ไม่มีข้อมูล)