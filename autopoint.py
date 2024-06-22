# Programa de pesquisa automática para ganhar pontos no edge
# 90 pontos dividido por 3 = 30 pesquisas
import pyautogui as pg
import time
pg.PAUSE = 0.5
# variaveis para cortar codigo
cl = pg.click
es = pg.write
pr = pg.press
tm = time.sleep
# lista dos temas a pesquisar
# foi colocado mais que o necessario para segurança de receber todos os pontos
lista_pesquisa = [
      'bitcoin','economia','blockchain','dolar','windows xp','engengaria de software','ciencia da computacao','arquitetura de computadores','exploit','trojan', 'kali linux','cobol','industria 4.0',
    'nanotecnologia','analista de sistemas','microsoft','redes de computadores','bug bounty','assembly', 'robo humanoides', 'espionagem virtual','ddos','hotkey','ubuntu',
    'i.a','ethernet','eniac','alan turing','eu robo', 'futurismo','display lsd','bluetooth','5G','arduino','raspbarry pi' ]
# Passo 1 - entrar no edge
pr("win")
tm(0.9)
es("edge")
pr('enter')
tm(3)
# caso abra a tela minimizada, será apertado o atalho de maximizar
pg.hotkey("win", "up")
######################################
# Passo 2 - repetiçao para eliminar 150 linhas de código de busca, tornando muito mais inteligente e simples
for pesquisa in lista_pesquisa:
    es(pesquisa)
    pr('enter')
    tm(7)
    # clica no x de limpar busca
    cl(x=716, y=111)
    tm(1.5)