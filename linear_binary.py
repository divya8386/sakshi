# =====================================================
# E-COMMERCE CUSTOMER ACCOUNT SEARCH PROGRAM
# (Linear Search + Binary Search WITHOUT INBUILT FUNCTIONS)
# =====================================================

# -----------------------------
# Linear Search Function
# -----------------------------
def linearSearch(lst, key, size):
    i = 0
    while i < size:
        if lst[i] == key:
            return i
        i += 1
    return -1


# -----------------------------
# Binary Search Function
# -----------------------------
def binarySearch(lst, key, size):
    first = 0
    last = size - 1

    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1


# =====================================================
# MAIN PROGRAM
# =====================================================

print("=== E-COMMERCE CUSTOMER ACCOUNT SEARCH SYSTEM ===")

# ---- LINEAR SEARCH ----
print("\n=== LINEAR SEARCH ===")
size = int(input("Enter number of customer account IDs: "))

customer_list = [0] * size  # Fixed-size list

print("Enter customer account IDs:")
i = 0
while i < size:
    cid = int(input())
    customer_list[i] = cid
    i += 1

key = int(input("Enter account ID to search (Linear Search): "))

pos = linearSearch(customer_list, key, size)

if pos == -1:
    print("Account ID", key, "is NOT found in the list.")
else:
    print("Account ID", key, "found at position", pos + 1, "using Linear Search.")


# ---- BINARY SEARCH ----
print("\n=== BINARY SEARCH ===")
print("Enter customer account IDs in ASCENDING ORDER (-999 to stop):")

max_size = 100
sorted_list = [0] * max_size
count = 0

while True:
    n = int(input())
    if n == -999:
        break
    sorted_list[count] = n
    count += 1

key2 = int(input("Enter account ID to search (Binary Search): "))

pos2 = binarySearch(sorted_list, key2, count)

if pos2 == -1:
    print("Account ID", key2, "is NOT found in the list.")
else:
    print("Account ID", key2, "found at position", pos2 + 1, "using Binary Search.")