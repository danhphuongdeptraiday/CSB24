my_list = ["123", "phuong", "Bun char", True, 9090]

# Để truy cập vào các phần tử trong list ta dùng: tên_list[index]
# 0 <= index <= len(ten_list) - 1
# Công thức để lấy ra phần tử ở cuối list: tên_list[len(tên_list) - 1]
# for i in range(len(my_list)):
#     print(my_list[i])
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i])

list_text = ["Lâm", "Minh1", "Minh2", "Huy", "Phúc"]
# dau = [""]

t = ""
# t = t + "Lâm" + "-" # "Lâm-"
# t = t + "Minh1" + "-" # "Lâm-Minh1-"

# output: "Lâm - Minh1 - Minh2 - Huy - Phúc"

for i in range (0, len(list_text)):
    if(i < len(list_text) - 1):
        if i % 2 != 0:
            t = t + list_text[i] + " + "
        else:
            t = t + list_text[i] + " - "
    else:
        t = t + list_text[i]

# print(t)

print(f"[{t}]")

# numbers = [42, 17, 89, 3, 56, 78, 24, 66, 10, 35]
# tong = 0
# tong = tong + numbers[0]
# tong = tong + numbers[1]
# tong = tong + numbers[2]

# phepTinhTong = ""

# for i in range(0, len(numbers)):
#     tong = tong + numbers[i]
#     if (i < len(numbers) - 1):

#         phepTinhTong = phepTinhTong + str(numbers[i]) + " + "
#     else:
#         phepTinhTong = phepTinhTong + str(numbers[i]) + " = "

# print(phepTinhTong + str(tong))


