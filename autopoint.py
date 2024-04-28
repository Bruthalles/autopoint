# Programa de pesquisa automática para ganhar pontos no edge
# 90 pontos dividido por 3 = 30 pesquisas

import pyautogui as pg
import time
pg.PAUSE = 0.5

#variaveis para cortar codigo

cl = pg.click
es = pg.write
pr = pg.press
tm = time.sleep

# lista dos temas a pesquisar
#foi colocado mais que o necessario para segurança de receber todos os pontos

lista_pesquisa = [
    'bitcoin','economia','italia','pangeia','peste negra','jogo do dinheiro','urss','2077','egito',      'trojan', 'isometria','1984','triplice alianca'
    'medicina','ibge','microsoft','black mirror','dropshipping','alemanha dividida', 'aristocrata', 'estelionatario','feudalismo','cerejeiras','guerra fria',
    'i.a','ethernet','eniac','alan turing','eu robo', 'revolucoes','napoleao','cristovao','RJ','suica','fruta guarana' ]

#funçao para ver pontos (final da barra)
def ver_pontos ():
        
    cl(x=1180, y=114)
    time.sleep(1)
    cl(x=1302, y=296)
    
    time.sleep(1)
    pg.scroll(-40000)
    time.sleep(1)

#funcao para entrar na barra de pontos (inicio)
def barra_pontos():
    
    es('ponto')
    pr('enter')

    time.sleep(6)
    cl(x=1182, y=104)
    time.sleep(1)
    
#Passo 1 - entrar no edge

pr("win")
time.sleep(0.9)
es("edge")
pr('enter')
time.sleep(3)

# caso abra a tela minimizada, será apertado o atalho de maximizar
pg.hotkey("win","up")
######################################
barra_pontos()

# botao direcionar para area de pesquisa
cl(x=1097, y=689)
time.sleep(3)

#Passo 2 - repetiçao para eliminar 150 linhas de código de busca, tornando muito mais inteligente e simples
for pesquisa in lista_pesquisa:
    es(pesquisa)
    pr('enter')
    tm(7)

    # clica no x de limpar busca
    cl(x=716, y=111)
    tm(1.5)

ver_pontos()
