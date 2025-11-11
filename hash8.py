SIZE = 10
MAX = 10

# Create hash table and count array
hash_table = []
count = []
for i in range(SIZE):
    hash_table += [[0]*MAX]
    count += [0]

def hash_function(key):
    return key % SIZE

def insert(key):
    i = hash_function(key)
    if count[i] < MAX:
        hash_table[i][count[i]] = key
        count[i] += 1
        print("Inserted", key)
    else:
        print("Chain full!")

def search(key):
    i = hash_function(key)
    for j in range(count[i]):
        if hash_table[i][j] == key:
            print("Found", key, "at index", i)
            return
    print("Not found!")

def delete(key):
    i = hash_function(key)
    for j in range(count[i]):
        if hash_table[i][j] == key:
            for k in range(j, count[i]-1):
                hash_table[i][k] = hash_table[i][k+1]
            count[i] -= 1
            print("Deleted", key)
            return
    print("Not found!")

def display():
    for i in range(SIZE):
        print(i, ":", end=" ")
        for j in range(count[i]):
            print(hash_table[i][j], "->", end=" ")
        print("None")
 
# -------- Menu --------
while True:
    print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
    c = int(input("Choice: "))
    if c == 5:
        break
    if c in [1, 2, 3]:
        key = int(input("Enter key: "))
    if c == 1:
        insert(key)
    elif c == 2:
        search(key)
    elif c == 3:
        delete(key)
    elif c == 4:
        display()
    else:
        print("Invalid choice!")