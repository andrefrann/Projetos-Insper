with open("nomes.txt","r") as arquivo:
    lista = []
    for linha in arquivo:
        lista.append(linha)
lista_f = []
for i in lista:
    x = i.lower()    #Deixa tudo em minúsculo
    x = i.title()    #Deixa todas as primeiras letras maiúsculas
    a = x.split()    #Separa todos os elementos em uma lista
    for n,i in enumerate(a):
        if i == "E":
            a[n] = "e"
        if i == "Dos":
            a[n] = "dos"
        if i == "Das":
            a[n] = "das"
        if i == "Do":       #Tira as letras maíusculas das ligações do nome ("do","da",etc)
            a[n] = "do"
        if i == "Da":
            a[n] = "da"
        if i == "De":
            a[n] = "de"
        if i == '\n':
            a[n] = ''
        nomes = []
    for i in a:
        if not i in nomes:
            nomes.append(i)   #Tira os sobrenomes duplicados
        lista_final = " ".join(nomes)
        z = ' '.join(nomes)
    if z not in lista_f:
        final = lista_f.append(z)   #Tira os nomes duplicados
    resultado = '\n'.join(lista_f)
print(resultado)




            

