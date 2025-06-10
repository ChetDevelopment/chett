# 9. Remove students who scored below 40 and show the remaining list
students = [
    {"name": "Sok", "score": 85},
    {"name": "Dara", "score": 42},
    {"name": "Rith", "score": 73},
    {"name": "Sophy", "score": 35},
    {"name": "Mony", "score": 90}
]
Low_score = []
for student in students:
    if student['score'] >= 40:
        Low_score.append(student)
for i in Low_score:
    print(f"{i['name']}, ", end='')