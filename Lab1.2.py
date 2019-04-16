strok=str(input("\nВведите строку "))
m=strok.split(' ')
st=''
for i in range(len(m)):
    if i%2!=0:
        st+=(m[i]+' ')
        
print(st)
