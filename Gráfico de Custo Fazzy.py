from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from tkinter import messagebox


estilo = {"bg":"#000080",'bg_part1':"#2510a3"}
win = Tk()
win.iconbitmap('img\Ico.ico')
win.title("Lano: Gerar Gráfico de Custo Fazzy")
win.geometry("1000x550")
win["bg"] = estilo["bg"]

#frame_titulo
frame_titulo = Frame(win)
frame_titulo["bg"] = estilo["bg"]
frame_titulo.pack()

titulo = Label(frame_titulo, text="GRÁFICO DE CUSTO FAZZY",font="Calibri 45 bold",fg="white")

titulo["bg"] = estilo["bg"]
titulo.pack()

#Frame_Parte_1 (Crisp, gerar, text,salvar)
frame_parte1 = Frame(win)
frame_parte1["bg"] = estilo["bg"]
frame_parte1.pack()

text_crisp = Label(frame_parte1, text="Crisp:",font="Calibri 20 bold",fg="white")
text_crisp["bg"] = estilo["bg"]
text_crisp.pack(side="left")

input_crisp = Text(frame_parte1,height=1,width=10,border=0,font="Arial 15")
input_crisp.pack(side="left",padx=20)

nome_gra = Label(frame_parte1, text="Nome do Gráfico:",font="Calibri 20 bold",fg="white")
nome_gra["bg"] = estilo["bg"]
nome_gra.pack(side="left")

nome_grafico = Text(frame_parte1,height=1,width=28,border=0,font="Arial 15 bold")
nome_grafico.pack(side="left",padx=20)

#div_parte_2
frame_parte2 = Frame(win)
frame_parte2["bg"] = estilo["bg_part1"]
frame_parte2.pack(fill=BOTH,pady=10)

#frame_AS
frame_As = Frame(frame_parte2)
frame_As["bg"] = estilo["bg_part1"]
frame_As.pack()

#FrameAi
frame_Ai = Frame(frame_parte2)
frame_Ai["bg"] = estilo["bg_part1"]
frame_Ai.pack()

As1_img = PhotoImage(file=r"img\As\As1.png").subsample(5,5) 
As1_text = Label(frame_As, image = As1_img) 
As1_text["bg"] = estilo["bg_part1"]
As1_text.pack(side="left")

As1 = Text(frame_As,height=1,width=10)
As1.pack(side="left")

Ai1_img = PhotoImage(file=r"img\Ai\Ai1.png").subsample(5,5) 
Ai1_text = Label(frame_As, image = Ai1_img) 
Ai1_text["bg"] = estilo["bg_part1"]
Ai1_text.pack(side="left")

Ai1 = Text(frame_As,height=1,width=10)
Ai1.pack(side="left")

As2_img = PhotoImage(file=r"img\As\As2.png").subsample(5,5) 
As2_text = Label(frame_As, image = As2_img) 
As2_text["bg"] = estilo["bg_part1"]
As2_text.pack(side="left")

As2 = Text(frame_As,height=1,width=10)
As2.pack(side="left")

Ai2_img = PhotoImage(file=r"img\Ai\Ai2.png").subsample(5,5) 
Ai2_text = Label(frame_As, image = Ai2_img) 
Ai2_text["bg"] = estilo["bg_part1"]
Ai2_text.pack(side="left")

Ai2 = Text(frame_As,height=1,width=10)
Ai2.pack(side="left")

#PARTE DE BAIXO

Ai3_img = PhotoImage(file=r"img\Ai\Ai3.png").subsample(5,5) 
Ai3_text = Label(frame_Ai, image = Ai3_img) 
Ai3_text["bg"] = estilo["bg_part1"]
Ai3_text.pack(side="left")

Ai3 = Text(frame_Ai,height=1,width=10)
Ai3.pack(side="left")

As3_img = PhotoImage(file=r"img\As\As3.png").subsample(5,5) 
As3_text = Label(frame_Ai, image = As3_img) 
As3_text["bg"] = estilo["bg_part1"]
As3_text.pack(side="left")

As3 = Text(frame_Ai,height=1,width=10)
As3.pack(side="left")

Ai4_img = PhotoImage(file=r"img\Ai\Ai4.png").subsample(5,5) 
Ai4_text = Label(frame_Ai, image = Ai4_img) 
Ai4_text["bg"] = estilo["bg_part1"]
Ai4_text.pack(side="left")

Ai4 = Text(frame_Ai,height=1,width=10)
Ai4.pack(side="left")

As4_img = PhotoImage(file=r"img\As\As4.png").subsample(5,5) 
As4_text = Label(frame_Ai, image = As4_img) 
As4_text["bg"] = estilo["bg_part1"]
As4_text.pack(side="left")

As4 = Text(frame_Ai,height=1,width=10)
As4.pack(side="left")

#Divisões dos valores de entrada PARTE DE CIMA
#div_parte_3
frame_parte3 = Frame(win)
frame_parte3["bg"] = estilo["bg"]
frame_parte3.pack()

#frame_logo
frame_logo = Frame(frame_parte3)
frame_logo["bg"] = estilo["bg"]
frame_logo.pack(side="left")

logo = PhotoImage(file=r"img\logo.png").subsample(2,2) 
logo_exi = Label(frame_logo, image = logo) 
logo_exi["bg"] = estilo["bg"]
logo_exi.pack(side="left")

frame_texto = Frame(frame_parte3)
frame_texto.pack()

texto_expli = """




DESENVOLVEDORES
Docente: Dr. Marcus Pinto da Costa da Rocha
Discentes: Gustavo Tocantins e Kadu Naoki"""
explic = Label(frame_logo,text=texto_expli,font="arial 9 bold",fg="white")
explic["bg"] = estilo["bg"]
explic.pack()

#frame_grafico
frame_grafico = Frame(frame_parte3)
frame_grafico["bg"] = estilo["bg"]
frame_grafico.pack()

#Gráfico de Exemplo


def criar_grafico():
    try:
        crisp = float(input_crisp.get("1.0","end")) #float(input("Valor de Crisp: "))
        #Dados de Entrada
        As_1 = float(As1.get("1.0","end").strip()) #200.38#float(input("A(s1): "))
        As_2 = float(As2.get("1.0","end").strip()) ##float(input("A(s2): "))
        As_3 = float(As3.get("1.0","end").strip())  ##float(input("A(s3): "))
        As_4 = float(As4.get("1.0","end").strip()) ##float(input("A(s4): "))

        As_x = [As_1,As_2,As_3,As_4]
        ws = [0,1,1,0]

        print("\nTRAPÉZIO INFERIOR")
        #Inferior 
        Ai_1 = float(Ai1.get("1.0","end").strip())##float(input("A(i1): "))
        Ai_2 = float(Ai2.get("1.0","end").strip())##float(input("A(i2): "))
        Ai_3 = float(Ai3.get("1.0","end").strip())##float(input("A(i3): "))
        Ai_4 = float(Ai4.get("1.0","end").strip())##float(input("A(i4): "))
    except:
        messagebox.showerror("Erro", f"Os dados de entrada estão incorretos")
    Ai_x = [Ai_1,Ai_2,Ai_3,Ai_4]
    wi = [0,0.67,0.67,0]

    plt.figure(figsize=(12,6))
    #Pontos no Gráfico
    plt.plot(As_x[0],0,"o", label=f"A1(s): {As_x[0]}", color="black")
    plt.plot(Ai_x[0],0,"o", label=f"A1(i): {Ai_x[0]}",color="black")
    plt.plot(As_x[1],1,"o", label=f"A2(s): {As_x[1]}",color="black")
    plt.plot(Ai_x[1],0.67,"o", label=f"A2(i): {Ai_x[1]}",color="black")
    plt.plot(Ai_x[2],0.67,"o", label=f"A3(i): {Ai_x[2]}",color="black")
    plt.plot(As_x[2],1,"o", label=f"A3(s): {As_x[2]}",color="black")
    plt.plot(Ai_x[3],0,"o", label=f"A4(i): {Ai_x[3]}",color="black")
    plt.plot(As_x[3],0,"o", label=f"A4(s): {As_x[3]}",color="black")


    #Nomes dos pontos no gráfico
    plt.text(As_x[0]+0.5,0,"A1(s)")
    plt.text(As_x[1],1.05,"A2(s)",{'ha': 'center', 'va': 'center'})
    plt.text(As_x[2],1.05,"A3(s)",{'ha': 'center', 'va': 'center'})
    plt.text(As_x[3]+0.5,0,"A4(s)")
    plt.text(Ai_x[0]+0.5,0,"A1(i)")
    plt.text(Ai_x[1],0.71,"A2(i)",{'ha': 'center', 'va': 'center'})
    plt.text(Ai_x[2],0.71,"A3(i)",{'ha': 'center', 'va': 'center'})
    plt.text(Ai_x[3]+0.5,0,"A4(i)")

    #Adicionar Legenda
    plt.legend(fancybox=True,title="Valores de A superior")

    #Linhas para ligar os pontos
    plt.hlines(y=1, xmin=As_x[0], xmax=As_x[1], linestyle=":", color="black")
    plt.vlines(x=As_x[1], ymin=0, ymax=1, linestyle=":",color="black")
    plt.vlines(x=As_x[2], ymin=0, ymax=1, linestyle=":",color="black")

    plt.hlines(y=0.67, xmin=As_x[0], xmax=Ai_x[1], linestyle=":",color="black")
    plt.vlines(x=Ai_x[1], ymin=0, ymax=0.67, linestyle=":",color="black")
    plt.vlines(x=Ai_x[2], ymin=0, ymax=0.67, linestyle=":",color="black")

    #Exibir Superior
    plt.plot(As_x,ws) 

    #Exibir inferior
    plt.plot(Ai_x,wi) #Exibir a linha da equação

    plt.vlines(x=crisp, ymin=0, ymax=1, linestyle="--",color="black")


    plt.yticks([0,0.67,1,1.4],[0,0.67,1,""])
    x_s = [As_1,As_2,As_3,As_4,Ai_1,Ai_2,Ai_3,Ai_4]
    valor = ["","","","","","","",""] #["A1(s)","A2(s)","A3(s)","A4(s)","A1(i)","A2(i)","A3(i)","A4(i)"]
    alinhar = {'ha': 'center', 'va': 'center','bbox':{'fc': '1', 'pad': 4}}

    plt.text((As_1+Ai_2)/2,1.2,"Sistemático", alinhar)
    plt.text(crisp,1.2,"Decisivo",alinhar)
    plt.text((Ai_3+As_4)/2,1.2,"Flexível",alinhar)

    plt.xticks(x_s,valor)

    plt.xlabel('Custo de Frete')
    plt.ylabel('Grau de Pertinência')
    plt.legend(loc='best')
    plt.title(nome_grafico.get("1.0","end"),fontdict={'family': 'Calibri', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 25})
    plt.show()

gerar = Button(frame_parte1, text="Gerar", bg="orange",font="arial 12 bold",fg="white",border=0,height=1,width=14,command=criar_grafico)
gerar.pack(side="left",padx=20)


win.mainloop()
