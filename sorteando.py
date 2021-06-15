import random
from tkinter import *
import tkinter as tk
import time
import os
import tkinter.messagebox as tkMessageBox


def sortenado():
    cont=0
    numini= int(Txtini.get())
    numfim=int(Txtfim.get())
    qtd=int(Txtqtd.get())
    textganha=""
    regres=numfim
    #cria uma lista depois sorteia com sample sem duplicidade
    opcoes = list(range(numini,numfim+1))
    ganhador=random.sample(opcoes,qtd)
    
    #for para separar a lista de sorteados
    for x in ganhador:
        cont=cont+1
        #Lblqtdganhador.config(text='Para '+str(qtd)+' número(s) sorteado(s)')
        textganha = str(textganha) +"\n"+ str(cont)+"º Ganhador"+" = " + str(x)
        Lblganhador.config(text='Número(s) da sorte: ' + str(textganha))
    Lblganhador.place(relx=0.2, rely = 0.55)
    #Lblqtdganhador.place(relx=0.1, rely = 0.5)
    botao['state'] = tk.NORMAL  

'''def contando():
    sec = int(Txtfim.get())
    while sec > 0:
        sec = sec - 1
        Lblqtdganhador['text'] = sec
        Lblqtdganhador.after(1000)
        print(sec)
    sortenado()'''

#contagem regressiva para ficar legal
def contando(validador = False,sec = None, pulando=1):
    try:
        botao['state'] = tk.DISABLED
        if validador == False:
            Lblganhador.config(text='')
            #Lblqtdganhador['text'] = ''
            Lblregressiva.place(relx=0.1, rely = 0.7)
            sec = int(Txtfim.get())
            if sec > 100:
                pulando = 25
            elif sec > 10:
                pulando = 5
            else:
                pulando = 1  
        if sec <= 1:
            Lblregressiva['text'] = ''
            Lblregressiva.place(relx=100, rely = 0.7)
            sortenado()
        else:
            sec = sec - pulando
            Lblganhador.place(relx=110, rely = 0.55)
            Lblregressiva['text'] = sec
            Lblregressiva['bg'] = 'DarkGoldenrod'
            Lblregressiva.after(200, lambda : contando(True,sec,pulando))  
             
    except:
        tkMessageBox.showinfo("Valor inválido!", message= "Favor verificar os campos com * ")
        botao['state'] = tk.NORMAL


def sair():
    os._exit(1)

tinicial = tk.Tk()
tinicial.geometry("500x600+600+100")
#w,h = tinicial.winfo_screenwidth(),tinicial.winfo_screenheight()
#tinicial.geometry("%dx%d+0+0" % (w, h))
tinicial.title("Tela de Sorteios - ...")
tinicial.resizable(width=False, height=False)
tinicial.config(bg='skyBlue')
tinicial.iconphoto(True, PhotoImage(file='./arquivos/trevopico.png'))
image=PhotoImage(file='./arquivos/trevopico.png')

Lbltela = tk.Label(tinicial,image=image,bg='skyBlue',)
Lbltela.place(relx=0.0, rely = 0.0)

Lbltitulo = tk.Label(tinicial,bg='skyBlue',text='Realize seu Sorteio',fg='black',font=('arial',20,'bold'))
Lbltitulo.place(relx=0.2, rely = 0.01)

Lblini = tk.Label(tinicial,text='Escolha o inicio* ',justify='center',bg='skyBlue',fg='black',font=('arial',14,'bold'))
Lblini.place(relx=0.05, rely = 0.10)
Txtini=tk.Entry(tinicial,width=6,justify='center',font=('arial',14,'bold'))
Txtini.place(relx=0.8, rely = 0.10)
Lblfim = tk.Label(tinicial,text='Escolha o fim* ',bg='skyBlue',fg='black',font=('arial',14,'bold'))
Lblfim.place(relx=0.05, rely = 0.19)
Txtfim=tk.Entry(tinicial,width=6,justify='center',font=('arial',14,'bold'))
Txtfim.place(relx=0.8, rely = 0.19)
Lblqtd = tk.Label(tinicial,text='Escolha a quantidade de sorteios* ',bg='skyBlue',fg='black',font=('arial',14,'bold'))
Lblqtd.place(relx=0.05, rely = 0.28)
Txtqtd=tk.Entry(tinicial,width=6,justify='center',font=('arial',14,'bold'))
Txtqtd.place(relx=0.8, rely = 0.28)

botao = tk.Button(tinicial,width=6,bg='skyBlue', text="Sortear", fg='black',font=('arial',14,'bold'),command=contando)
botao.place(relx=0.2, rely = 0.4)

botaosair = tk.Button(tinicial,width=6,bg='skyBlue', text="Sair", fg='black',font=('arial',14,'bold'),command=sair)
botaosair.place(relx=0.5, rely = 0.4)

#Lblqtdganhador = tk.Label(tinicial,bg='skyBlue',fg='black',font=('arial',14,'bold'))

Lblganhador = tk.Label(tinicial,bg='GreenYellow',fg='black',font=('arial',14,'bold'))


Lblregressiva = tk.Label(tinicial,width=6,bg='skyBlue',fg='black',font=('arial',60,'bold'))



tinicial.mainloop()
