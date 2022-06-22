
from tkinter import *
from tkinter import ttk
import random

from numpy import size

# cores ---------------------------------------

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = '#676a6e'  
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

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


jogador_1 = 'X'
jogador_2 = 'O'
jogando = 'X'



tabela = [[1,2,3],[4,5,6],[7,8,9]]
board = [['','',''],['','',''],['','','']]


def jogano(i):
    global jogando
    if jogando == 'X':
            cor = co7
    if jogando == 'O':
        cor = co4
    # if jogando == 'O':
    #     robo()
    
    
    if i == str(1):
        
        if b_0['text'] == '':
            if jogando == 'X':
                b_0['fg'] = cor
                b_0['text'] = 'X'
                tabela[0][0] = jogando
                jogando = 'O'
                print(tabela)
            elif jogando == 'O':
                b_0['fg'] = cor
                b_0['text'] = 'O'
                tabela[0][0] = jogando
                jogando = 'X'
                print(tabela)
    if i == str(2):

        if b_1['text'] == '':
            if jogando == 'X':
                b_1['fg'] = cor
                b_1['text'] = 'X'
                tabela[0][1] = jogando
                jogando = 'O'
                print(tabela)
            elif jogando == 'O':
                b_1['fg'] = cor
                b_1['text'] = 'O'   
                tabela[0][1] = jogando
                jogando = 'X'  
                print(tabela)  
           
    if i == str(3):

        if b_2['text'] == '':
            if jogando == 'X':
                b_2['fg'] = cor
                b_2['text'] = 'X'
                tabela[0][2] = jogando  
                jogando = 'O'
                print(tabela)
            elif jogando == 'O':
                b_2['fg'] = cor
                b_2['text'] = 'O' 
                tabela[0][2] = jogando     
                jogando = 'X'
                print(tabela) 
            
    if i == str(4):

        if b_3['text'] == '':
            if jogando == 'X':
                b_3['fg'] = cor
                b_3['text'] = 'X'
                tabela[1][0] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_3['fg'] = cor
                b_3['text'] = 'O' 
                tabela[1][0] = jogando  
                jogando = 'X'

    if i == str(5):

        if b_4['text'] == '':
            if jogando == 'X':
                b_4['fg'] = cor
                b_4['text'] = 'X'
                tabela[1][1] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_4['fg'] = cor
                b_4['text'] = 'O' 
                tabela[1][1] = jogando
                jogando = 'X'

    if i == str(6):

        if b_5['text'] == '':
            if jogando == 'X':
                b_5['fg'] = cor
                b_5['text'] = 'X'
                tabela[1][2] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_5['fg'] = cor
                b_5['text'] = 'O' 
                tabela[1][2] = jogando
                jogando = 'X'

    if i == str(7):

        if b_6['text'] == '':
            if jogando == 'X':
                b_6['fg'] = cor
                b_6['text'] = 'X'
                tabela[2][0] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_6['fg'] = cor
                b_6['text'] = 'O' 
                tabela[2][0] = jogando
                jogando = 'X'

    if i == str(8):

        if b_7['text'] == '':
            if jogando == 'X':
                b_7['fg'] = cor
                b_7['text'] = 'X'
                tabela[2][1] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_7['fg'] = cor
                b_7['text'] = 'O' 
                tabela[2][1] = jogando
                jogando = 'X'

    if i == str(9):

        if b_8['text'] == '':
            if jogando == 'X':
                b_8['fg'] = cor
                b_8['text'] = 'X'
                tabela[2][2] = jogando  
                jogando = 'O'
            elif jogando == 'O':
                b_8['fg'] = cor
                b_8['text'] = 'O' 
                tabela[2][2] = jogando
                jogando = 'X'
    
    # acabar jogo na horizontal
    if tabela[0][0] == tabela[0][1] == tabela[0][2] != '':
        if tabela[0][0] == 'X':
            vencedor(jogador_1)
        if tabela[0][0] == 'O':
            vencedor(jogador_2)
            
    if tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
        if tabela[1][0] == 'X':
            vencedor(jogador_1)
        if tabela[1][0] == 'O':
            vencedor(jogador_2)
    if tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
        if tabela[2][0] == 'X':
            vencedor(jogador_1)
        if tabela[2][0] == 'O':
            vencedor(jogador_2)

    #acabar jogo na vertical
    if tabela[0][0] == tabela[1][0] == tabela[2][0] != '':
        if tabela[0][0] == 'X':
            vencedor(jogador_1)
        if tabela[0][0] == 'O':
            vencedor(jogador_2)
    if tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
        if tabela[0][1] == 'X':
            vencedor(jogador_1)
        if tabela[0][1] == 'O':
            vencedor(jogador_2)
    if tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
        if tabela[0][2] == 'X':
            vencedor(jogador_1)
        if tabela[0][2] == 'O':
            vencedor(jogador_2)

    #acabar o jogo na diagonal
    if tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
        if tabela[0][0] == 'X':
            vencedor(jogador_1)
        if tabela[0][0] == 'O':
            vencedor(jogador_2)
    if tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
        if tabela[0][2] == 'X':
            vencedor(jogador_1)
        if tabela[0][2] == 'O':
            vencedor(jogador_2) 

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

def restart():
    global tabela
    global board
    global jogando
    jogando = 'X'
    tabela = [[1,2,3],[4,5,6],[7,8,9]]
    board = [['','',''],['','',''],['','','']]
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

def bot_move():
    
    for i,linha in enumerate(tabela):
        for j, valor in enumerate(linha):
            if valor == 'X' or valor == 'O':

                board[i][j] = valor
    best_score = -80
    best_move = 0
    for i, linha in enumerate(board):
        for j, valor in enumerate(linha):
            if valor == '':
                board[i][j] = jogador_1
                score = minimax(board, False)
                board[i][j] = ''
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

def minimax(bo, ismax):
    if marcar_vencedor(jogador_1):
        return 1
    elif marcar_vencedor(jogador_2):
        return -1
    elif checar_empate():
        return 0

    if ismax:
        best_score = -80
        for i, linha in enumerate(bo):
            for j, valor in enumerate(linha):
                if valor == '':
                    board[i][j] = jogador_1
                    score = minimax(bo, False)
                    board[i][j] = ''
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = 80
        for i, linha in enumerate(bo):
            for j, valor in enumerate(linha):
                if valor == '':
                    board[i][j] = jogador_2
                    score = minimax(bo, True)
                    board[i][j] = ''
                    if score < best_score:
                        best_score = score
        return best_score
    
def checar_empate():
    for i,linha in enumerate(board):
        for j, valor in enumerate(linha):
            if valor == '':
                return False

    return True

def marcar_vencedor(mark):
        #horizontal
        if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == mark:
            return True
        elif (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == mark):
            return True
        elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == mark):
            return True
        #vertical
        elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == mark):
            return True
        elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == mark):
            return True
        elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == mark):
            return True
        #diagonal
        elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == mark):
            return True
        elif (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == mark):
            return True
        else:
            return False


# botões
b_0 = Button(frame, command= lambda: jogano('1'), text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_0.place(x=35, y=21)

b_1 = Button(frame, command= lambda: jogano('2'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_1.place(x=104, y=21)

b_2 = Button(frame, command= lambda: jogano('3'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_2.place(x=169, y=21)

b_3 = Button(frame, command= lambda: jogano('4'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_3.place(x=35, y=92)

b_4 = Button(frame, command= lambda: jogano('5'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_4.place(x=104, y=92)

b_5 = Button(frame, command= lambda: jogano('6'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_5.place(x=169, y=92)

b_6 = Button(frame, command= lambda: jogano('7'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_6.place(x=35, y=162)

b_7 = Button(frame, command= lambda: jogano('8'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_7.place(x=104, y=162)

b_8 = Button(frame, command= lambda: jogano('9'),text='', width=2,height=1, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co7 )
b_8.place(x=169, y=162)

b_9 = Button(frame, command= lambda: restart(),text='RESTART', width=7,height=0, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co5 )
b_9.place(x=7, y=215)

b_10 = Button(frame, command= lambda: jogano(bot_move()),text='BOT', width=7,height=0, relief='flat', padx=1, pady=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co5 )
b_10.place(x=160, y=215)






































janela.mainloop()