def retGrade(m):
    if m > 100 or m < 0:
        return 'Invalid Range'
    if m >= 85:
        return 'A'
    if m >= 70:
        return 'B'
    if m >= 50:
        return 'C'
    else:
        return 'Fail'

input_marks = int(input("Marks: "))
print(retGrade(input_marks))

