SIZE = 10
table = [None] * SIZE   # Initialize hash table with None

# Hash function
def hash_function(key):
    return key % SIZE

# Insert function (Linear Probing)
def insert(key):
    i = hash_function(key)
    start = i
    while table[i] is not None:       # If slot is occupied
        i = (i + 1) % SIZE           # Linear probing
        if i == start:               # If table is full
            print("Hash table is full!")
            return
    table[i] = key

# Search function
def search(key):
    i = hash_function(key)
    start = i
    for key  in range(SIZE):
        if table[i] == key:
            return True
        i = (i + 1) % SIZE
        if i == start:
            break
    return False

# Delete function
def delete(key):
    i = hash_function(key)
    start = i
    for key in range(SIZE):
        if table[i] == key:
            table[i] = None
            print(f"{key} deleted.")
            return
        i = (i + 1) % SIZE
        if i == start:
            break
    print(f"{key} not found.")

# Display function
def display():
    print("Hash Table:", table)


# --------------------------
# Test the hash table
# --------------------------
insert(15)
insert(25)
insert(31)
display()

print("Search 25:", search(25))
delete(25)
print("Search 25 after delete:", search(25))
display()
