# = = = PROJECTO DE FP - 2a parte = = = #
#
#  - Grupo 30 - 
#  
#  Bernardo Marques Graca           numero 76531
#  Rui Miguel Hungria Furtado       numero 76379
#  Vasco Bailao Martins Fernandes   numero 76462


# = = = Modulos exteriores = = = # 

from robot import* 

from testes_tai import*

import time

# = = = Definicao de tipos = = = #

# - - Tipo objecto - - #

espaco= 'espaco'
comida= 'comida'
parede= 'parede'
monstro='monstro'
premio='premio'
desconhecido='desconhecido'


# # ========================================================================
# # RECONHECEDORES
# # ========================================================================
# # espaco_p: universal -> logico
# # espaco_p(e) tem o valor verdadeiro se e for do tipo espaco e falso caso contrario.

def espaco_p(e):
    return e==espaco
    
# # comida_p: universal -> logico
# # comida_p(c) tem o valor verdadeiro se c for do tipo comida e falso caso contrario.    

def comida_p(c):
    return c==comida
      
# # parede_p: universal -> logico
# # parede_p(p) tem o valor verdadeiro se p for do tipo parede e falso caso contrario.

def parede_p(p):
    return p==parede
   
# # monstro_p: universal -> logico
# # monstro_p(m) tem o valor verdadeiro se m for do tipo monstro e falso caso contrario.    

def monstro_p(m):
    return m==monstro

# # premio_p: universal -> logico
# # premio_p(pm) tem o valor verdadeiro se pm for do tipo premio e falso caso contrario.

def premio_p(pm):
    return pm==premio

# # desconhecido_p: universal -> logico
# # desconhecido_p(d) tem o valor verdadeiro se d for do tipo desconhecido e falso caso contrario.

def desconhecido_p(d):
    return d==desconhecido
 
# - - Tipo direccao - - #

norte='norte'
sul='sul'
este='este'
oeste='oeste'

# ========================================================================
#  RECONHECEDORES
# ========================================================================
#  norte_p: universal -> logico
#  norte_p(d) tem o valor verdadeiro se d for do tipo norte e falso caso contrario
#  com d correspondendo a direccao

def norte_p(d):
    return d==norte
   
#  sul_p: universal -> logico
#  sul_p(d) tem o valor verdadeiro se d for do tipo sul e falso caso contrario
#  com d correspondendo a direccao

def sul_p(d):
    return d==sul
        
#  este_p: universal -> logico
#  este_p(d) tem o valor verdadeiro se d for do tipo este e falso caso contrario
#  com d correspondendo a direccao

def este_p(d):
    return d==este
    
#  oeste_p: universal -> logico
#  oeste_p(d) tem o valor verdadeiro se d for do tipo oeste e falso caso contrario    
#  com d correspondendo a direccao

def oeste_p(d):
    return d==oeste
    
# ========================================================================
# OPERACOES 
# ========================================================================
# vira_esquerda: direccao -> direccao
# vira_esquerda(d) devolve a direccao a esquerda da direccao para onde o robot 
# onde o robot esta direccionado 
# vira_esquerda(d) toma a direccao oeste se a direccao d for norte 
# vira_esquerda(d) toma a direccao sul se a direccao d for oeste
# vira_esquerda(d) toma a direccao este se a direccao d for sul
# vira_esquerda(d) toma a direccao norte se a direccao d for este

def vira_esquerda(d):
    if d==norte:
        return oeste
    if d==oeste:
        return sul
    if d==sul:
        return este
    if d==este:
        return norte

# vira_direita: direccao -> direccao
# vira_direita(d) devolve a direccao a direita da direccao para onde robot 
# onde robot esta direccionado
# vira_direita(d) toma a direccao este se a direccao d for norte 
# vira_direita(d) toma a direccao sul se a direccao d for este
# vira_direita(d) toma a direccao oeste se a direccao d for sul
# vira_direita(d) toma a direccao norte se a direccao d for oeste

def vira_direita(d):
    if d==norte:
        return este
    if d==este:
        return sul
    if d==sul:
        return oeste
    if d==oeste:
        return norte

# - - Tipo posicao - - #

# ========================================================================
# CONSTRUTOR
# ========================================================================
# posicao : inteiro X inteiro -> posicao
# a posicao ira receber dois inteiros correspondentes a linha e a coluna
# respectivamente e ira devolver a posicao (um tuplo) que contem a linha
# e a coluna

class posicao:
    
        def __init__ (self,linha,coluna):
            if(isinstance(coluna,int) and isinstance(linha,int)and (coluna>=0) and (linha>=0)):
                self.col=coluna
                self.linh=linha
            else:
                raise TypeError('posicao: args devem ser inteiros nao negativos')
            
        def __repr__(self):
            return '('+str(self.linh)+','+str(self.col)+')'

#========================================================================
# SELECTORES
#========================================================================
# posicao_linha: linha -> inteiro nao negativo
# posicao_linha(self): tem como valor a linha da posicao escolhida .

        def posicao_linha(self):
            return self.linh        
        
# posicao_coluna: coluna -> inteiro nao negativo
# posicao_coluna(self): tem como valor a coluna da posicao escolhida .
        
        def posicao_coluna(self):
            return self.col

#========================================================================
# TESTES
#========================================================================
# posicao_igual: posicao X posicao -> logico
# posicao_igual(self, posicao2), tera o valor verdadeiro se as posicoes
# self e posicao2 forem iguais e falso caso contrario.        
        
        def posicao_igual(self,posicao2):
            if self.col==posicao2.col and self.linh==posicao2.linh:
                return True
            return False

#========================================================================
# OPERACOES 
#========================================================================
# posicao_relativa: posicao X direccao -> direccao
# posicao_relativa(self,direc) devolve a posicao adjacente relativamente  
# onde o robot esta direccionado 
# se o robot estiver virado para norte, a posicao adjacente sera uma
# nova posicao imediatamente na linha acima mas na mesma coluna
# se o robot estiver virado para sul, a posicao adjacente sera uma
# nova posicao imediatamente na linha abaixo mas na mesma coluna
# se o robot estiver virado para este, a posicao adjacente sera uma
# nova posicao imediatamente na coluna adireita mas na mesma linha
# se o robot estiver virado para oeste, a posicao adjacente sera uma
# nova posicao imediatamente na coluna a esquerda mas na mesma linha        
        
        def posicao_relativa(self,direc):
            if direc==norte:
                return posicao(self.linh-1,self.col)
            elif direc==sul:
                return posicao(self.linh+1,self.col)
            elif direc==este:
                return posicao(self.linh,self.col+1)
            elif direc==oeste:
                return posicao(self.linh,self.col-1)
            else:
                raise TypeError('o argumento dado nao corresponde a uma direccao')       
            

# - - Tipo mapa - - #


# ========================================================================
# CONSTRUTORES
# ========================================================================
# mapa: -> mapa
# cria_mapa

class mapa:
    
        def __init__(self):
            self.mapa={}

# mapa_poe_o_objecto_em: mapa X posicao X objecto -> mapa
# a funcao mapa_poe_objecto(self,posicao,objecto), ira desenvolver um novo mapa
# no qual colocara o objecto dado na posicao fornecida

        def mapa_poe_objecto_em(self,posicao,objecto):
            if objecto==premio or espaco or comida or monstro or parede or desconhecido and isinstance(posicao,posicao) :
                self.mapa[posicao]=objecto
                return self

#========================================================================
# SELECTORES
#=======================================================================
# mapa_objecto_em: mapa X posicao -> objecto
# mapa_objecto_em(self,posicao): devera devolver o objecto ao qual corresponde
# a posicao fornecida.

    
        def mapa_objecto_em(self,posicao):    
            for posicao in self.mapa:
                if posicao in self.mapa:
                    return self.mapa[posicao]
                else:
                    return desconhecido

# mapa_altura: mapa -> inteiro nao negativo
# mapa_altura(self): ira devolver a altura do retangulo que envolve a area
# explorada, incluindo as paredes envolventes. A altura inicial sera 1 pois 
# ja conhecemos a primeira posicao ocupada pelo robot
        
        def mapa_altura (self):
            altura=1
            for posicao in self.mapa.keys():
                if posicao.posicao_linha()>altura:
                    altura=posicao.posicao_linha()+1
            return altura

# mapa_largura: mapa -> inteiro nao negativo
# mapa_largura(self): ira devolver a largura do retangulo que envolve a area
# explorada, incluindo as paredes envolventes. A largura inicial sera 1 pois 
# ja conhecemos a primeira posicao ocupada pelo robot
        
        def mapa_largura(self):
            largura=1
            for posicao in self.mapa.keys():
                if posicao.posicao_coluna()>largura:
                    altura=posicao.posicao_coluna()+1
            return altura
        
#Como usamos dicionarios, foi pedido pelos professores a funcao __eq__ para que
#a funcao mapa_objecto_em funcionasse bem
        
        def __eq__(self,outro):
            return self.posicao_igual(outro)
                  
#Como usamos dicionarios, foi pedido pelos professores a funcao __eq__ para que
#a funcao mapa_objecto_em funcionasse bem

        def __hash__(self):
            return self.l**2+self.c**3  
    
# ==============================================================================
# CONSTRUTOR
# ==============================================================================
# caminho : posicao -> caminho
# caminho cria um caminho apenas com uma posicao quando a origem e o destino sao
# sao coincidentes
# considera-se o caminho uma lista pois e necessario que este seja alteravel          

class caminho:
    
    def __init__(self,pos):
            if isinstance(pos,posicao):
                self.cm=[pos]
            else:
                raise ValueError \
                      ('os argumentos dados nao sao uma posicao')
            
#Esta funcao faz com que o caminho seja representado por uma lista
    
    def __repr__(self):
        s = '[ '
        for i in self.cm:
            s = s + str(i) + ' '
        return s + ']'
    
# caminho_carrega: esta funcao faz com que as posicoes sejam "descarregadas" 
# para uma lista nova, para que nas funcoes caminho_apos_origem e
# caminho_antes_destino possa ser usada uma lista que possa ser modificada
    def caminho_carrega(self, lista):
        for i in lista:
            if not isinstance(i, posicao):
                raise ValueError ('A funcao nao devolve uma lista')
        self.cm = lista
        
# caminho_junta_posicao: caminho X direccao -> caminho
# caminho_junta_posicao altera o caminho existente juntando um novo caminho
# adjacente ao destino dado na direccao dada
        
    def caminho_junta_posicao(self,direccao):
        self.cm= self.cm +[self.cm[-1].posicao_relativa(direccao)]
        return self
        
# ==============================================================================
# SELECTORES
# ==============================================================================
# caminho_origem: caminho -> posicao
# caminho_origem recebe um caminho e devolve a posicao origem desse mesmo 
# caminho
                
    def caminho_origem(self):
        return self.cm[0]
    
    
# caminho_destino : caminho -> posicao
# caminho_destino recebe um caminho e devolve a posicao destino desse mesmo caminho
    def caminho_destino(self):
        return self.cm[-1]
       
# caminho_comprimento: caminho -> inteiro
# caminho_comprimento devolve o comprimento do caminho ou seja quantas
# posicoes existem nele
       
    def caminho_comprimento(self):
        return len(self.cm)    
    
# ===========================================================================
# OPERACOES
# ===========================================================================
# caminho_apos_origem: caminho -> caminho
# caminho_apos_origem recebe um caminho e devolve o caminho sem a origem
        
    def caminho_apos_origem(self):
        c = caminho(self.caminho_origem())
        c.caminho_carrega(self.cm[1:])
        return c
    
# caminho_antes_destino : caminho -> caminho
# caminho_antes_destino recebe um caminho e devolve o caminho sem o destino
    
    def caminho_antes_destino(self):
            c = caminho(self.caminho_origem())
            c.caminho_carrega(self.cm[:-1])
            return c    
    
# caminho_elimina_ciclos : caminho -> caminho
# caminho_elimina_ciclos devolve um caminho que resulta do caminho dado
# depois de eliminar todas as posicoes que constituem ciclos no caminho 

    def caminho_elimina_ciclos(self):
        lista=self.cm[:]
        for i in range(len(lista)):
            for j in range (i+1, len(lista)):
                if lista[i].posicao_igual(lista[j]):
                    del lista[i:j]
        x=caminho(lista[0])
        for y in range (1,len(lista)):
            x.cm+=caminho(lista[y]).cm
        return x
            
    
# ===========================================================================
# TESTES
# ===========================================================================
# caminho_contem_ciclo : caminho -> logico
# caminho_contem_ciclo devolve o valor True se o caminho dado passa duas
# vezes pela mesma posicao e False caso contrario
    
    def caminho_contem_ciclo(self):
        for i in range (len(self.cm)):
            for el in self.cm[i+1:]:
                if self.cm[i].posicao_igual(el):
                    return True
        return False
            

   
    
# ===========================================================================
# CONSTRUTORES
# ===========================================================================
# estado: posicao X direccao -> estado
# estado recebe a posicao e a direccao inicial do robot e devolve o 
# estado em que o robot se encontra na posicao e direccao dadas    

class estado:
        
    def __init__(self,pos,direc):
        if (isinstance(pos,posicao)) and direc==norte or sul or este or oeste:
            self.p=pos
            self.d=direc
            self.m=mapa()
            self.c=caminho(pos)
            self.e=[(self.p),(self.d),(self.m),(self.c)]

# ===========================================================================
# OPERACOES
# ===========================================================================
# estado_robot_avanca: estado -> estado 
# estado_robot_avanca recebe um estado e devolve um novo estado que
# corresponde a situacao que resulta de avancar uma casa
    
    def estado_robot_avanca (self):
        self.c=self.c.caminho_junta_posicao(self.d)
        self.m=self.m.mapa_poe_objecto_em(self.p,espaco)
        self.p=self.p.posicao_relativa(self.d)
        return self     
        
# estado_robot_vira_direita: estado -> estado
# estado_robot_vira_direita recebe um estado e devolve um outro estado 
# correspondente a mudanca de direccao a direita
    
    def estado_robot_vira_direita(self):
        self.d=vira_direita(self.d)
        return self        
           
# estado_robot_vira_esquerda: estado -> estado
# estado_robot_vira_esquerda recebe um estado e devolve um outro estado 
# correspondente a mudanca de direccao a esquerda
    
    def estado_robot_vira_esquerda(self):
        self.d=vira_esquerda(self.d)
        return self
    
    def actualiza_mapa(self,objecto):
        self.m.mapa_poe_objecto_em(self,pos,objecto)
        return self
    
# ===========================================================================
# SELECTORES
# ===========================================================================
    def estado_robot_apanha(self):
        return self
           
    def estado_robot_dispara(self):
        return self

# estado_posicao_robot: estado->posicao
# estado_posicao_robot recebe um estade e devolve a posicao desse estado

    def estado_posicao_robot(self):
        return self.p
    
# estado_direccao_robot: estado->direccao
# estado_direccao_robot: recebe um estado e devolve a direccao desse estado
    
    def estado_direccao_robot(self):
        return self.d        

# estado_caminho_percorrido: estado->caminho
# estado_caminho_percorrido: recebe um estado e devolve o caminho desse estado
        
    def estado_caminho_percorrido(self):
        return self.c
        
# estado_mapa: estado->mapa
# estado_mapa: recebe um estado e devolve o mapa desse estado
    
    def estado_mapa(self):
        return self.m    
            

    
    
    
# = = = Controlo do Robot = = = #

# controla_robot : robot -> str x estado
    
def controla_robot(canal,e):
    time.sleep(0.2)
    energia=robot_energia(canal)
    if energia==0:
        robot_desliga(canal) 
    else:
        if e.estado_posicao_robot().posicao_relativa(e.estado_direccao_robot()) not in e.estado_caminho_percorrido().cm:
            if robot_sente_espaco(canal):
                robot_anda(canal)
                return 'robot anda',e.estado_robot_avanca()
                
            if robot_sente_parede(canal):
                robot_vira_direita(canal)
                return 'vira_direita',e.estado_robot_vira_direita()
            
            #if robot_sente_parede(canal):
                #robot_vira_esquerda(canal)
                #return 'vira_esquerda',e.estado_robot_vira_esquerda()
                     
            if robot_sente_monstro(canal):
                robot_dispara(canal)
                return 'robot_dispara',e.estado_robot_dispara()
                    
            if robot_sente_comida(canal) or robot_sente_premio(canal):
                robot_apanha(canal)
                return 'robot_apanha',e.estado_robot_apanha()
        else:
            robot_vira_direita(canal)
            return 'vira_direita',e.estado_robot_vira_direita()       