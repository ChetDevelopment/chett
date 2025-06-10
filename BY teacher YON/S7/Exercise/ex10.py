# 10. Check if any students have the same score.
students = [
    {"name": "Sok", "score": 85},
    {"name": "Dara", "score": 42},
    {"name": "Rith", "score": 73},
    {"name": "Sophy", "score": 35},
    {"name": "Mony", "score": 90}
]

scores_seen = []
has_duplicates = False

for student in students:
    if student["score"] in scores_seen:
        has_duplicates = True
        break
    scores_seen.append(student["score"])

if has_duplicates:
    print("There are duplicate scores.")
else:
    print("No duplicates.")
