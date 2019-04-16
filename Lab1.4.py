import random
n=int(input("\nВведите кол-во эл-ов списка "))
k=int(input("\nВведите диапазон эл-ов списка "))
m=random.sample(range(k),n)
mi=k+1
for i in range(n):
    if m[i]<mi:
        mi=m[i]
print(m)
print('Минимальное число массива',mi)
