
with open('Lista clasei 11D', 'r') as f:
    list1=f.readlines()

m=0
y=0
u=0
me1=0
me2=0
for i in list1:
    lista2=i.split()
    m+=int(lista2[2])
    if lista2[3]=='Eng1':
        me1+=int(lista2[2])
        y+=1
        with open('grupa1.txt','a') as f:
            x=lista2[0]+' '+lista2[1]+'\n'
            f.write(x)
    else:
        me2+=int(lista2[2])
        u+=1
        with open('grupa.txt','a') as f:
            x=lista2[0]+'  '+lista2[1]+'\n'
            f.write(x)
with open('grupa1.txt','a') as f:
    f.write('Media grupului 1: '+str(me1/y))
with open('grupa2.txt','a') as f:
    f.write('Media grupului 2: '+str(me2/u))
print('Media clasei: ',m/len(list1))