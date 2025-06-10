# 3. Count how many students failed (score < 50).
students = [
 {"name": "Sok", "score": 85},
 {"name": "Dara", "score": 42},
 {"name": "Rith", "score": 73},
 {"name": "Sophy", "score": 35},
 {"name": "Mony", "score": 90}
]
count = 0
for student in students:
    if student["score"] < 50:
        count += 1
print(count)