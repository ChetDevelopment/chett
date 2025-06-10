# 5. Calculate the average score of all students
students = [
 {"name": "Sok", "score": 85},
 {"name": "Dara", "score": 42},
 {"name": "Rith", "score": 73},
 {"name": "Sophy", "score": 35},
 {"name": "Mony", "score": 90}
]
total_score =0
for student in students:
    total_score += student["score"]
average = total_score/len(students)
print(average)