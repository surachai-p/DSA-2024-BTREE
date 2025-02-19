class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # เป็นโหนดใบหรือไม่
        self.keys = []  # รายการคีย์ในโหนด
        self.data = []  # ข้อมูลที่สอดคล้องกับคีย์ (ถ้ามี)
        self.children = []  # รายการลูกของโหนด

class BTree:
    def __init__(self):
        self.root = BTreeNode(leaf=True)  # เริ่มต้นด้วยโหนดรากที่เป็นใบ

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

# สร้างและทดสอบ B-Tree
btree = BTree()
btree.root.keys = [1, 2, 3]
btree.root.data = ['A', 'B', 'C']

# เพิ่มโหนดลูก (สมมติว่าแบ่งออกเป็นสองโหนดลูก)
left_child = BTreeNode(leaf=True)
left_child.keys = [5, 7]
left_child.data = ['Y', 'Z']

right_child = BTreeNode(leaf=True)
right_child.keys = [25, 35]
right_child.data = ['N', 'O']

btree.root.children = [left_child, right_child]
btree.root.leaf = False  # ตอนนี้ root ไม่ใช่ใบอีกต่อไป

# แสดงโครงสร้างของ B-Tree
btree.display()
