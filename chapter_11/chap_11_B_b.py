import operator

student = {"adil": {"maths": 70, "sst": 89, "phys": 90},
           "riz": {"maths": 90, "sst": 79, "phys": 100},
           "dil": {"maths": 60, "sst": 69, "phys": 80}}

for name, subjects in student.items():
    total = 0
    for subject, marks in subjects.items():
        total = total + marks
    avg = int(total/3)
    student[name] = {"total": total, "avg": avg}

    topper_name = ''
    topper_markss = 0
    if avg > topper_markss:
        topper_name = name
        topper_markss = avg

print(student)
print(topper_name)
print(topper_markss)
