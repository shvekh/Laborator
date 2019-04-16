s=str(input("Введите строку: "))
m=s.split(' ')
for i in range(len(m)):
    if len(m[i])<10:
        print(m[i])
