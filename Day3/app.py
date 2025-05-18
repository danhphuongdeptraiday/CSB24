str = "Hello World"
print(str[::-1])
# print(len(str))
# ten_string[index]
# index >= 0 va index < len(str) - 1
# print(str[len(str) - 1]: truy cap vao phan tu cuoi cua 1 chuoi

# cắt 1 chuỗi trong khoảng từ a đến b: lon hon = a va nho hon b
# str[a: b]
# print(str[2: 7])
# print(str[2: len(str)])
# print(str[2:])
# print(str[2 : -1])

# t = str.replace("o", "t") # => tra ve gia tri moi
# print(t)
# print(str)
# print("I am Learning
# Python String on GeeksforGeeks")

# a = "10"
# # print("Number: "+ str(a))
# print(f"Number: {a}")
# print(word.index(""))
# print(word[:20])
# word = "Python's Software"
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print(word[a:b])


# word = "abcdefghijklmnopqrstuvwxyz"
# char = input("Enter character: ")
# step = int(input("Enter step: "))

# for i in range(3, 0, -1):
#     print(i)

# print(s + s[::-1])

# "abc"
#  012

s = input("Enter string: ")
reverseString = ""
# reverseString = "" + "c"
# reverseString = "c" + "b"
# reverseString = "cb" + "a"
for i in range(len(s) - 1, -1, -1):
    print(reverseString)
    reverseString = reverseString + s[i]
print(s + reverseString)
# final_index = word.index(char) + step
# print(word[final_index])