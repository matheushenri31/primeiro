from tkinter import *
import time

# Cores
cor1 = '#000000'  #Preta
cor2 = '#cc21c9'   #Rosa mais forte
cor3 = '#ba41b8'   #Rosa intermediario
cor4 = '#c46ec3'  #Rosa mais fraco
cor5 = '#ffffff'  #Branca


janela = Tk()
janela.title('Horário')
janela.geometry('350x180')
janela.config(bg=cor1)
janela.iconphoto(False,PhotoImage(file='relogio.png'))
janela.resizable(width=False, height=False)

def horas():
    hora = time.strftime('%H')
    minuto = time.strftime('%M')
    segundo = time.strftime('%S')
    lb_horas['text'] = f'{hora}:{minuto}:{segundo}'
    lb_horas.after(1000, horas)


# Criando labels
lb_titulo = Label(janela, width=15, height=1, text='Horário de Brasília', font='Arial 20', bg=cor1, fg=cor5)
lb_titulo.place(x=50, y=20)

bt_horas = Button(janela, command=horas, text='Clique aqui para ver as horas', width=25, relief='raised', overrelief='ridge', bg=cor1, fg=cor5, font='Arial 13')
bt_horas.place(x=50, y=100)

lb_horas = Label(janela, text='', font='Times 50', bg=cor1, fg=cor3)
lb_horas.place(x=50, y=70)

janela.mainloop()
