numero=0
lista=[]
opcao="s"

while(opcao=="s"):
    lista.append(input("Insira um numero \n"))
    opcao=input("Deseja adicionar mais um numero? \n")

opcao=input("Deseja modificar a lista ? s/n \n")

while(opcao=="s"):
    contador=0
    numero=float(input("Insira um numero: \n"))
    if(numero>0):
        for i in lista:
            contador=contador+1
        lista.insert(contador,lista[0])
        lista.pop(0)
        print(lista)
    else:
        for i in lista:
            contador=contador+1
        contador=contador-1
        lista.insert(0,lista[contador])
        contador=contador+1
        lista.pop(contador)
        print(lista)
    opcao=input("Deseja modificar a lista novamente? \n")