# N = int(input("Enter number: "))

# print((N-1)/2)
# start = int((N - 1)/2)

# count = 0
# for i in range(start, N):
#     count = count + 1

# print(count)

# import math

# print(math.sqrt(100))

# import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# p = (a + b + c)/2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print("S")


# for i in range (start, end, don_vi)
# start: số bắt đầu
# end: kết thức
# đơn vị: sự thay đổi của i sau mỗi lần lặp
# start <= i < end

# In ra từng chữ cái theo chiều từ cuối lên đầu
text = "hello cac ban"
# for i in range(0, len(text)):
#     print(text[i])

# for i in range(len(text) - 1, -1, -1):
#     if text[i] != " ":
#         print(text[i])

# Đếm xem có baonh chữ a và l trong text
# count_text = 0
# for i in range(0, len(text)):
#     if text[i] == "a" or text[i] == "l":
#         count_text = count_text + 1

# print(count_text)

n = int(input("Enter n: "))
t = ""

for i in range(0, n):
    t = t + "*"

for i in range(n, 0, -1):
    print(t[0: i])

# output = "******"
# print(output[0:6])
# print(output[0:5])
# print(output[0:4])
# print(output[0:3])
# print(output[0:2])
# print(output[0:1])


