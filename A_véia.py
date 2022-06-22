
from tkinter import *
# cores ---------------------------------------

co0 = "#FFFFFF"  # branca 
co1 = "#333333"  # preta pesado 
co2 = "#fcc058"  # laranja 
co3 = "#38576b"  # valor 
co4 = "#3297a8"   # azul 
co5 = "#fff873"   # amarela 
co6 = "#fcc058"  # laranja 
co7 = "#e85151"   # vermelha 
co8 = '#676a6e'  # Cinza
fundo = "#3b3b3b" # preto

# janela ----------------------------------------

janela = Tk()
janela.title('A véia')
res_x = '250'
res_y = '350'
resolucao = res_x + 'x' + res_y
janela.geometry(resolucao)

#  frame do placar---------------------------------

frame_placar = Frame(janela, width=res_x, height=100, bg=fundo)
frame_placar.grid(column=0, row=0)

label_O = Label(frame_placar, text='O', font=('Ivy 50 bold'), fg=co8, bg=fundo)
label_O.place(x=180,y=10)
label_X = Label(frame_placar, text='X', font=('Ivy 50 bold'), fg=co8, bg=fundo)
label_X.place(x=20,y=10)

label_p = Label(frame_placar, text=':', font=('Ivy 50 bold'), fg=co0, bg=fundo)
label_p.place(x=112,y=5)

# frame do jogo----------------------------------

frame = Frame(janela, width=res_x, height=250, bg=co1)
frame.grid(column=0, row=1, sticky=S)


# linhas verticais ---------------------------------
app_ = Label(frame, text='', height=27, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
app_.place(x=90, y=15)

app_ = Label(frame, text='', height=27, relief='flat', pady=4, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
app_.place(x=160, y=15)

# linhas horizontais -------------------------------
app_ = Label(frame, text='', width=190, relief='flat', padx=2,pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7 )
app_.place(x=25, y=80)

app_ = Label(frame, text='', width=190, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7 )
app_.place(x=25, y=150)

# parametros para as regras
jogador_1 = 'X'
jogador_2 = 'O'
jogador_atual = 'X'


# tabuleiro que a interface manipula -------------------------
tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]

# tabuleiro que o algoritmo MiniMax manipula pra testar as jogadas 
tabuleiro_minimax = [['','',''],['','',''],['','','']]

# função que controla os botões
def jogada(i):
    global jogador_atual
    if jogador_atual == 'X':
            cor = co7
    if jogador_atual == 'O':
        cor = co4

    
    if i == str(1):
        
        if b_0['text'] == '':
            if jogador_atual == 'X':
                b_0['fg'] = cor
                b_0['text'] = 'X'
                tabuleiro[0][0] = jogador_atual
                jogador_atual = 'O'
                print(tabuleiro)
            elif jogador_atual == 'O':
                b_0['fg'] = cor
                b_0['text'] = 'O'
                tabuleiro[0][0] = jogador_atual
                jogador_atual = 'X'
                print(tabuleiro)
    if i == str(2):

        if b_1['text'] == '':
            if jogador_atual == 'X':
                b_1['fg'] = cor
                b_1['text'] = 'X'
                tabuleiro[0][1] = jogador_atual
                jogador_atual = 'O'
                print(tabuleiro)
            elif jogador_atual == 'O':
                b_1['fg'] = cor
                b_1['text'] = 'O'   
                tabuleiro[0][1] = jogador_atual
                jogador_atual = 'X'  
                print(tabuleiro)  
           
    if i == str(3):

        if b_2['text'] == '':
            if jogador_atual == 'X':
                b_2['fg'] = cor
                b_2['text'] = 'X'
                tabuleiro[0][2] = jogador_atual  
                jogador_atual = 'O'
                print(tabuleiro)
            elif jogador_atual == 'O':
                b_2['fg'] = cor
                b_2['text'] = 'O' 
                tabuleiro[0][2] = jogador_atual     
                jogador_atual = 'X'
                print(tabuleiro) 
            
    if i == str(4):

        if b_3['text'] == '':
            if jogador_atual == 'X':
                b_3['fg'] = cor
                b_3['text'] = 'X'
                tabuleiro[1][0] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_3['fg'] = cor
                b_3['text'] = 'O' 
                tabuleiro[1][0] = jogador_atual  
                jogador_atual = 'X'

    if i == str(5):

        if b_4['text'] == '':
            if jogador_atual == 'X':
                b_4['fg'] = cor
                b_4['text'] = 'X'
                tabuleiro[1][1] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_4['fg'] = cor
                b_4['text'] = 'O' 
                tabuleiro[1][1] = jogador_atual
                jogador_atual = 'X'

    if i == str(6):

        if b_5['text'] == '':
            if jogador_atual == 'X':
                b_5['fg'] = cor
                b_5['text'] = 'X'
                tabuleiro[1][2] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_5['fg'] = cor
                b_5['text'] = 'O' 
                tabuleiro[1][2] = jogador_atual
                jogador_atual = 'X'

    if i == str(7):

        if b_6['text'] == '':
            if jogador_atual == 'X':
                b_6['fg'] = cor
                b_6['text'] = 'X'
                tabuleiro[2][0] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_6['fg'] = cor
                b_6['text'] = 'O' 
                tabuleiro[2][0] = jogador_atual
                jogador_atual = 'X'

    if i == str(8):

        if b_7['text'] == '':
            if jogador_atual == 'X':
                b_7['fg'] = cor
                b_7['text'] = 'X'
                tabuleiro[2][1] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_7['fg'] = cor
                b_7['text'] = 'O' 
                tabuleiro[2][1] = jogador_atual
                jogador_atual = 'X'

    if i == str(9):

        if b_8['text'] == '':
            if jogador_atual == 'X':
                b_8['fg'] = cor
                b_8['text'] = 'X'
                tabuleiro[2][2] = jogador_atual  
                jogador_atual = 'O'
            elif jogador_atual == 'O':
                b_8['fg'] = cor
                b_8['text'] = 'O' 
                tabuleiro[2][2] = jogador_atual
                jogador_atual = 'X'
    
    # acabar jogo na horizontal
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != '':
        if tabuleiro[0][0] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][0] == 'O':
            vencedor(jogador_2)
            
    if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != '':
        if tabuleiro[1][0] == 'X':
            vencedor(jogador_1)
        if tabuleiro[1][0] == 'O':
            vencedor(jogador_2)
    if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != '':
        if tabuleiro[2][0] == 'X':
            vencedor(jogador_1)
        if tabuleiro[2][0] == 'O':
            vencedor(jogador_2)

    #acabar jogo na vertical
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != '':
        if tabuleiro[0][0] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][0] == 'O':
            vencedor(jogador_2)
    if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != '':
        if tabuleiro[0][1] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][1] == 'O':
            vencedor(jogador_2)
    if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != '':
        if tabuleiro[0][2] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][2] == 'O':
            vencedor(jogador_2)

    #acabar o jogo na diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
        if tabuleiro[0][0] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][0] == 'O':
            vencedor(jogador_2)
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        if tabuleiro[0][2] == 'X':
            vencedor(jogador_1)
        if tabuleiro[0][2] == 'O':
            vencedor(jogador_2) 

# checa o vencedor e desabilita os campos
def vencedor(v):
    
    if v == jogador_1:
        marca_vencedor = 'X'
        label_X['fg'] = co7
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'
    if v == jogador_2:
        
        label_O['fg'] = co4
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

# prepara o tabuleiro para nova partida
def restart():
    global tabuleiro
    global tabuleiro_minimax
    global jogador_atual
    jogador_atual = 'X'
    tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
    tabuleiro_minimax = [['','',''],['','',''],['','','']]
    label_O['fg'] = co8
    label_X['fg'] = co8
    b_0['text'] = ''
    b_1['text'] = ''
    b_2['text'] = ''
    b_3['text'] = ''
    b_4['text'] = ''
    b_5['text'] = ''
    b_6['text'] = ''
    b_7['text'] = ''
    b_8['text'] = ''
    b_0['state'] = 'normal'
    b_1['state'] = 'normal'
    b_2['state'] = 'normal'
    b_3['state'] = 'normal'
    b_4['state'] = 'normal'
    b_5['state'] = 'normal'
    b_6['state'] = 'normal'
    b_7['state'] = 'normal'
    b_8['state'] = 'normal'

# chama o minimax e devolve a melhor jogada
def movimento_bot():
    
    for i,linha in enumerate(tabuleiro):
        for j, valor in enumerate(linha):
            if valor == 'X' or valor == 'O':

                tabuleiro_minimax[i][j] = valor
    best_score = -80
    best_move = 0
    for i, linha in enumerate(tabuleiro_minimax):
        for j, valor in enumerate(linha):
            if valor == '':
                tabuleiro_minimax[i][j] = jogador_1
                score = minimax(tabuleiro_minimax, False)
                tabuleiro_minimax[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move == (0,0):
        jogada = '1'
        return jogada
    if best_move == (0,1):
        jogada = '2'
        return jogada
    if best_move == (0,2):
        jogada = '3'
        return jogada 
    if best_move == (1,0):
        jogada = '4'
        return jogada
    if best_move == (1,1):
        jogada = '5'
        return jogada
    if best_move == (1,2):
        jogada = '6'
        return jogada
    if best_move == (2,0):
        jogada = '7'
        return jogada
    if best_move == (2,1):
        jogada = '8'
        return jogada
    if best_move == (2,2):
        jogada = '9'
        return jogada


"""Função recursiva, if ismax vai testar uma posição disponivel 
 e passar a vez pro jogador dois que seria o ismax=False, que por sua vez testa a posição 
 e chama o minimax novamente com a ismax
 até sair um ganhador ou empate"""
def minimax(tabuleiro_atual, ismax):
    if marcar_vencedor_partidas_simuladas(jogador_1):
        return 1
    elif marcar_vencedor_partidas_simuladas(jogador_2):
        return -1
    elif checar_empate():
        return 0

    if ismax:
        best_score = -80
        for i, linha in enumerate(tabuleiro_atual):
            for j, valor in enumerate(linha):
                if valor == '':
                    tabuleiro_minimax[i][j] = jogador_1
                    score = minimax(tabuleiro_atual, False)
                    tabuleiro_minimax[i][j] = ''
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = 80
        for i, linha in enumerate(tabuleiro_atual):
            for j, valor in enumerate(linha):
                if valor == '':
                    tabuleiro_minimax[i][j] = jogador_2
                    score = minimax(tabuleiro_atual, True)
                    tabuleiro_minimax[i][j] = ''
                    if score < best_score:
                        best_score = score
        return best_score
    
# checar se foi empate
def checar_empate():
    for i,linha in enumerate(tabuleiro_minimax):
        for j, valor in enumerate(linha):
            if valor == '':
                return False

    return True

# marca quem ganhou nas partidas simulados do minimax e é a condição de parada da função recursiva
def marcar_vencedor_partidas_simuladas(mark):
        #horizontal
        if tabuleiro_minimax[0][0] == tabuleiro_minimax[0][1] and tabuleiro_minimax[0][0] == tabuleiro_minimax[0][2] and tabuleiro_minimax[0][0] == mark:
            return True
        elif (tabuleiro_minimax[1][0] == tabuleiro_minimax[1][1] and tabuleiro_minimax[1][0] == tabuleiro_minimax[1][2] and tabuleiro_minimax[1][0] == mark):
            return True
        elif (tabuleiro_minimax[2][0] == tabuleiro_minimax[2][1] and tabuleiro_minimax[2][0] == tabuleiro_minimax[2][2] and tabuleiro_minimax[2][0] == mark):
            return True
        #vertical
        elif (tabuleiro_minimax[0][0] == tabuleiro_minimax[1][0] and tabuleiro_minimax[0][0] == tabuleiro_minimax[2][0] and tabuleiro_minimax[0][0] == mark):
            return True
        elif (tabuleiro_minimax[0][1] == tabuleiro_minimax[1][1] and tabuleiro_minimax[0][1] == tabuleiro_minimax[2][1] and tabuleiro_minimax[0][1] == mark):
            return True
        elif (tabuleiro_minimax[0][2] == tabuleiro_minimax[1][2] and tabuleiro_minimax[0][2] == tabuleiro_minimax[2][2] and tabuleiro_minimax[0][2] == mark):
            return True
        #diagonal
        elif (tabuleiro_minimax[0][0] == tabuleiro_minimax[1][1] and tabuleiro_minimax[0][0] == tabuleiro_minimax[2][2] and tabuleiro_minimax[0][0] == mark):
            return True
        elif (tabuleiro_minimax[0][2] == tabuleiro_minimax[1][1] and tabuleiro_minimax[0][2] == tabuleiro_minimax[2][0] and tabuleiro_minimax[0][2] == mark):
            return True
        else:
            return False


# botões
b_0 = Button(frame, command= lambda: jogada('1'), text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_0.place(x=35, y=21)

b_1 = Button(frame, command= lambda: jogada('2'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_1.place(x=104, y=21)

b_2 = Button(frame, command= lambda: jogada('3'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_2.place(x=169, y=21)

b_3 = Button(frame, command= lambda: jogada('4'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_3.place(x=35, y=92)

b_4 = Button(frame, command= lambda: jogada('5'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_4.place(x=104, y=92)

b_5 = Button(frame, command= lambda: jogada('6'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_5.place(x=169, y=92)

b_6 = Button(frame, command= lambda: jogada('7'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_6.place(x=35, y=162)

b_7 = Button(frame, command= lambda: jogada('8'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_7.place(x=104, y=162)

b_8 = Button(frame, command= lambda: jogada('9'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_8.place(x=169, y=162)

b_9 = Button(frame, command= lambda: restart(),text='RESTART', width=7,height=0, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co5 )
b_9.place(x=7, y=215)

b_10 = Button(frame, command= lambda: jogada(movimento_bot()),text='BOT', width=7,height=0, relief='flat', padx=1, pady=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co5 )
b_10.place(x=160, y=215)






































janela.mainloop()