# Simple Node class 
class Student: 
    def __init__(self, roll, name, marks): 
        self.roll = roll 
        self.name = name 
        self.marks = marks 
        self.next = None 
 
 
# Simple Linked List class 
class StudentList: 
    def __init__(self): 
        self.head = None 
 
    def add(self, roll, name, marks): 
        new = Student(roll, name, marks) 
        if not self.head: 
            self.head = new 
        else: 
            temp = self.head 
            while temp.next: 
                temp = temp.next 
            temp.next = new 
        print("Added:", name) 
 
    def delete(self, roll): 
        cur = self.head 
        prev = None 
        while cur and cur.roll != roll: 
            prev = cur 
            cur = cur.next 
 
        if not cur: 
            print("Student not found.") 
            return 
 
        if not prev: 
            self.head = cur.next 
        else: 
            prev.next = cur.next 
        print("Deleted Roll No:", roll) 
 
    def update(self, roll, name=None, marks=None): 
        cur = self.head 
        while cur: 
            if cur.roll == roll: 
                if name: 
                    cur.name = name 
                if marks is not None: 
                    cur.marks = marks 
                print("Updated.") 
                return 
            cur = cur.next 
        print("Student not found.") 
 
    def search(self, roll): 
        cur = self.head 
        while cur: 
            if cur.roll == roll: 
                print(f"Found: Roll: {cur.roll}, Name: {cur.name}, Marks: {cur.marks}") 
                return 
            cur = cur.next 
        print("Student not found.") 
 
    def sort(self, key="roll", desc=False): 
        nodes = [] 
        cur = self.head 
        while cur: 
            nodes.append(cur) 
            cur = cur.next 
 
        nodes.sort(key=lambda x: getattr(x, key), reverse=desc) 
 
        for i in range(len(nodes) - 1): 
            nodes[i].next = nodes[i + 1] 
 
        if nodes: 
            nodes[-1].next = None 
            self.head = nodes[0] 
 
        print(f"Sorted by {key} ({'desc' if desc else 'asc'}).") 
 
    def show(self): 
        cur = self.head 
        if not cur: 
            print("No records.") 
            return 
 
        while cur: 
            print(f"Roll: {cur.roll}, Name: {cur.name}, Marks: {cur.marks}") 
            cur = cur.next 
 
 
# ======= Menu ======= 
if __name__ == "__main__": 
    s = StudentList() 
    s.add(1, "Aarav", 85) 
    s.add(2, "Priya", 92) 
    s.add(3, "Rahul", 78) 
 
    while True: 
        print("\n1. Add  2. Delete  3. Update  4. Search  5. Sort  6. Show  7. Exit") 
        ch = input("Choice: ") 
 
        if ch == '1': 
            r = int(input("Roll: ")) 
            n = input("Name: ") 
            m = float(input("Marks: ")) 
            s.add(r, n, m) 
 
        elif ch == '2': 
            r = int(input("Roll to delete: ")) 
            s.delete(r) 
 
        elif ch == '3': 
            r = int(input("Roll to update: ")) 
            n = input("New name (blank to skip): ") 
            m = input("New marks (blank to skip): ") 
            s.update(r, n if n else None, float(m) if m else None) 
 
        elif ch == '4': 
            r = int(input("Roll to search: ")) 
            s.search(r) 
 
        elif ch == '5': 
            k = input("Key (roll/marks): ") 
            o = input("Order (asc/desc): ") 
            s.sort(k, o == 'desc') 
 
        elif ch == '6': 
            s.show() 
 
        elif ch == '7': 
            print("Bye!") 
            break 
 
        else: 
            print("Invalid choice.") 