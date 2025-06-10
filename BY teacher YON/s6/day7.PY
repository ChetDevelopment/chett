# students = [
# student=[
# {
#         "name": "Alice",
#         "age": 17,
#         "gender": "Female",
#         "address": {
#             "city": "Phnom Penh",
#             "district": "Chamkarmon"
#         },
#         "subjects": [
#             {"name": "Math", "score": 85},
#             {"name": "Physics", "score": 78},
#             {"name": "Biology", "score": 90}
#         ]
#     },
#     {
#         "name": "Sokha",
#         "age": 16,
#         "gender": "Male",
#         "address": {
#             "city": "Siem Reap",
#             "district": "Svay Dangkum"
#         },
#         "subjects": [
#             {"name": "English", "score": 75},
#             {"name": "Computer", "score": 88},
#             {"name": "Art", "score": 92}
#         ]
#     },
#     {
#         "name": "Dara",
#         "age": 18,
#         "gender": "Male",
#         "address": {
#             "city": "Battambang",
#             "district": "Battambang"
#         },
#         "subjects": [
#             {"name": "History", "score": 60},
#             {"name": "Geography", "score": 70},
#             {"name": "Math", "score": 80}
#         ]
#     }
# ]
# countA = 0
# for i in range(len(student)):
#     if student[i] == "Male":
#         countA += 1
# print(countA)

# students=[
# {
#         "name": "Alice",
#         "age": 17,
#         "gender": "Female",
#         "address": {
#             "city": "Phnom Penh",
#             "district": "Chamkarmon"
#         },
#         "subjects": [
#             {"name": "Math", "score": 85},
#             {"name": "Physics", "score": 78},
#             {"name": "Biology", "score": 90}
#         ]
#     },
#     {
#         "name": "Sokha",
#         "age": 16,
#         "gender": "Male",
#         "address": {
#             "city": "Siem Reap",
#             "district": "Svay Dangkum"
#         },
#         "subjects": [
#             {"name": "English", "score": 75},
#             {"name": "Computer", "score": 88},
#             {"name": "Art", "score": 92}
#         ]
#     },
#     {
#         "name": "Dara",
#         "age": 18,
#         "gender": "Male",
#         "address": {
#             "city": "Battambang",
#             "district": "Battambang"
#         },
#         "subjects": [
#             {"name": "History", "score": 60},
#             {"name": "Geography", "score": 70},
#             {"name": "Math", "score": 80}
#         ]
#     }
# ]
# math_students = 0

# for student in students:
#     for subject in student["subjects"]:
#         if subject["name"] == "Math":
#             math_students += 1
# print( math_students)
# students=[
# {
#         "name": "Alice",
#         "age": 17,
#         "gender": "Female",
#         "address": {
#             "city": "Phnom Penh",
#             "district": "Chamkarmon"
#         },
#         "subjects": [
#             {"name": "Math", "score": 85},
#             {"name": "Physics", "score": 78},
#             {"name": "Biology", "score": 90}
#         ]
#     },
#     {
#         "name": "Sokha",
#         "age": 16,
#         "gender": "Male",
#         "address": {
#             "city": "Siem Reap",
#             "district": "Svay Dangkum"
#         },
#         "subjects": [
#             {"name": "English", "score": 75},
#             {"name": "Computer", "score": 88},
#             {"name": "Art", "score": 92}
#         ]
#     },
#     {
#         "name": "Dara",
#         "age": 18,
#         "gender": "Male",
#         "address": {
#             "city": "Battambang",
#             "district": "Battambang"
#         },
#         "subjects": [
#             {"name": "History", "score": 60},
#             {"name": "Geography", "score": 70},
#             {"name": "Math", "score": 80}
#         ]
#     }
# ]
# for student in students:
#     if student["name"] == "Sokha":
#         scores = [subject["score"] for subject in student["subjects"]]
#         average = sum(scores) / len(scores)
#         print( average)
# students=[
# {
#         "name": "Alice",
#         "age": 17,
#         "gender": "Female",
#         "address": {
#             "city": "Phnom Penh",
#             "district": "Chamkarmon"
#         },
#         "subjects": [
#             {"name": "Math", "score": 85},
#             {"name": "Physics", "score": 78},
#             {"name": "Biology", "score": 90}
#         ]
#     },
#     {
#         "name": "Sokha",
#         "age": 16,
#         "gender": "Male",
#         "address": {
#             "city": "Siem Reap",
#             "district": "Svay Dangkum"
#         },
#         "subjects": [
#             {"name": "English", "score": 75},
#             {"name": "Computer", "score": 88},
#             {"name": "Art", "score": 92}
#         ]
#     },
#     {
#         "name": "Dara",
#         "age": 18,
#         "gender": "Male",
#         "address": {
#             "city": "Battambang",
#             "district": "Battambang"
#         },
#         "subjects": [
#             {"name": "History", "score": 60},
#             {"name": "Geography", "score": 70},
#             {"name": "Math", "score": 80}
#         ]
#     }
# ]
# for student in students:
#     if student["name"] == "Dara":
#         total = sum(subject["score"] for subject in student["subjects"])
#         print(total)
students=[
{
        "name": "Alice",
        "age": 17,
        "gender": "Female",
        "address": {
            "city": "Phnom Penh",
            "district": "Chamkarmon"
        },
        "subjects": [
            {"name": "Math", "score": 85},
            {"name": "Physics", "score": 78},
            {"name": "Biology", "score": 90}
        ]
    },
    {
        "name": "Sokha",
        "age": 16,
        "gender": "Male",
        "address": {
            "city": "Siem Reap",
            "district": "Svay Dangkum"
        },
        "subjects": [
            {"name": "English", "score": 75},
            {"name": "Computer", "score": 88},
            {"name": "Art", "score": 92}
        ]
    },
    {
        "name": "Dara",
        "age": 18,
        "gender": "Male",
        "address": {
            "city": "Battambang",
            "district": "Battambang"
        },
        "subjects": [
            {"name": "History", "score": 60},
            {"name": "Geography", "score": 70},
            {"name": "Math", "score": 80}
        ]
    }
]
  



