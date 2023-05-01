def gradingStudents(grades):
    n = len(grades)
    for i in range (n):
        mod = grades[i]%5
        if mod >= 3 and grades[i] >=37:
            grades[i] += (5-mod)
    return grades
