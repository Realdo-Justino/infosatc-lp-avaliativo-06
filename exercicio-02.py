variavel=""
opcao="s"
import re

def procura(variavel):
    falso=0
    certo=0
    for i in variavel:
            if(i=="{"):
                for teste in variavel:
                    if(teste=="}"):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
            if(i=="["):
                for teste in variavel:
                    if(teste=="]"):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
            if(i=="("):
                for teste in variavel:
                    if(teste==")"):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
            if(i=="}"):
                for teste in variavel:
                    if(teste=="{"):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
            if(i=="]"):
                for teste in variavel:
                    if(teste=="["):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
            if(i==")"):
                for teste in variavel:
                    if(teste=="("):
                        certo=1
                if (certo==1):
                    pass
                else:
                    falso=1
    return falso

while(opcao=="s"):
    falso=0
    regex = re.compile('[()}{]')
    contador=0
    variavel=input("Insira os valores ")
    for i in variavel:
        if((regex.search(i) == None)and (i!="[")and (i!="]")):
            contador=contador+1
        else:
            opcao="n"
    if(contador==0):
        falso=procura(variavel)
        print(falso)
    if(falso==1):
        contador=1
    if(contador>0):
        opcao="s"
        print("Valor inlido por favor insira apenas os valores seguintes: (){}[]")
print("Verdadeiro, ",variavel)
        
                