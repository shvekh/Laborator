s=str(input("Введите строку: "))
s1=' '.join(s)
sNew=''
s2=s1.split(' ')
for i in range(len(s2)):
    Flag=s2[i].isalpha()
    if Flag==True:
        sNew+=s2[i]
print('Новая строка: ',sNew)

