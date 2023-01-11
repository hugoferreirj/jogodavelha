import tkinter
from tkinter import *
from tkinter import ttk

#cores

branco = "#FFFFFF"
preto = "#333333"
laranja = "#fcc058"
azul = "#3297a8"
amarelo = "#fff873"
fundo = "#3b3b3b"
vermelho= "#e85151"

#criando janela principal
janela = Tk()   
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

# Dividindo a janela em 2 frames

frame_cima = Frame(janela, width=240, height=100, bg=preto, relief="raised")
frame_cima.grid(row=1, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=2, column=0, sticky=NW)


# Configurando o frame cima

app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=preto, fg=vermelho)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=preto, fg=branco)
app_x.place(x=17, y=70)
app_xp = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=preto, fg=branco)
app_xp.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=preto, fg=branco)
app_separador.place(x=110, y=20)

app_0 = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=preto, fg=azul)
app_0.place(x=170, y=10)
app_0 = Label(frame_cima, text='Jogador2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=preto, fg=branco)
app_0.place(x=165, y=70)
app_0p = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=preto, fg=branco)
app_0p.place(x=130, y=20)

# Criando Lógica

jogador1 = "X"
jogador2 = "O"

p1 = 0 # pontuações
p2 = 0 
jogando = jogador1
jogar = ''
contador = 0
contador_de_rodada = 0
tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def iniciar_jogo(): #controlar o jogo
    b_jogar.place(x=800, y=197)
    

    def controlar(i):
        global jogando
        global contador
        global jogar
        global tabela

        # comparando o valor recebido
        n = int(i)
        for j in range(1,10):
            if n==j:
                #verificando se aquela posicao esta vazia
                if b[n]['text']=='':
                    #verificar quem esta jogando e definindo o simbolo
                    if jogando == jogador1:
                        cor = vermelho
                    if jogando == jogador2:
                        cor = azul

                    #definindo a cor do texto do botao e marcar aquela posição da tabela com o valor atual
                    b[n]['fg'] = cor 
                    b[n]['text'] = jogando
                    if 0 < n < 4:
                        tabela[0][n-1] = jogando
                    elif 4 <= n < 7:
                        tabela[1][n-4] = jogando
                    elif 7 <= n < 10:
                        tabela[2][n-7] = jogando
                    #verificando quem está jogando para trocar de jogador
                    if jogando == jogador1:
                        jogando = jogador2
                        jogar = "Jogador 2"
                    elif jogando == jogador2:
                        jogando = jogador1
                        jogar = "Jogador 1"
                    break
        
        if  0 < n <10: 
            #incrementar o contador para a próxima rodada
            contador+=1
            #Apos o contador ser maior ou igual a 5, 
            # verifica se houve algum vencedor de acordo com os padroes
            
            if contador >= 5:
                #colunas 
                for j in range(0,3):
                    if tabela[0][j] == tabela[1][j] == tabela[2][j] != "":
                        vencedor(jogando)
                        break
                #linhas 
                for j in range(0,3):
                    if tabela[j][0] == tabela[j][1] == tabela[j][2] != "":
                        vencedor(jogando)
                        break
                
                #diagonais
                if tabela[0][0] == tabela[1][1] == tabela[2][2] != "" or tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                #Empate
                elif contador>=9:
                    vencedor('foi empate')

    
    def vencedor(j):
        global tabela
        global jogando
        global p1
        global p2
        global contador_de_rodada, contador

        for i in range(1,10):
            b[i]['text'] = ""
            b[i]['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='Vencedor', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=preto, fg=vermelho)
        app_vencedor.place(x=40, y=220)

        if j == 'foi empate':
            app_vencedor['text'] = 'Foi um empate'

        elif j == jogador1:
            p2+=1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_0p['text'] = str(p2)

        elif j == jogador2:
            p1+=1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_xp['text'] = str(p1)

        def start():
            global tabela
            app_vencedor.destroy()
            b_jogar.destroy()
            for i in range(1,10):
                b[i]['text'] = ""
                b[i]['state'] = 'normal'
            

        # botao jogar
        b_jogar = Button(frame_baixo, text='Proxima rodada', command=start, height=1, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=branco)
        b_jogar.place(x=80, y=197)

        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()
        
        if contador_de_rodada>=5:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0

    def terminar():
        global tabela
        global contador_de_rodada 
        global p1
        global p2, contador

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contador_de_rodada = 0
        p1 = 0
        p2 = 0
        contador = 0
        for i in range(1,10):
            b[i]['state'] = 'disable'
        
        app_fim = Label(frame_baixo, text='Jogo acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=preto, fg=vermelho)
        app_fim.place(x=25, y=90)

        def jogarNovamente():
            app_xp['text'] = '0'
            app_0p['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            iniciar_jogo()

        b_jogar = Button(frame_baixo, text='Jogar de novo', command=jogarNovamente, height=1, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=branco)
        b_jogar.place(x=85, y=197)
    # Configurando o frame baixo

    # linhas verticais
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=branco)
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=branco)
    app_.place(x=157, y=15)

    # linhas horizontais
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=branco)
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=branco)
    app_.place(x=30, y=127)

    b = []
    for _ in range(10):
        b.append(None)


    # linha 0
    b[1] = Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[1].place(x=30, y=15)

    b[2] = Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[2].place(x=96, y=15)

    b[3] = Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[3].place(x=163, y=15)

    # linha 1
    b[4] = Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[4].place(x=30, y=75)

    b[5] = Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[5].place(x=96, y=75)

    b[6] = Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[6].place(x=163, y=75)

    # linha 2
    b[7] = Button(frame_baixo,command=lambda:controlar('7'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[7].place(x=30, y=135)

    b[8] = Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[8].place(x=96, y=135)

    b[9] = Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, height=1, relief='flat', font=('Ivy 20 bold'), overrelief=RIDGE, bg=fundo)
    b[9].place(x=163, y=135)

    
b_jogar = Button(frame_baixo, text='Jogar', command=iniciar_jogo, width=10, height=1, relief='raised', font=('Ivy 10 bold'), overrelief=RIDGE, bg=fundo, fg=branco)
b_jogar.place(x=85, y=197)

janela.mainloop()