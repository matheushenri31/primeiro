from tkinter import *
from PIL import ImageTk, Image
from random import *

# Cores
rosa = '#cc29cc'
branco = '#f7f7f7'
preto = '#000000'
roxo = '#7121a3'
azul = '#3136cc'
vermelho = '#d13d5d'

# Configurações básicas da janela

janela = Tk()
janela.title('% de amor')
janela.iconphoto(False, PhotoImage(file='coracao_icone.png'))
janela.geometry('340x370')
janela.config(bg=branco)

# Criando os 2 frames

frame_cima = Frame(janela, width=340, height=65, relief='flat', padx=0, pady=0, bg=branco)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=340, height=305, relief='flat', padx=0, pady=0, bg=branco)
frame_baixo.grid(row=1, column=0)

# TRABALHANDO NO FRAME_ACIMA ---------------

# Criando Label para 'calculadora do amor'
nome_calculadora_amor = Label(frame_cima, text='Calculadora do amor',font='Fixedsys 22', fg=rosa, bg=branco)
nome_calculadora_amor.place(x=20, y=10)

# Label para barra ----------
barra_vermelha = Label(frame_cima, width=340, height=1, bg=vermelho, anchor=NW, pady=0, fg=vermelho)
barra_vermelha.place(x=0, y=50)

# TRABALHANDO NO FRAME_BAIXO --------------

# Criando imagens
img = Image.open('relacao.png')
img = img.resize((60, 60))
img = ImageTk.PhotoImage(img)

img_female = Image.open('female.png')
img_female = img_female.resize((50, 50))
img_female = ImageTk.PhotoImage(img_female)

img_masc = Image.open('male.png')
img_masc = img_masc.resize((50, 50))
img_masc = ImageTk.PhotoImage(img_masc)

img_wifi_amor = Image.open('wifi_amor.png')
img_wifi_amor = img_wifi_amor.resize((40, 40))
img_wifi_amor = ImageTk.PhotoImage(img_wifi_amor)

# Implementando as imagens
img_relacao = Label(frame_baixo, image=img, bg=branco)
img_relacao.place(x=135, y=0)

female = Label(frame_baixo, image=img_female, bg=branco)
female.place(x=240, y=80)

masc = Label(frame_baixo, image=img_masc, bg=branco)
masc.place(x=30, y=80)

wifi_amor = Label(frame_baixo, image=img_wifi_amor, bg=branco)
wifi_amor.place(x=270, y=170)

# Criando os Entry
entry_masc = Entry(frame_baixo, width=20, relief='raised')
entry_masc.place(x=10, y=150)

entry_fem = Entry(frame_baixo, width=20, relief='raised')
entry_fem.place(x=200, y=150)

barra_vertical_vermelha = Label(frame_baixo, width=1, height=2, bg=vermelho)
barra_vertical_vermelha.place(x=150, y=140)

barra_vertical_roxa = Label(frame_baixo, width=1, height=2, bg=roxo)
barra_vertical_roxa.place(x=170, y=140)

# Criando função para porcentagem
def pega_nomes():
    if botao_calcula_amor:
        global entry_fem
        global entry_masc
        nome_masc = entry_masc.get()
        nome_fem = entry_fem.get()
        label_nomes['text'] = f'{nome_masc}  &  {nome_fem}'.title()

        a = randint(0, 100)
        lb_porcentagem['text'] = f'%  {a}'

# Criando botão para calcular a % de amor
botao_calcula_amor = Button(frame_baixo, command=pega_nomes, text='Calcule aqui', font='arial 10 bold', width=10, height=2, relief='ridge', overrelief='raised', bg=roxo, fg=branco)
botao_calcula_amor.place(x=125, y=80)

texto_porcentagem = Label(frame_baixo, text='A porcentagem de amor entre', font='Times 12 bold', bg=branco, fg=vermelho)
texto_porcentagem.place(x=65, y=198)

# Label onde aparecerá os nomes
label_nomes = Label(frame_baixo, text=' . . .  ', width=30, height=1, bg=branco, fg=vermelho, font='times 12 bold')
label_nomes.place(x=30, y=220)

# Criando label onde aparecerá porcentagem
lb_porcentagem = Label(frame_baixo, text='%      ?', width=15, height=2, relief='raised', bg=branco, font='times 10 bold')
lb_porcentagem.place(x=115, y=260)

# criando linhas horizontais
linha_horizontal_vermelha = Label(frame_baixo, width=15, height=1, bg=azul)
linha_horizontal_vermelha.place(x=0, y=267)

linha_horizontal_roxa = Label(frame_baixo, width=15, height=1, bg=rosa)
linha_horizontal_roxa.place(x=230, y=267)

janela.mainloop()

