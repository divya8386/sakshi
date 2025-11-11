
thisdict = {
    "student1": ["DE", "DSA", "DELD"],
    "Student2": ["Maths", "DSA"],
    "Student3": [],
    "student4": ["Maths"]
}


print(thisdict)


def find_length(lst):
    count = 0
    for x in lst:
        count += 1
    return count


for x in thisdict:
    print(x, ":", find_length(thisdict[x]))


def average_books(thisdict):
    total_books = 0
    total_students = 0
    for student in thisdict:
        total_students += 1
        total_books += find_length(thisdict[student])
    avg = total_books / total_students
    print("Average books borrowed:", avg)

average_books(thisdict)
   

def no_books(thisdict):
    for student in thisdict:
        if find_length(thisdict[student]) == 0:
            print(student, "did not borrow any book")

no_books(thisdict)


book_num = {}

for list in thisdict.values():
    for book in list:
        if book in book_num:
            book_num[book] += 1
        else:
            book_num[book] = 1


max_count = 0
min_count = None
max_book = ""
min_book = ""

for book in book_num: 
    count = book_num[book]

    # for max
    if count > max_count:
        max_count = count
        max_book = book

    # for min
    if min_count is None or count < min_count:
        min_count = count
        min_book = book

print("Most borrowed book:", max_book)
print("Least borrowed book:", min_book)
