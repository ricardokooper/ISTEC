#André Pinto - 2023371
#Antonio Martins - 2023367
#Ricardo Paulo - 2023368


def eh_tabuleiro(tab):
    if not isinstance(tab, tuple):
        return False
    if len(tab) != 3:
        return False
    
# Verificamos se cada tuple no tab tem 3 elementos: 
    
    for elementos in tab:
        
        if not isinstance (elementos,tuple):
            return False
        if len(elementos) != 3: 
            return False 
 
 # verificar se os elementos de cada tuple são valores int
        for valor in elementos:
            if not isinstance(valor, int):
                return False
            if type(valor) == str:
                return False
    
    return True



def eh_posicao(pos):
    # Verifica se (pos) é um número inteiro no intervalo de 1 a 9, conforme tabela.
    if not isinstance(pos,int):
        return False
    if not 1<=pos<=9:
        return False 
    return True
    

def obter_coluna(tab,numero_coluna):
# obter coluna correspondente entre os valores 1 e 3 da tabela

# #verificar se tab é uma tabela conforme funçao eh_tabuleiro:
    if not eh_tabuleiro(tab):
        raise ValueError ("obter_coluna: algum dos argumentos e invalido")

# verificar se numero_coluna é um inteiro dentro do range (1:3):
    if not isinstance(numero_coluna,int) and not 1<=numero_coluna<=3:
        raise ValueError ("obter_coluna: algum dos argumentos e invalido")
# se o valor pedido for uma coluna que nao existe retorna erro
    if numero_coluna not in range(1,4):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
# direcionar o numero_coluna aos respectivos valores da coluna na tabela:
    # o 1º [ ] identifica o tuple, 2º[ ] identifica o elemento desse tuplo:

# se numero_coluna for 1, corresponde a posiçao 0 de cada tuple:
    if numero_coluna == 1:
        return (tab[0][0], tab[1][0], tab[2][0])

#se numero_coluna for 2, corresponde a posiçao 1 de cada tuple:
    if numero_coluna == 2:
        return (tab[0][1], tab[1][1], tab[2][1])

#se numero_coluna for 3, corresponde a posiçao 2 de cada tuple:
    if numero_coluna == 3:
        return (tab[0][2], tab[1][2], tab[2][2])


def obter_linha(tab,numero_linha):
#obter linha correspondente entre os valores 1 e 3 da tabela:
#verificar se tab é uma tabela conforme funçao eh_tabuleiro:
    if not eh_tabuleiro(tab):
        raise ValueError ("obter_linha: algum dos argumentos e invalido")


#verificar se numero_linha é um inteiro dentro do range (1:3):   
    if not isinstance(numero_linha,int):
        raise ValueError ("obter_linha: algum dos argumentos e invalido") 
    if numero_linha not in range(1,4):
        raise ValueError ("obter_linha: algum dos argumentos e invalido") 

# direcionar o numero_linha aos respectivos valores da linha na tabela:
# o tab[ ] identifica o tuple e o seu conteudo:
    
# se numero_linha for 1, corresponde a posiçao 0 do tuple tab:
    if numero_linha==1:
        return (tab[0])
# se numero_linha for 2, corresponde a posiçao 1 do tuple tab:
    if numero_linha==2:
        return (tab[1])
# se numero_linha for 3, corresponde a posiçao 2 do tuple tab:
    if numero_linha==3:
        return (tab[2])


   
def obter_diagonal(tab,numero_diag):
    #direcionar o numero_diagonal aos respectivos valores da diagonal na tabela:
    if not eh_tabuleiro(tab):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
#verificar se numero_diag é um inteiro dentro do range (1:2):     
    if not isinstance(numero_diag,int):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if numero_diag not in range(1,3):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')

#se o numero_diag for 1, corresponde (1,5,9) dos tuplos [0,1,2] respectivamente:   
    if numero_diag == 1:
        return (tab[0][0], tab[1][1], tab[2][2])
#se o numero_diag for 2, corresponde (7,5,3) dos tuplos [2,1,0] respectivamente:      
    if numero_diag == 2:
        return (tab[2][0], tab[1][1], tab[0][2])    
 


def tabuleiro_str(tab):
# funçao para transformar a tabela numa string para o utilizador:
    
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    #iniciar variavel em string para guardar o tabuleiro "visivel"
    tabuleiro = ''
    #iniciar indice para percorrer linhas
    ilinha = 0
    while ilinha < len(tab):
        #iniciar indice para percorrer as colunas
        coluna = 0
        #verificar todos os elementos e incrementar o loop 
        # para terminar quando acabar os elementos
        for linha in tab:
            while coluna < len(linha):
                if tab[ilinha][coluna] == 0:
                    tabuleiro = tabuleiro + '   '
                if tab[ilinha][coluna] == 1:
                    tabuleiro = tabuleiro + ' X '
                if tab[ilinha][coluna] == -1:
                    tabuleiro = tabuleiro + ' O '
                if coluna < 2:
                    tabuleiro = tabuleiro + '|'
                coluna = coluna + 1        
        if ilinha < 2:
            tabuleiro = tabuleiro + '\n-----------\n'
        ilinha = ilinha + 1
    return tabuleiro


def eh_posicao_livre(tab, pos):
    #validar se o tab e valido e se a posicao esta dentro dos valores validos
    if not eh_tabuleiro(tab):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if not isinstance(pos,int) or not 1 <= pos <= 9:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    
#divisao por 3 para calcular a linha:
    linha = (pos - 1) // 3
#resto da divisao por 3 encontramos o quadrante:  
    quadrante = (pos - 1) % 3       

    return tab[linha][quadrante]==0

def obter_posicoes_livres(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
# variavel para depositar as posicoes livre:
    resultado = ()
#posicoes de 1 a 9 da tabela:
    pos = 1
#Verifica se a posicao pos esta livre
    while pos <= 9:
        if eh_posicao_livre(tab, pos):
#Adiciona a posicao pos(este transformado em tuple) livre a variavel resultado
            resultado = resultado + (pos,)
#Incrementa a variavel pos
        pos = pos + 1
    return resultado       


def jogador_ganhador(tab):
    
    
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    i = 1
    #compara todos os valores 
    while i <= 2:
        if obter_linha(tab, i)[0] == obter_linha(tab, i)[1] == obter_linha(tab, i)[2]:
            return obter_linha(tab, i)[0]
        elif obter_coluna(tab, i)[0] == obter_coluna(tab, i)[1] == obter_coluna(tab, i)[2]:
            return obter_coluna(tab, i)[0]
        elif obter_diagonal(tab, i)[0] == obter_diagonal(tab, i)[1] == obter_diagonal(tab, i)[2]:
            return obter_diagonal(tab, i)[0]
        i = i + 1
    i = 3
    if obter_linha(tab, i)[0] == obter_linha(tab, i)[1] == obter_linha(tab, i)[2]:
        return obter_linha(tab, i)[0]
    elif obter_coluna(tab, i)[0] == obter_coluna(tab, i)[1] == obter_coluna(tab, i)[2]:
        return obter_coluna(tab, i)[0]
    
    return 0

def marcar_posicao(tab, jogador, posicao):
    
    
    if not eh_tabuleiro(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not type(jogador) == int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if jogador != -1 and jogador != 1:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not type(posicao) == int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    if not 1 <= posicao <= 9:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    if posicao not in obter_posicoes_livres(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    
    nova_linha = ()
    novotab = ()
    
    posicao = posicao - 1 
    
    if posicao // 3 == 0: # linha 1
        nova_linha = (tab[0][0:posicao]) + (jogador,) + (tab[0][posicao+1:3])
        novotab = (nova_linha,) + (tab[1:3])
        
        # posicao+1 devolve o valor inicial a posicao
        
    if posicao // 3 == 1: #linha 2
        posicao = posicao - 3 # garante que o indice do tuplo ira ficar entre 0 e 2
        nova_linha = (tab[1][0:posicao]) + (jogador,) + (tab[1][posicao+1:3])  
        novotab = (tab[0],) + (nova_linha,) + (tab[2],)
        
    if posicao // 3 == 2: #linha 3
        posicao = posicao - 6 # garante que o indice do tuplo fica entre 0 e 2
        nova_linha = (tab[2][0:posicao]) + (jogador,) + (tab[2][posicao+1:3])
        novotab = (tab[0:2]) + (nova_linha,) 
    
    return novotab

def escolher_posicao_manual(tab):
# valida todas as condicoes para que a posicao possa ser escolhida
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    
    posicao = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    
    if not eh_posicao(posicao):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')                
    
    if not type(posicao) == int:
        raise ValueError('escolher_posicao_manual: a posicao introduzida' + \
                         ' e invalida')        
    
    if posicao not in obter_posicoes_livres(tab):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return posicao

def escolher_posicao_auto(tab, bot, modo):
    
    
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if not type(bot) == int:
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')        
    if bot != 1 and bot != -1:
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if modo != 'basico' and modo != 'normal' and modo != 'perfeito':
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    
    if modo == 'basico':
        return modo_basico(tab, bot)
    if modo == 'normal':
        return modo_normal(tab, bot)
    if modo == 'perfeito':
        return modo_perfeito(tab, bot)
    
def canto(tab):
    if tab[0][0] == 0:
        return 1
    elif tab[0][2] == 0:
        return 3
    elif tab[2][0] == 0:
        return 7
    elif tab[2][2] == 0:
        return 9

def canto_possivel(tab):
    #avalia se a funcao canto tem algum valor ou se e nula e retorna true or false respetivamente
    if canto(tab) == None:
        return False
    return True

def lateral(tab):
    if tab[0][1] == 0:
        return 2
    elif tab[1][0] == 0:
        return 4
    elif tab[1][2] == 0:
        return 6
    elif tab[2][1] == 0:
        return 8    

def lateral_possivel(tab):
#avalia se a funcao lateral tem algum valor ou se e nula e retorna true or false respetivamente
    if lateral(tab) == None:
        return False
    return True
   
def canto_oposto(tab, bot):
    if tab[0][0] == 0 and tab[2][2] != bot and tab[2][2] != 0:
        return 1
    elif tab[0][2] == 0 and tab[2][0] != bot and tab[2][0] != 0:
        return 3
    elif tab[2][0] == 0 and tab[0][2] != bot and tab[0][2] != 0:
        return 7
    elif tab[2][2] == 0 and tab[0][0] != bot and tab[0][0] != 0:
        return 9

def canto_oposto_possivel(tab, bot):
#avalia se a funcao canto oposto tem algum valor ou se e nula e retorna true or false respetivamente   
    if canto_oposto(tab, bot) == None:
        return False
    return True

def vitoria(tab, bot):
   for n in range(1, 10):
    if eh_posicao_livre(tab, n):
        if jogador_ganhador(marcar_posicao(tab, bot, n)) == bot:
            return n


def vitoria_possivel(tab, bot):
    #avalia se a funcao vitoria tem algum valor ou se e nula e retorna true or false respetivamente   
    if vitoria(tab, bot) == None:
        return False
    return True

def bloqueio(tab, bot):
    for n in range(1, 10):
        if eh_posicao_livre(tab, n):
            if jogador_ganhador(marcar_posicao(tab, -bot, n)) == -bot:
                return n
    return None

    
def bloqueio_possivel(tab, bot):
    
    if bloqueio(tab, bot) == None:
        return False
    return True

def bifurcacao(tab, bot):
    # Procura uma linha, coluna ou diagonal com duas peças do jogador atual e uma posição vazia.
    for linha in range(3):
        for coluna in range(3):
            if tab[linha][coluna] == bot:
                #verificar se a linha tem duas pecas do jogador e uma posicao vazia
                if tab[linha][0] == bot and tab[linha][1] == bot and tab[linha][2] == 0:
                    return linha * 3 + coluna
                #verificar se a coluna tem duas pecas do jogador e uma posicao
                elif tab[0][coluna] == bot and tab[1][coluna] == bot and tab[2][coluna] == 0:
                    return linha * 3 + coluna
                #verificar se as diagonais tem duas pecas do jogador e uma posicao vazia
                elif tab[linha][0] == bot and tab[1][1] == bot and tab[2][2] == 0:
                    return linha * 3 + coluna
                elif tab[2][0] == bot and tab[1][1] == bot and tab[0][2] == 0:
                    return linha * 3 + coluna

    return None

def bifurcacao_possivel(tab,bot):
    if bifurcacao(tab,bot) == None:
        return False
    return True

def bloqueio_bifurcacao(tabuleiro, jogador):

  #verifica todas as linhas

  for i in range(3):
    if tabuleiro[i][0] != jogador and tabuleiro[i][1] != jogador and tabuleiro[i][2] == None:
      return (i, 2)
    if tabuleiro[i][1] != jogador and tabuleiro[i][2] != jogador and tabuleiro[i][0] == None:
      return (i, 0)
    if tabuleiro[i][0] != jogador and tabuleiro[i][2] != jogador and tabuleiro[i][1] == None:
      return (i, 1)

  #verifica todas as colunas

  for i in range(3):
    if tabuleiro[0][i] != jogador and tabuleiro[1][i] != jogador and tabuleiro[2][i] == None:
      return (2, i)
    if tabuleiro[1][i] != jogador and tabuleiro[2][i] != jogador and tabuleiro[0][i] == None:
      return (0, i)
    if tabuleiro[0][i] != jogador and tabuleiro[2][i] != jogador and tabuleiro[1][i] == None:
      return (1, i)

  #verifica as diagonais

  if tabuleiro[0][0] != jogador and tabuleiro[1][1] != jogador and tabuleiro[2][2] == None:
    return (2, 2)
  if tabuleiro[2][0] != jogador and tabuleiro[1][1] != jogador and tabuleiro[0][2] == None:
    return (0, 2)
  if tabuleiro[0][2] != jogador and tabuleiro[1][1] != jogador and tabuleiro[2][0] == None:
    return (2, 0)
  if tabuleiro[2][2] != jogador and tabuleiro[1][1] != jogador and tabuleiro[0][0] == None:
    return (0, 0)

  return None

def bloqueio_bifurcacao_possivel(tab,bot):
    if bloqueio_bifurcacao(tab,bot) == None:
        return False
    return True  

def modo_basico(tab, bot):
    if tab[1][1] == 0: #meio
        return 5
    #regra n7
    elif canto_possivel(tab):
        return canto(tab)
    #regra n8
    elif lateral_possivel(tab):
        return lateral(tab)

def modo_normal(tab, bot):
    #regra n1
    if vitoria_possivel(tab, bot):
        return vitoria(tab, bot)
    
    #regra n2
    elif bloqueio_possivel(tab, bot):
        return bloqueio(tab, bot)
            
    #regra n5
    elif tab[1][1] == 0: #centro
        return 5
            
    #regra n6
    elif canto_oposto_possivel(tab, bot):
        return canto_oposto(tab, bot)
            
    #regra n7
    elif canto_possivel(tab):
        return canto(tab)
                    
    #regra n8
    elif lateral_possivel(tab):
        return lateral(tab)
    
def modo_perfeito(tab, bot):
    #regra n1
    if vitoria_possivel(tab, bot):
        return vitoria(tab, bot)
    #regra n2
    elif bloqueio_possivel(tab, bot):
        return bloqueio(tab, bot)
    #regra n3
    elif bifurcacao_possivel(tab, bot):
       return bifurcacao(tab, bot)
    #regra n4
    elif bloqueio_bifurcacao_possivel(tab, bot):
        return bloqueio_bifurcacao(tab, bot)     
    #regra n5
    elif tab[1][1] == 0: #posicao 5
        return 5       
    #regra n6
    elif canto_oposto_possivel(tab, bot):
        return canto_oposto(tab, bot)      
    #regra n7
    elif canto_possivel(tab):
        return canto(tab)             
    #regra n8
    elif lateral_possivel(tab):
        return lateral(tab)    
    
def jogo_do_galo(jogador, dificuldade):
    
    
    if jogador != 'X' and jogador != 'O':
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    if dificuldade != 'basico' and dificuldade != 'normal' and dificuldade != 'perfeito':
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com ","'" ,jogador,"'.")
    
    if jogador == 'O':
        jogador = -1
    elif jogador == 'X':
        jogador = 1

    
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0)) # tabuleiro inicial
    
    while jogador_ganhador(tab) == 0:
        if jogador == -1:
            bot = 1
            print('Turno do computador :','(',dificuldade,')')
            
            tab = marcar_posicao(tab, bot, escolher_posicao_auto(tab, bot, dificuldade))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
            tab = marcar_posicao(tab, jogador, escolher_posicao_manual(tab))
        
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
        elif jogador == 1:
            bot = -1
            tab = marcar_posicao(tab, jogador, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'            
            
            print('Turno do computador :','(',dificuldade,')')
            tab = marcar_posicao(tab, bot, escolher_posicao_auto(tab, bot, dificuldade))
            print(tabuleiro_str(tab))
            
            if obter_posicoes_livres(tab) == ():
                return 'EMPATE'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if jogador_ganhador(tab) == 1:
                return 'X'
            


