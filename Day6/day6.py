# s = "#"
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     print(s * i)

# print(s * 1)
# print(s * 2)
# print(s * 3)
# print(s * 4)
# print(s * 5)
# print(s * 6)

# if '56' <= '9':
#     print("hello")
# text = input("Enter text: ")

# if text.isdigit() == True:
#     print("Digit")
# else:
#     print("Not Digit")

# n = 123
# getLenN = len(str(n))

# # print(n % 10)
# # print(n // 10)

# sum = 0
# for i in range(0, getLenN):
#     print("hello")
#     if (n > 0):
#         sum = sum + n % 10
#         n = n // 10

# print(sum)

# while True:
# sum = 0
# t = 0
# n = 12345
# while n > 0:
#     sum = sum + n % 10
#     n = n // 10

# print(sum)

# username_input = input("Enter username: ")
# password_input = input("Enter password: ")

# username = "phuong"
# password = "123"

# while True:
#     if username == username_input:
#         if password == password_input:
#             print("Success login")
#             break
#         else: 
#             password_input = input("You are wrong password, please enter password again: ")
#     else: 
#         username_input = input("You are wrong username, please enter username again: ")

# n = int(input("Enter n: "))

# my_list = []
# index = 0
# while index < n:
#     my_number = int(input(f"Nhập giá trị tại vị trí {index}: "))
#     my_list.append(my_number)
#     index = index + 1
# print(my_list)

my_list_food = ["Banh mi", "Lau Rieu", "Bun Cha", "Banh Da", "Kem", "Thit xien"]
# my_list_food.insert()
# 1. Banh mi
# 2. Lau Rieu

# n = input("Nhập 1 số để chọn chức năng: ")
while True:
    print("""
        [1]: Hiện ra toàn bộ đồ ăn đang có
        [2]: Thêm món ăn vào trong list_food  
        [3]: Xoá các món ăn ở cuối
        [4]: Chèn 1 phần tử bất kỳ vào mảng
        [0]: Thoát
        """)
    n = input("Để tiếp tục chương trình hay nhập các số từ (0-3): ")
    print("")
    if n == "1":
        for i in range(0, len(my_list_food)):
            print(f"{i + 1}. {my_list_food[i]}")
    
    elif n == "2":
        new_food = input("Thêm món ăn mới: ")
        # my_list_food.append(new_food)

        # cach 1
        # if new_food != "":
        #     my_list_food.append(new_food)

        # cach 2
        if new_food == "":
            while True:
                new_food = input("Mời bạn nhập lại món ăn, ko được để giá trị rỗng: ")
                if new_food != "":
                    my_list_food.append(new_food)
                    break
        else:
            my_list_food.append(new_food)

    elif n == "3":
        amount = input("Nhập số lượng phần tử muốn xoá từ cuối lên đầu: ")
        if amount == "" or int(amount) > len(my_list_food):
            while True:
                amount = input("Bạn nhập thiếu nội hoặc sai số lượng, vui lòng nhập lại amount: ")
                if amount != "" and int(amount) <= len(my_list_food):
                    for i in range(0, int(amount)):
                        my_list_food.pop()
                    break
        else:
            for i in range(0, int(amount)):
                my_list_food.pop()
    
    elif n == "4":
        vi_tri = input("Nhập vị trí muốn chèn: ")
        value = input("Nhập giá trị mới: ")

        left_side = my_list_food[ : int(vi_tri)]
        right_side = my_list_food[int(vi_tri) : ]

        newArray = []
        for element in left_side:
            newArray.append(element)
        
        newArray.append(value)

        for element in right_side:
            newArray.append(element)

        my_list_food = newArray
    
    elif n == "0":
        print("Thoát chương trình thành công !!")
        break
    else: 
        print("Bạn đang nhập sai ký tự, vui lòng nhập lại")

# [1, 2, 3]
# print(my_list_food[0: 2])
# print(my_list_food[2: ])

# new_Value = "phuong"

# my_list_food[1] = new_Value
# print(my_list_food)
# hello 
# phuong

# vi tri chen = 1
# gia tri muon chen

# [1, "hello", 2, 3]