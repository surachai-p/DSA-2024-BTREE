class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # ตรวจสอบว่าเป็นใบหรือไม่
        self.keys = []  # เก็บคีย์ของโหนด
        self.data = []  # เก็บข้อมูลของโหนด (สามารถปรับเปลี่ยนตามต้องการ)
        self.children = []  # เก็บลูกของโหนด

class BTree:
    def __init__(self):
        self.root = BTreeNode(leaf=True)  # เริ่มต้นด้วยโหนดรากเป็นใบ
    
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

# ทดสอบสร้าง B-Tree และแสดงข้อมูล
btree = BTree()

# เพิ่มข้อมูลตัวอย่าง
btree.root.keys = [10, 20, 30]
btree.root.data = ['A', 'B', 'C']

# สร้างโหนดลูกและเพิ่มเข้าไปในต้นไม้
child1 = BTreeNode(leaf=True)
child1.keys = [5]
child1.data = ['X']

child2 = BTreeNode(leaf=True)
child2.keys = [15]
child2.data = ['Y']

child3 = BTreeNode(leaf=True)
child3.keys = [25, 35]
child3.data = ['Z', 'W']

btree.root.children = [child1, child2, child3]
btree.root.leaf = False

# แสดงโครงสร้าง B-Tree
btree.display()
