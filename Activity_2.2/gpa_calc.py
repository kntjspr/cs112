def GPACalculator(grades):
    numeral_rating = grades['NR']
    academic_units = grades['AU']
    sums_prod = 0
    sums_au = 0
    for nr, au in zip(numeral_rating, academic_units):
        sums_prod = sums_prod + (nr * au)
        sums_au = sums_au + au
    gpa = sums_prod / sums_au
    return gpa
       
if __name__ == "__main__":
    grades = {'NR':[3.0, 2.5, 2.5, 3.0, 3.0], 'AU':[3.0, 3.0, 3.0, 3.0, 3.0]}
    print(f"GPA: {GPACalculator(grades)}")
