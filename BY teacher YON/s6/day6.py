# student=[
#     {"name":"chet","class":"B","id":53},
#     {"name":"ya","class":"C","id":39},
#     {"name":"smey","class":"A","id":48}
# ]
# print(student[0]["name"])
# student=[
#     {"name":"chet","class":"B","id":53},
#     {"name":"ya","class":"C","id":39},
#     {"name":"smey","class":"A","id":48}
# ]
# print(student[2]["id"])
# student=[
#     {"name":"chet","class":"B","id":53},
#     {"name":"ya","class":"C","id":39},
#     {"name":"smey","class":"A","id":48}
# ]
# print(student[2]["class"])
# student=[
#     {"name":"SreyDoeurn","class":"2026B"},
#     {"name":"Sokkeang","class":"2026B"},
#     {"name":"Darika","class":"2026C"},
#     {"name":"King","class":"2026C"},
#     {"name":"Viza","class":"2026A"},
#     {"name":"Seavmey","class":"2026A"}
# ]
# print(student[5])
# student=[
#     {"name":"SreyDoeurn","class":"2026B"},
#     {"name":"Sokkeang","class":"2026B"},
#     {"name":"Darika","class":"2026C"},
#     {"name":"King","class":"2026C"},
#     {"name":"Viza","class":"2026A"},
#     {"name":"Seavmey","class":"2026A"}
# ]
# print(student[2]["name"])
# student=[
#     {"name":"SreyDoeurn","class":"2026B"},
#     {"name":"Sokkeang","class":"2026B"},
#     {"name":"Darika","class":"2026C"},
#     {"name":"King","class":"2026C"},
#     {"name":"Viza","class":"2026A"},
#     {"name":"Seavmey","class":"2026A"}
# ]
# print(student[0]["name"])
# student=[
#     {"name":"SreyDoeurn","class":"2026B"},
#     {"name":"Sokkeang","class":"2026B"},
#     {"name":"Darika","class":"2026C"},
#     {"name":"King","class":"2026C"},
#     {"name":"Viza","class":"2026A"},
#     {"name":"Seavmey","class":"2026A"}
# ]
# for i in range(len(student)):
#     print(student[i]["name"])
# student=[
#     {"name":"SreyDoeurn","class":"2026B"},
#     {"name":"Sokkeang","class":"2026B"},
#     {"name":"Darika","class":"2026C"},
#     {"name":"King","class":"2026C"},
#     {"name":"Viza","class":"2026A"},
#     {"name":"Seavmey","class":"2026A"}
# ]
# for i in range(len(student)):
#     print(student[i]["class"],student[i]["name"])
# fruits=[
#     {"name":"banana","quality":40,"price":12,"in_stock":"True"},
#     {"name":"apple","quality":41,"price":10,"in_stock":"True"},
#     {"name":"Kiwi","quality":40,"price":4,"in_stock":"True"},
#     {"name":"jack fruit","quality":1,"price":47,"in_stock":"True"},
#     {"name":"Turen","quality":0,"price":100,"in_stock":"False"}
# ]
# for i in range(len(fruits)):
#     print(fruits[i]["name"])
# fruits=[
#     {"name":"banana","quality":40,"price":12,"in_stock":True},
#     {"name":"apple","quality":41,"price":10,"in_stock":True},
#     {"name":"Kiwi","quality":40,"price":4,"in_stock":True},
#     {"name":"jack fruit","quality":1,"price":47,"in_stock":True},
#     {"name":"Turen","quality":0,"price":100,"in_stock":True}
# ]
# sum = 0
# for fruit in fruits:
#     sum += fruit["price"]
# print(sum)
# fruits=[
#     {"name":"banana","quality":40,"price":12,"in_stock":True},
#     {"name":"apple","quality":41,"price":10,"in_stock":True},
#     {"name":"Kiwi","quality":40,"price":4,"in_stock":True},
#     {"name":"jack fruit","quality":1,"price":47,"in_stock":True},
#     {"name":"Turen","quality":0,"price":100,"in_stock":True}
# ]
# sum = 0
# for fruit in fruits:
#     sum += fruit["quality"]
# print(sum)
# fruits=[
#     {"name":"banana","qty":40,"price":12,"in_stock":True},
#     {"name":"apple","qty":41,"price":10,"in_stock":True},
#     {"name":"Kiwi","qty":40,"price":4,"in_stock":True},
#     {"name":"jack fruit","qty":1,"price":47,"in_stock":True},
#     {"name":"Turen","qty":0,"price":100,"in_stock":False}
# ]
# countA = 0
# for fruit in fruits:
#     if fruit["in_stock"] == False:

#         countA += 1
# print(countA)
# fruits=[
#     {"name":"banana","qty":40,"price":12,"in_stock":True},
#     {"name":"apple","qty":41,"price":10,"in_stock":True},
#     {"name":"Kiwi","qty":40,"price":4,"in_stock":True},
#     {"name":"jack fruit","qty":1,"price":47,"in_stock":True},
#     {"name":"Turen","qty":0,"price":100,"in_stock":False}
# ]

# for fruit in fruits:
#     if fruit["in_stock"] == False:
#         print(fruit["name"])
# fruits=[
#     {"name":"banana","qty":40,"price":12,"in_stock":True},
#     {"name":"apple","qty":41,"price":10,"in_stock":True},
#     {"name":"Kiwi","qty":40,"price":4,"in_stock":True},
#     {"name":"jack fruit","qty":1,"price":47,"in_stock":True},
#     {"name":"Turen","qty":0,"price":100,"in_stock":False}
# ]
# countA = 0
# for fruit in fruits:
#     if fruit["in_stock"] == False:
#         print(fruit["name"])
#         countA += 1
# print(countA)
