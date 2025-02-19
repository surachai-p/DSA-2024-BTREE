# ใบงานการทดลอง: B-Tree

## วัตถุประสงค์
1. เพื่อให้นักศึกษาเข้าใจโครงสร้างและหลักการทำงานของ B-Tree
2. เพื่อให้นักศึกษาสามารถสร้างและจัดการ B-Tree ที่มี Order ต่างๆ ได้
3. เพื่อให้นักศึกษาสามารถประยุกต์ใช้ B-Tree ในการจัดเก็บและค้นหาข้อมูลได้
4. เพื่อให้นักศึกษาเข้าใจการทำงานของ splitting และ merging ใน B-Tree

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. โปรแกรม IDE หรือ Text Editor ที่รองรับการเขียนโปรแกรมภาษา Python
3. ใบงานการทดลอง

## ทฤษฎีที่เกี่ยวข้อง

### B-Tree คืออะไร
B-Tree เป็นโครงสร้างข้อมูลแบบต้นไม้ที่ถูกออกแบบมาเพื่อการจัดเก็บข้อมูลในหน่วยความจำสำรอง โดยสามารถเก็บข้อมูล (data) คู่กับค่าคีย์ (key) ในแต่ละโหนดได้ ทำให้สามารถค้นหาและเข้าถึงข้อมูลได้อย่างมีประสิทธิภาพ

### Order ใน B-Tree
Order (m) คือค่าที่กำหนดขนาดของโหนดใน B-Tree โดยมีผลต่อคุณสมบัติต่างๆ ดังนี้:

1. จำนวนคู่ key-data ในแต่ละโหนด:
   - จำนวนสูงสุด: m-1 คู่
   - จำนวนต่ำสุด: ⌈m/2⌉-1 คู่ (ยกเว้น root)
   
2. จำนวนลูกในแต่ละโหนด:
   - จำนวนลูกสูงสุด: m ลูก
   - จำนวนลูกต่ำสุด: ⌈m/2⌉ ลูก (ยกเว้น root)

ตัวอย่าง: B-Tree order 3
- แต่ละโหนดมี key ได้มากที่สุด 2 ตัว (3-1)
- แต่ละโหนดมี key ขั้นต่ำ 1 ตัว (⌈3/2⌉-1)
- แต่ละโหนดมีลูกได้มากที่สุด 3 โหนด
- แต่ละโหนดต้องมีลูกอย่างน้อย 2 โหนด (⌈3/2⌉)

### การจัดเก็บข้อมูลใน B-Tree
1. ลักษณะการเก็บข้อมูล:
   - B-Tree สามารถเก็บข้อมูล (data) ไว้กับ key ได้ในทุกโหนด
   - แต่ละ key จะมี data field ที่เก็บข้อมูลหรือ pointer ไปยังข้อมูลจริง
   - การค้นหาข้อมูลสามารถพบได้ตั้งแต่ root node

2. เปรียบเทียบกับ B+ Tree:
   
   B-Tree:
   - เก็บข้อมูลได้ในทุกโหนด
   - ค้นหาข้อมูลเจอได้เร็วกว่าถ้าข้อมูลอยู่ในโหนดบน
   - ใช้พื้นที่น้อยกว่าในการเก็บข้อมูล
   - เหมาะกับการค้นหาข้อมูลแบบ random access

   B+ Tree:
   - เก็บข้อมูลเฉพาะที่ leaf nodes
   - โหนดภายในเก็บเฉพาะ key สำหรับนำทาง
   - มี linked list เชื่อมระหว่าง leaf nodes
   - เหมาะกับการค้นหาแบบ range query

### ผลของ Order ต่อประสิทธิภาพ
1. Order น้อย (เช่น 3, 4):
   - ข้อดี: ใช้หน่วยความจำน้อย, การเพิ่ม/ลบข้อมูลทำได้เร็ว
   - ข้อเสีย: ต้นไม้อาจสูง, การค้นหาอาจช้า

2. Order มาก (เช่น 100, 200):
   - ข้อดี: ต้นไม้เตี้ย, การค้นหาเร็ว
   - ข้อเสีย: ใช้หน่วยความจำมาก, การเพิ่ม/ลบข้อมูลอาจช้า

### การนำ B-Tree ไปใช้งานจริง
1. ระบบจัดการฐานข้อมูล (Database Management Systems)
   - MySQL ใช้ B-Tree และ B+Tree ในการสร้าง Index
   - PostgreSQL ใช้ B-Tree สำหรับ Primary Key และ Index
   - Oracle Database ใช้ B-Tree ในการจัดการ Index

2. ระบบจัดการคลังสินค้า (Inventory Management Systems)
   - จัดการรหัสสินค้า (SKU) และตำแหน่งจัดเก็บ
   - ติดตามสต็อกสินค้าแบบ real-time
   - ระบบค้นหาสินค้าที่ใกล้หมดอายุ

3. ระบบทะเบียนนักศึกษา (Student Registration Systems)
   - จัดการรหัสนักศึกษาและประวัติการเรียน
   - ระบบลงทะเบียนเรียน
   - ระบบตรวจสอบผลการเรียน

4. ระบบไฟล์ (File Systems)
   - NTFS ของ Windows
   - HFS+ ของ Mac OS X
   - Ext4 ของ Linux

5. ระบบ DNS (Domain Name System)
   - จัดเก็บและค้นหา domain name
   - ระบบ cache สำหรับ DNS resolver

### คุณสมบัติทั่วไปของ B-Tree
- เป็น Self-balancing tree (ปรับสมดุลตัวเองอัตโนมัติ)
- ทุกใบ (leaf) อยู่ในระดับเดียวกัน
- จำนวนลูกของแต่ละโหนดจะมากกว่าจำนวน key เสมอ 1 ตัว
- ข้อมูลใน key จะเรียงจากน้อยไปมากจากซ้ายไปขวา
- ลูกทางซ้ายของ key จะมีค่าน้อยกว่า key
- ลูกทางขวาของ key จะมีค่ามากกว่า key
- สามารถเก็บข้อมูลได้ในทุกโหนด ไม่จำกัดเฉพาะ leaf nodes

## การทดลอง

### การทดลองที่ 1: การสร้าง B-Tree Node และ B-Tree

```python
class BTreeNode:
    def __init__(self, leaf=True):
        # leaf: บอกว่าโหนดนี้เป็นใบหรือไม่
        self.leaf = leaf
        # keys: เก็บค่า key ในโหนด เรียงจากน้อยไปมาก
        self.keys = []
        # data: เก็บข้อมูลที่สัมพันธ์กับแต่ละ key
        self.data = []
        # children: เก็บ pointer ไปยังลูกของโหนด
        self.children = []

class BTree:
    def __init__(self, order):
        # root: pointer ไปยังโหนด root
        self.root = None
        # order: กำหนดจำนวน key สูงสุดในแต่ละโหนด
        self.order = order
        
    def get_min_keys(self):
        # คำนวณจำนวน key ขั้นต่ำที่แต่ละโหนดต้องมี
        return (self.order // 2) - 1 if self.order % 2 == 0 else self.order // 2
        
    def get_max_keys(self):
        # คำนวณจำนวน key สูงสุดที่แต่ละโหนดสามารถมีได้
        return self.order - 1
```

### การทดลองที่ 2: การเพิ่มข้อมูลใน B-Tree

```python
def insert(self, key, data):
    # ถ้ายังไม่มี root
    if self.root is None:
        self.root = BTreeNode()
        self.root.keys.append(key)
        self.root.data.append(data)
        return
        
    # ถ้า root เต็ม
    if len(self.root.keys) == self.get_max_keys():
        new_root = BTreeNode(leaf=False)
        new_root.children.append(self.root)
        self._split_child(new_root, 0)
        self.root = new_root
        
    self._insert_non_full(self.root, key, data)

def _insert_non_full(self, node, key, data):
    i = len(node.keys) - 1
    
    if node.leaf:
        # หาตำแหน่งที่จะแทรก key และ data
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        node.keys.insert(i, key)
        node.data.insert(i, data)
    else:
        # หา child ที่เหมาะสม
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        
        if len(node.children[i].keys) == self.get_max_keys():
            self._split_child(node, i)
            if key > node.keys[i]:
                i += 1
                
        self._insert_non_full(node.children[i], key, data)

def _split_child(self, parent, i):
    order = self.order
    child = parent.children[i]
    
    # สร้างโหนดใหม่
    new_node = BTreeNode(child.leaf)
    
    # คำนวณตำแหน่งกลาง (แก้ไขจากเดิม)
    mid = (order - 1) // 2
    
    # ย้าย keys และ data ไปยังโหนดใหม่
    new_node.keys = child.keys[mid+1:]  # แก้ไขจากเดิม
    new_node.data = child.data[mid+1:]  # แก้ไขจากเดิม
    
    # เก็บค่า key และ data ตรงกลางไว้
    mid_key = child.keys[mid]
    mid_data = child.data[mid]
    
    # ตัด keys และ data ของโหนดเดิม
    child.keys = child.keys[:mid]
    child.data = child.data[:mid]
    
    # ถ้าไม่ใช่ใบ ต้องย้ายลูกด้วย
    if not child.leaf:
        new_node.children = child.children[mid+1:]  # แก้ไขจากเดิม
        child.children = child.children[:mid+1]     # แก้ไขจากเดิม
    
    # เพิ่ม key และ data ตรงกลางไปยัง parent
    parent.keys.insert(i, mid_key)
    parent.data.insert(i, mid_data)
    parent.children.insert(i + 1, new_node)
```
### ผลการทดลองที่ 2
1. เขียนโปรแกรมเพื่อเพิ่มข้อมูลนักศึกษา 5 คน รันโปรแกรมและบันทึกรูปผลการรันโปรแกรม
   ```python
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
        
    def get_min_keys(self):
        return (self.order // 2) - 1 if self.order % 2 == 0 else self.order // 2
        
    def get_max_keys(self):
        return self.order - 1

    def insert(self, key, data):
        if self.root is None:
            self.root = BTreeNode()
            self.root.keys.append(key)
            self.root.data.append(data)
            return
        
        if len(self.root.keys) == self.get_max_keys():
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
            
            if len(node.children[i].keys) == self.get_max_keys():
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

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

   #สร้าง B-Tree ที่มี order 3
   btree = BTree(order=3)

   #รับข้อมูลนักศึกษาจากผู้ใช้
   num_students = int(input("ป้อนจำนวนนักศึกษา: "))
   for _ in range(num_students):
    sid = int(input("ป้อนรหัสนักศึกษา: "))
    name = input("ป้อนชื่อนักศึกษา: ")
    btree.insert(sid, name)

   #แสดงโครงสร้างของ B-Tree
   btree.display()
   ```
   ![image](https://github.com/user-attachments/assets/55ee0f47-4eb7-4845-b7b7-165d4ed9d5a1)

2. แก้ไข class B-Tree ให้มีการเก็บจำนวน Entry สูงสุด และต่ำสุด แทนการใช้ get_min_keys และ get_max_keys
   ```python
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
        self.max_keys = order - 1  # 🔹 ค่ามากสุดที่แต่ละโหนดมีได้
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2  # 🔹 ค่าน้อยสุดที่โหนดต้องมี

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
        mid = self.order // 2  # 🔹 ใช้ self.order แทน

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

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

      # สร้าง B-Tree ที่มี order 3
      btree = BTree(order=3)
      
      # รับข้อมูลนักศึกษาจากผู้ใช้
      num_students = int(input("ป้อนจำนวนนักศึกษา: "))
      for _ in range(num_students):
          sid = int(input("ป้อนรหัสนักศึกษา: "))
          name = input("ป้อนชื่อนักศึกษา: ")
          btree.insert(sid, name)
      
      # แสดงโครงสร้างของ B-Tree
      btree.display()


   ```
   
   ![image](https://github.com/user-attachments/assets/a90244eb-519d-436f-9a20-f220d30d3aea)



### การทดลองที่ 3: การค้นหาข้อมูลใน B-Tree

```python
def search(self, key):
    """ค้นหาข้อมูลจาก key ที่กำหนด"""
    def _search_node(node, key):
        i = 0
        # หาตำแหน่งที่เหมาะสม
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
            
        # ถ้าเจอ key ที่ตรงกัน
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
            
        # ถ้าเป็นใบและไม่เจอ key
        if node.leaf:
            return None
            
        # ค้นหาในลูกที่เหมาะสม
        return _search_node(node.children[i], key)
    
    if self.root is None:
        return None
        
    result = _search_node(self.root, key)
    if result:
        node, index = result
        return node.data[index]
    return None
```
### ผลการทดลอง
1. เขียนโปรแกรมเพื่อทดสอบการค้นหาข้อมูลใน B-Tree ตามข้อมูลที่ได้เพิ่มในการทดลองก่อนหน้า
   ```python
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
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
        mid = self.order // 2

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

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

    def search(self, key, node=None):
        """ ค้นหาข้อมูลใน B-Tree ตามรหัสนักศึกษา """
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]  # พบข้อมูล, คืนค่าชื่อนักศึกษา

        if node.leaf:
            return None  # ไม่พบข้อมูลในโหนดใบ

        return self.search(key, node.children[i])  # ค้นหาต่อในโหนดลูก

      # สร้าง B-Tree ที่มี order 3
      btree = BTree(order=3)
      
      # รับข้อมูลนักศึกษาจากผู้ใช้
      num_students = int(input("ป้อนจำนวนนักศึกษา: "))
      for _ in range(num_students):
          sid = int(input("ป้อนรหัสนักศึกษา: "))
          name = input("ป้อนชื่อนักศึกษา: ")
          btree.insert(sid, name)

      # แสดงโครงสร้างของ B-Tree
      btree.display()
      
      # ทดสอบการค้นหาข้อมูล
      search_id = int(input("\nป้อนรหัสนักศึกษาที่ต้องการค้นหา: "))
      result = btree.search(search_id)
      
      if result:
          print(f"พบข้อมูล: รหัส {search_id}, ชื่อ {result}")
      else:
          print(f"ไม่พบรหัสนักศึกษา {search_id}")


   ```
  ![image](https://github.com/user-attachments/assets/0494adb3-980a-4e5e-b31d-217bbc4762f7)

### การทดลองที่ 4: การแสดงผล B-Tree

```python
def display(self):
    def _display(node, level):
        if node:
            # แสดง key และ data ในโหนดปัจจุบัน
            print('  ' * level + f"Keys: {node.keys}")
            print('  ' * level + f"Data: {node.data}")
            print('  ' * level + f"Is Leaf: {node.leaf}")
            print('  ' * level + f"Number of children: {len(node.children)}")
            print()
            # แสดงลูกทุกตัวแบบ recursive
            for child in node.children:
                _display(child, level + 1)
    
    print("B-Tree Structure:")
    _display(self.root, 0)
```
### ผลการทดลอง
1. เขียนโปรแกรมเพื่อทดสอบการแสดงข้อมูลใน B-Tree 
   ```python
   class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []      # เก็บรหัสนักศึกษา (Key)
        self.data = []      # เก็บชื่อนักศึกษา (Value)
        self.children = []  # เก็บโหนดลูก (ถ้ามี)

   class BTree:
    def __init__(self, order):
        self.root = None
        self.order = order
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
        mid = self.order // 2

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

    def display(self, node=None, level=0):
        """ แสดงโครงสร้างของ B-Tree แบบเป็นลำดับชั้น """
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys, 'Data:', node.data)
        for child in node.children:
            self.display(child, level + 1)

    def display_all_data(self, node=None):
        """ แสดงข้อมูลนักศึกษาทั้งหมดใน B-Tree """
        if node is None:
            node = self.root
        if node.leaf:
            for i in range(len(node.keys)):
                print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
        else:
            for i in range(len(node.keys)):
                self.display_all_data(node.children[i])
                print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
            self.display_all_data(node.children[-1])

      # สร้าง B-Tree ที่มี order = 3
      btree = BTree(order=3)
      
      # รับข้อมูลนักศึกษาจากผู้ใช้
      num_students = int(input("ป้อนจำนวนนักศึกษา: "))
      for _ in range(num_students):
          sid = int(input("ป้อนรหัสนักศึกษา: "))
          name = input("ป้อนชื่อนักศึกษา: ")
          btree.insert(sid, name)
      
      # แสดงโครงสร้างของ B-Tree
      print("\n🔹 โครงสร้างของ B-Tree:")
      btree.display()
      
      # แสดงข้อมูลนักศึกษาทั้งหมด
      print("\n🔹 รายชื่อนักศึกษาที่ถูกเก็บใน B-Tree:")
      btree.display_all_data()
      

   ```
   ![image](https://github.com/user-attachments/assets/2923f61c-c268-4246-8746-1b119a55643b)

### การทดลองที่ 5: ตัวอย่างการใช้งานจริง :ระบบทะเบียนนักศึกษา

```python
# สร้าง B-Tree สำหรับระบบทะเบียน
registration_system = BTree(order=3)

# เพิ่มข้อมูลนักศึกษา
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })

# เพิ่มข้อมูลตัวอย่าง
register_student(6301, {
    "name": "สมชาย ใจดี",
    "gpa": 3.75,
    "courses": ["CS101", "CS102"]
})

register_student(6302, {
    "name": "สมหญิง รักเรียน",
    "gpa": 3.85,
    "courses": ["CS101", "MATH101"]
})

# ค้นหาข้อมูลนักศึกษา
def get_student_info(student_id):
    student = registration_system.search(student_id)
    if student:
        print(f"รหัสนักศึกษา: {student_id}")
        print(f"ชื่อ: {student['name']}")
        print(f"เกรดเฉลี่ย: {student['gpa']}")
        print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
    else:
        print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")

# ทดสอบค้นหา
get_student_info(6301)
```

## แบบฝึกหัด
1. ให้นักศึกษาเพิ่มเมธอดสำหรับลบข้อมูล (key และ data) ออกจาก B-Tree
 ```python
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
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
        mid = self.order // 2

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

    def search(self, key, node=None):
        """ ค้นหาข้อมูลจาก B-Tree """
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]

        if node.leaf:
            return None

        return self.search(key, node.children[i])

    def delete(self, key, node=None):
        """ ลบ key และ data ออกจาก B-Tree """
        if self.root is None:
            print("ต้นไม้ไม่มีข้อมูลให้ลบ")
            return

        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # 🔹 1. ถ้า key อยู่ในโหนดปัจจุบัน
        if i < len(node.keys) and node.keys[i] == key:
            if node.leaf:
                # 🔸 ถ้าเป็นโหนดใบ ลบ key ได้เลย
                del node.keys[i]
                del node.data[i]
            else:
                # 🔸 ถ้าเป็นโหนดภายใน ใช้ Predecessor หรือ Successor
                if len(node.children[i].keys) >= self.min_keys + 1:
                    pred_key, pred_data = self._get_predecessor(node.children[i])
                    node.keys[i], node.data[i] = pred_key, pred_data
                    self.delete(pred_key, node.children[i])
                elif len(node.children[i+1].keys) >= self.min_keys + 1:
                    succ_key, succ_data = self._get_successor(node.children[i+1])
                    node.keys[i], node.data[i] = succ_key, succ_data
                    self.delete(succ_key, node.children[i+1])
                else:
                    # 🔸 รวมโหนดถ้าทั้งสองลูกมี key น้อยเกินไป
                    self._merge_nodes(node, i)
                    self.delete(key, node.children[i])
        else:
            # 🔹 2. ถ้า key ไม่อยู่ในโหนดปัจจุบัน ให้ค้นหาในโหนดลูกที่เหมาะสม
            if node.leaf:
                print(f"ไม่พบรหัส {key} ใน B-Tree")
                return

            child = node.children[i]
            if len(child.keys) == self.min_keys:
                self._balance_child(node, i)

            self.delete(key, node.children[i])

    def display(self, node=None, level=0):
        """ แสดงโครงสร้างของ B-Tree """
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

      #  สร้าง B-Tree สำหรับระบบทะเบียน
      registration_system = BTree(order=3)
      
      #  เพิ่มข้อมูลนักศึกษา
      def register_student(student_id, info):
          registration_system.insert(student_id, {
              "name": info["name"],
              "gpa": info["gpa"],
              "courses": info["courses"]
          })
      
      #  ลบข้อมูลนักศึกษา
      def delete_student(student_id):
          registration_system.delete(student_id)
          print(f"ลบรหัสนักศึกษา {student_id} สำเร็จ")
      
      #  ค้นหาข้อมูลนักศึกษา
      def get_student_info(student_id):
          student = registration_system.search(student_id)
          if student:
              print(f"\nรหัสนักศึกษา: {student_id}")
              print(f"ชื่อ: {student['name']}")
              print(f"เกรดเฉลี่ย: {student['gpa']}")
              print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
          else:
              print(f"\nไม่พบข้อมูลนักศึกษารหัส {student_id}")
      
      #  เพิ่มข้อมูลตัวอย่าง
      register_student(6301, {
          "name": "สมชาย ใจดี",
          "gpa": 3.75,
          "courses": ["CS101", "CS102"]
      })
      
      register_student(6302, {
          "name": "สมหญิง รักเรียน",
          "gpa": 3.85,
          "courses": ["CS101", "MATH101"]
      })
      
      #  แสดงโครงสร้าง B-Tree
      print("\n🔹 โครงสร้าง B-Tree ก่อนลบ:")
      registration_system.display()
      
      #  ทดสอบลบข้อมูล
      delete_student(6301)
      
      #  แสดงโครงสร้าง B-Tree หลังลบ
      print("\n🔹 โครงสร้าง B-Tree หลังลบ:")
      registration_system.display()
      
      #  ทดสอบค้นหาหลังลบ
      get_student_info(6301)
      get_student_info(6302)
      

```

![image](https://github.com/user-attachments/assets/9adf7cb7-32b2-40b8-943e-4d00730c4fa6)

2. ให้นักศึกษาเพิ่มเมธอดสำหรับอัปเดตข้อมูล (data) สำหรับ key ที่กำหนด
 ```python
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
       self.max_keys = order - 1
       self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
       mid = self.order // 2

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

   def search(self, key, node=None):
       if node is None:
           node = self.root
       i = 0
       while i < len(node.keys) and key > node.keys[i]:
           i += 1

       if i < len(node.keys) and key == node.keys[i]:
           return node.data[i]

       if node.leaf:
           return None

       return self.search(key, node.children[i])

   def update(self, key, new_data, node=None):
       """ อัปเดตข้อมูลของ Key ที่กำหนด """
       if node is None:
           node = self.root
       
       i = 0
       while i < len(node.keys) and key > node.keys[i]:
           i += 1
       
       if i < len(node.keys) and node.keys[i] == key:
           node.data[i] = new_data  # 🔹 อัปเดตข้อมูลใหม่
           print(f"อัปเดตรหัสนักศึกษา {key} สำเร็จ")
           return True

       if node.leaf:
           print(f"ไม่พบรหัสนักศึกษา {key} ใน B-Tree")
           return False

       return self.update(key, new_data, node.children[i])

   def display(self, node=None, level=0):
       """ แสดงโครงสร้างของ B-Tree """
       if node is None:
           node = self.root
       print('Level', level, 'Keys:', node.keys)
       for child in node.children:
           self.display(child, level + 1)
      
      # ✅ สร้าง B-Tree สำหรับระบบทะเบียน
      registration_system = BTree(order=3)
      
      # ✅ เพิ่มข้อมูลนักศึกษา
      def register_student(student_id, info):
          registration_system.insert(student_id, {
              "name": info["name"],
              "gpa": info["gpa"],
              "courses": info["courses"]
          })
      
      # ✅ อัปเดตข้อมูลนักศึกษา
      def update_student(student_id, new_info):
          success = registration_system.update(student_id, {
              "name": new_info["name"],
              "gpa": new_info["gpa"],
              "courses": new_info["courses"]
          })
          
          if not success:
              print(f"ไม่สามารถอัปเดตข้อมูลนักศึกษารหัส {student_id} ได้")
      
      # ✅ ลบข้อมูลนักศึกษา
      def delete_student(student_id):
          registration_system.delete(student_id)
          print(f"ลบรหัสนักศึกษา {student_id} สำเร็จ")
      
      # ✅ ค้นหาข้อมูลนักศึกษา
      def get_student_info(student_id):
          student = registration_system.search(student_id)
          if student:
              print(f"\nรหัสนักศึกษา: {student_id}")
              print(f"ชื่อ: {student['name']}")
              print(f"เกรดเฉลี่ย: {student['gpa']}")
              print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
          else:
              print(f"\nไม่พบข้อมูลนักศึกษารหัส {student_id}")
      
      # ✅ เพิ่มข้อมูลตัวอย่าง
      register_student(6301, {
          "name": "สมชาย ใจดี",
          "gpa": 3.75,
          "courses": ["CS101", "CS102"]
      })
      
      register_student(6302, {
          "name": "สมหญิง รักเรียน",
          "gpa": 3.85,
          "courses": ["CS101", "MATH101"]
      })
      
      # ✅ แสดงโครงสร้าง B-Tree ก่อนอัปเดต
      print("\n🔹 โครงสร้าง B-Tree ก่อนอัปเดต:")
      registration_system.display()
      
      # ✅ อัปเดตข้อมูลนักศึกษา 6301
      update_student(6301, {
          "name": "สมชาย แก้ไข",
          "gpa": 3.90,
          "courses": ["CS201", "CS202"]
      })
      
      # ✅ แสดงโครงสร้าง B-Tree หลังอัปเดต
      print("\n🔹 โครงสร้าง B-Tree หลังอัปเดต:")
      registration_system.display()
      
      # ✅ ทดสอบค้นหาหลังอัปเดต
      get_student_info(6301)
      get_student_info(6302)

```

![image](https://github.com/user-attachments/assets/40764abe-f589-41d9-94a8-2299b42ac674)

3. ให้นักศึกษาเพิ่มเมธอดสำหรับแสดงข้อมูลทั้งหมดใน B-Tree เรียงตาม key
 ```python
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
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
        mid = self.order // 2

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

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node.data[i]
        if node.leaf:
            return None
        return self.search(key, node.children[i])

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys)
        for child in node.children:
            self.display(child, level + 1)

# ✅ สร้าง B-Tree สำหรับระบบทะเบียน
registration_system = BTree(order=3)

# ✅ เพิ่มข้อมูลนักศึกษา
def register_student(student_id, info):
    registration_system.insert(student_id, {
        "name": info["name"],
        "gpa": info["gpa"],
        "courses": info["courses"]
    })
      
      # ✅ ค้นหาข้อมูลนักศึกษา
      def get_student_info(student_id):
          student = registration_system.search(student_id)
          if student:
              print(f"รหัสนักศึกษา: {student_id}")
              print(f"ชื่อ: {student['name']}")
              print(f"เกรดเฉลี่ย: {student['gpa']}")
              print(f"วิชาที่ลงทะเบียน: {', '.join(student['courses'])}")
          else:
              print(f"ไม่พบข้อมูลนักศึกษารหัส {student_id}")
      
      # ✅ แสดงข้อมูลนักศึกษาทั้งหมด (เรียงตาม Key)
      def display_sorted(node=None):
          if node is None:
              node = registration_system.root
          if node:
              for i in range(len(node.keys)):
                  if not node.leaf:
                      display_sorted(node.children[i])
                  print(f"รหัสนักศึกษา: {node.keys[i]}, ข้อมูล: {node.data[i]}")
              if not node.leaf:
                  display_sorted(node.children[-1])
          else:
              print("B-Tree ว่างเปล่า ไม่มีข้อมูล")
      
      # ✅ เพิ่มข้อมูลตัวอย่าง
      register_student(6301, {"name": "สมชาย ใจดี", "gpa": 3.75, "courses": ["CS101", "CS102"]})
      register_student(6302, {"name": "สมหญิง รักเรียน", "gpa": 3.85, "courses": ["CS101", "MATH101"]})
      
      # ✅ แสดงข้อมูลทั้งหมด (เรียงตามรหัสนักศึกษา)
      print("\n🔹 รายชื่อนักศึกษาทั้งหมด (เรียงตามรหัสนักศึกษา):")
      display_sorted()
      

```

![image](https://github.com/user-attachments/assets/e4370670-4819-445c-acd6-6a96a7a42651)

4. ให้นักศึกษาเพิ่มเมธอดสำหรับค้นหาข้อมูลแบบช่วง (range search)
   
   ```python
   class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []      # เก็บรหัสนักศึกษา (Key)
        self.data = []      # เก็บชื่อนักศึกษา (Value)
        self.children = []  # เก็บโหนดลูก (ถ้ามี)

   class BTree:
    def __init__(self, order):
        self.root = None
        self.order = order
        self.max_keys = order - 1
        self.min_keys = (order // 2) - 1 if order % 2 == 0 else order // 2

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
        mid = self.order // 2

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

    def display(self, node=None, level=0):
        """ แสดงโครงสร้างของ B-Tree แบบเป็นลำดับชั้น """
        if node is None:
            node = self.root
        print('Level', level, 'Keys:', node.keys, 'Data:', node.data)
        for child in node.children:
            self.display(child, level + 1)

    def display_all_data(self, node=None):
        """ แสดงข้อมูลนักศึกษาทั้งหมดใน B-Tree """
        if node is None:
            node = self.root
        if node.leaf:
            for i in range(len(node.keys)):
                print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
        else:
            for i in range(len(node.keys)):
                self.display_all_data(node.children[i])
                print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
            self.display_all_data(node.children[-1])

    def range_search(self, start, end, node=None):
        """ ค้นหานักศึกษาที่มีรหัสอยู่ในช่วง [start, end] """
        if node is None:
            node = self.root
        if node.leaf:
            for i in range(len(node.keys)):
                if start <= node.keys[i] <= end:
                    print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
        else:
            for i in range(len(node.keys)):
                if node.keys[i] >= start:
                    self.range_search(start, end, node.children[i])
                if start <= node.keys[i] <= end:
                    print(f"รหัส: {node.keys[i]}, ชื่อ: {node.data[i]}")
            self.range_search(start, end, node.children[-1])
      
      # ===========================
      # 🔹 เริ่มต้นใช้งาน B-Tree
      # ===========================
      
      # สร้าง B-Tree ที่มี order = 3
      btree = BTree(order=3)
      
      # กำหนดข้อมูลนักศึกษาในโค้ด
      students = [
          (12345, "สมชาย"), 
          (23456, "สมหญิง"), 
          (34567, "อรพิน"), 
          (45678, "จิราภา"),
          (56789, "พิมพ์ประภา")
      ]
      
      # เพิ่มข้อมูลนักศึกษาเข้าไปใน B-Tree
      for sid, name in students:
          btree.insert(sid, name)
      
      # แสดงโครงสร้างของ B-Tree
      print("\n🔹 โครงสร้างของ B-Tree:")
      btree.display()
      
      # แสดงข้อมูลนักศึกษาทั้งหมด
      print("\n🔹 รายชื่อนักศึกษาที่ถูกเก็บใน B-Tree:")
      btree.display_all_data()
      
      # ทดสอบค้นหาข้อมูลนักศึกษาในช่วงรหัสที่กำหนด
      start_id = 23456
      end_id = 45678
      print(f"\n📌 รายชื่อนักศึกษาในช่วงรหัส {start_id} ถึง {end_id}:")
      btree.range_search(start_id, end_id)
      
   ```

   ![image](https://github.com/user-attachments/assets/9d05975d-558e-4890-bc5d-b404a6a2b260)




