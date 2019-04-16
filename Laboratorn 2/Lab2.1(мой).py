my_number=int(input("Задаем число = "))
user_number=int(input('Введите число: '))
while user_number!=my_number:
    print("Не совпадает")
    user_number=int(input('Введите число повторно: '))
print('Совпадает')
