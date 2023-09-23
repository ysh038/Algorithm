total_credit = 0.0
total_grade = 0.0

for i in range(20):
    name, credit, grade = map(str, input().split())
    
    if(grade == "A+"):
        total_grade += 4.5 * float(credit)
    elif(grade == "A0"):
        total_grade += 4.0 * float(credit)
    elif(grade == "B+"):
        total_grade += 3.5 * float(credit)
    elif(grade == "B0"):
        total_grade += 3.0 * float(credit)
    elif(grade == "C+"):
        total_grade += 2.5 * float(credit)
    elif(grade == "C0"):
        total_grade += 2.0 * float(credit)
    elif(grade == "D+"):
        total_grade += 1.5 * float(credit)
    elif(grade == "D0"):
        total_grade += 1.0 * float(credit)
    elif(grade == "F"):
        total_grade += 0.0 * float(credit)
    elif(grade == "P"):
        continue

    total_credit += float(credit)


print(total_grade/total_credit)