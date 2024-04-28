import operator


marks = {'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
         'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
         'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}}
print(f"marks obtained by amol is {marks['Amol']['Eng']}")
marks['Raka']['Maths'] = 77
print(marks)
# sorted returns list thats why conv to dict
marks = dict(sorted(marks.items()))
print(marks)
