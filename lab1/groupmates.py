#coding:utf-8
groupmates = [
    {
        "name": u"Саня",
        "group": "2280",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Игорь",
        "group": "2280",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Жека",
        "group": "2290",
        "age": 19,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print u"Имя Студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20)
    for student in students:
        print student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20)
    print "\n"

def filter_by_average(students, min_average):
    result = []
    for student in students:
        avg = sum(student["marks"]) / float(len(student["marks"]))
        if avg >= min_average:
            result.append(student)
    return result

print_students(groupmates)

filtered = filter_by_average(groupmates, 4.0)
print u"Студенты со средним баллом >= 4.0:"
print_students(filtered)
