from tkinter import *

# Cores
cor1 = '#28419e'  # Azul Facebook
cor2 = '#e0e0e0'  # Cinza quase branco
cor3 = '#000000'  # Preta
cor4 = '#c7c7c7'  # Cinza

janela = Tk()
janela.geometry('400x400')
janela.title('Facebook')
janela.iconphoto(False,PhotoImage(file='icone_facebook.png'))
janela.resizable(width=False, height=False)

# Pegando imagens
ovelha = PhotoImage(file='ovelha_facebook.png')
user = PhotoImage(file='user_facebook.png')

lb_frame_cima = LabelFrame(janela, width=400, height=100, bg=cor4, relief='flat')
lb_frame_cima.grid(row=0, column=0)

lb_frame_baixo = LabelFrame(janela, width=400, height=300, bg=cor2, relief='flat')
lb_frame_baixo.grid(row=1, column=0)

facebook = Label(lb_frame_cima, text='Facebook', width=400, padx=5, relief='flat', anchor=NW, font='George 55 bold', fg=cor1, bg=cor4)
facebook.place(x=10, y=5)

cadastro = Label(lb_frame_baixo, text='Cadastro: ', font='arial 12 ', anchor=NW, bg=cor2, fg=cor1)
cadastro.place(x=10, y=12)

nome = Label(lb_frame_baixo, text='Nome: ', font='arial 12', bg=cor2, fg=cor1)
nome.place(x=10, y=50)

entry_nome = Entry(lb_frame_baixo, width=20)
entry_nome.place(x=70, y=50)

email = Label(lb_frame_baixo, text='e-mail: ', font='Arial 12', bg=cor2, fg=cor1)
email.place(x=10, y=90)

entry_email = Entry(lb_frame_baixo, width=25)
entry_email.place(x=70, y=90)

senha = Label(lb_frame_baixo, text='Senha: ', font='Arial 12', bg=cor2, fg=cor1)
senha.place(x=10, y=130)

entry_senha = Entry(lb_frame_baixo, width=20)
entry_senha.place(x=70, y=130)

sexo = Label(lb_frame_baixo, text='Seu sexo: ', font='Arial 12', bg=cor2, fg=cor1)
sexo.place(x=10, y=165)

identificao_sexo = StringVar()

opcao_masc = Radiobutton(lb_frame_baixo, text='Masculino', variable=identificao_sexo, value='Masculino')
opcao_masc.place(x=10, y=200)

opcao_femin = Radiobutton(lb_frame_baixo, text='Feminino', value='Feminino', variable=identificao_sexo)
opcao_femin.place(x=10, y=235)

opcao_masc.select()

lb_ovelha = Label(lb_frame_baixo, image=ovelha, bg=cor2)
lb_ovelha.place(x=110, y=200)

lb_user = Label(lb_frame_baixo, image=user, bg=cor2)
lb_user.place(x=270, y=20)


janela.mainloop()