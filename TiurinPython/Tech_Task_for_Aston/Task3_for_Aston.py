print("Введите любое множество чисел(используя пробел): " , end="")
New_list = [int(i) for i in input().split()]
print("Числа кратные 3: ", end="")
count = 0
for i in New_list:
    if i % 3 == 0:
        print(i, end =" ")
        count += 1
if count == 0:
    print("В этом списке нет чисел кратных 3")