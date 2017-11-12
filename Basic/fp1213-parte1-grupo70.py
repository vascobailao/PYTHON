#Bernardo Graça 75631
#Vasco Fernandes 76462
from NASA import*


s=dimensoes()
#Esra funcao vai calcular a temperatura em pontos em que a função conteudo nao devolve uma string e quando a função conteudo devolve uma string e/ou algum dos pontos à volta é ruído.
def temp (c,l):
    c1=s[0]
    l1=s[1]
    tempt=0
    if conteudo(c,l) != ' ':
        return conteudo(c,l)
    elif conteudo(c,l) == ' ':
                n=1
                soma= 0
                if conteudo(c+n,l+n)!= ' ' :
                    soma = soma +1
                    tempt=tempt+conteudo(c+n,l+n)
                                 
                elif conteudo (c-n,l)!= ' ':
                    soma= soma +1
                    tempt=tempt+conteudo(c-n,l)
                                   
                elif conteudo(c-n,l+n)!= ' ':
                    soma= soma +1
                    tempt=tempt+conteudo(c-n,l+n)
                                   
                elif conteudo(c,l+n)!= ' ':
                    soma= soma +1
                    tempt=tempt+conteudo(c,l+n)
                
                elif conteudo(c,l-n)!= ' ':
                    soma=soma+1
                    tempt=tempt+conteudo(c,l-n)          
                    
                elif conteudo(c+n,l-n)!= ' ':
                    soma=soma+1
                    tempt=tempt+conteudo(c+n,l-n)                 
                    
                elif conteudo(c+n,l)!= ' ':
                    soma=soma+1
                    tempt=tempt+conteudo(c+n,l)                 
                    
                elif conteudo(c-n,l-n)!= ' ':
                    soma=soma+1
                    tempt=tempt+conteudo(c-n,l-n)               
                    
                temp1 = tempt/soma
    return temp1
    
#A função pontofinal devolve como resultado a posição final do caminho.       
def pontofinal(c,l):
    s=dimensoes()
    c1=s[0]
    l1=s[1]
    if l<=s[1]//2:
        return (c,s[1])
    if l>s[1]//2:
        return (c1//2,s[1]-s[1])

#A função caminho descreve o caminho e a temperatura de cada um dos pontos do caminho.
def caminho(c,l):
    r=[]
    s=dimensoes()
    c1=s[0]
    l1=s[1]
    if c<c1//2:
        while c!=c1//2:
            temp(c,l)
            c=c+1
            r=r+[temp(c,l)]
    elif c>c1//2:
        while c!=c1//2:
            temp(c,l)
            c=c-1
            r=r+[temp(c,l)]
    else:
        temp(c,l)
    if l<=l1//2:
        while l!=l1:
            temp(c,l)
            l=l+1
            r=r+[temp(c,l)]
    else:
        while l!=0:
            temp(c,l)
            l=l-1
            r=r+[temp(c,l)]
    return r

#A função média devolve a média da temperatura ao longo do caminho.
def media(r):
    res= 0
    for i in r:
        res = res +i
    return res/len(r)
 
        
      
    
        
#A função temperaturas devolve uma lista com a posição inicial, o ponto em que muda de caminho, o ponto final, a média das temperaturas ao longo do caminho e as temepraturas de todos os pontos ao longo do percurso
def temperaturas(c,l):
        lista=[]
        r=0
        temp=media(caminho(c,l))
        lista1=caminho(c,l)
        s=dimensoes()
        c1=s[0]
        l1=s[1]
        PI_caminho=(c1//2,l)
        primeira_posicao=(c,l)
        Pontofim=pontofinal(c,l)
        lista_tuplos=[]
        lista=lista+[primeira_posicao]+[PI_caminho]+[Pontofim]+[temp]+[lista1]
        return lista         
    