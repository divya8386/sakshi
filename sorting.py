# Function for Selection Sort
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        # swap
        temp = salaries[i]
        salaries[i] = salaries[min_index]
        salaries[min_index] = temp


# Function for Bubble Sort
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                # swap
                temp = salaries[j]
                salaries[j] = salaries[j + 1]
                salaries[j + 1] = temp


# Main program
n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    sal = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

# Copy list for both sorts
salaries_selection = salaries[:]
salaries_bubble = salaries[:]

# Apply Selection Sort
selection_sort(salaries_selection)
print("\nSalaries after Selection Sort (ascending):")
print(salaries_selection)

# Apply Bubble Sort
bubble_sort(salaries_bubble)
print("\nSalaries after Bubble Sort (ascending):")
print(salaries_bubble)

# Display Top 5 Highest Salaries
print("\nTop 5 Highest Salaries:")
count = 0
i = len(salaries_bubble) - 1
while i >= 0 and count < 5:
    print(salaries_bubble[i])
    i -= 1
    count += 1
