numbers = [42, 17, 89, 3, 56, 78, 24, 66, 10, 35]
#min_number = numbers[0]
#for i in range(1, len(numbers)):
#    if numbers[i] < min_number:
#        min_number = numbers[i]

#print(min_number)




#max_number = numbers[0]
#for i in range(1, len(numbers)):
#    if numbers[i] > max_number:
#        max_number = numbers[i]

#print(max_number)

total = 0

for i in range(len(numbers)):
    if i % 2 == 0:  
        total += numbers[i]
    else:           
        total -= numbers[i]

print(total)