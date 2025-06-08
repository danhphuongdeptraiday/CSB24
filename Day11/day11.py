# Kiểu dữ liệu và dictionary
# Được lưu dưới dạng là key: value



my_dictionary = {
    "information": "thông tin",
    "question": "câu hỏi",
    "numbers": [1, 2, 3], # => Kiểu dữ liệu list
    "isActive": True # => Kiểu dữ liệu boolean
}

# Truy cập và các value trong dictionary: tên_dict.values()
# print(my_dictionary.values())
# for value in my_dictionary.values():
#     print(value)

# list = ["123", "phuong", "Bun char", True, 9090]
# for i in list:
#     print(i)

# for i in range(0, len(list)):
#     print(list[i])

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])

#  Truy cập vào các gía trị trong dictionary: tên_dict["key"]
# print(my_dictionary["information"])
# print(my_dictionary["numbers"][0])
# print(my_dictionary["numbers"][1])
# print(my_dictionary["numbers"][2])

# print(my_dictionary)

# Thêm 1 cặp giá trị mới vào trong dictionary: tên_dict["key mới"] = giá trị mới

my_dictionary["name"] = "Phuong"

# key = input("Enter key: ")
# value = input("Enter value: ")
# my_dictionary[key] = value

# Dùng vòng for để khai báo 5 cặp key và value bất kỳ cho 1 dictionary
# Key value phải được nhập từ input
# Ban đầu dictionary phải rỗng
# result = {}

# for i in range (5):
#     key = input(f"Enter key cho cặp {i + 1}: ")
#     value = input(f"Enter value cho cặp {i + 1}: ")
#     result[key] = value

# print(result)

# person1 = {
#     "name" : "Nhậtật Minh" ,
#     "age" : 17  , 
#     "favourite" : "Đi ngủ",
#     "address" : "Nam Định"
# }
# person2 = {
#     "name" : "Tuấn Minh" ,
#     "age" : 13  , 
#     "favourite" : "chơi game",
#     "address" : "Thái Bình"
# }
# person3 = {
#     "name" : "Huy" ,
#     "age" : 16  , 
#     "favourite" : "chơi game",
#     "address" : "Hà Nội"
# }

# list_person = [person1, person2, person3]
list_person = [
    {
        "name" : "Nhậtật Minh" ,
        "age" : 17  , 
        "favourite" : "Đi ngủ",
        "address" : "Nam Định"
    },
    {
        "name" : "Tuấn Minh" ,
        "age" : 13  , 
        "favourite" : "chơi game",
        "address" : "Thái Bình"
    },
    {
        "name" : "Huy" ,
        "age" : 16  , 
        "favourite" : "chơi game",
        "address" : "Hà Nội"
    }
]

# print(list_person[0]["name"])
# print(list_person[1]["name"])
# print(list_person[2]["name"])

for i in range(0, len(list_person)):
    print(list_person[i]["name"])

totalAge = 0
for i in range(0, len(list_person)):
    totalAge = totalAge + list_person[i]["age"]

print(totalAge)

# if person1["age"] > person2["age"] and person1["age"] > person3["age"]:
#     print(person1["name"])
# elif person2["age"] > person1["age"] and person2["age"] > person3["age"]:
#     print(person2["name"])
# elif person3["age"] > person2["age"] and person3["age"] > person1["age"]:
#     print(person3["name"])