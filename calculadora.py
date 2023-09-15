#CRIANDO UMA CALCULADORA TKINTER
from tkinter import *

#FUNÇÕES
def limpar() -> None:
    #DELETANDO TUDO O QUE TIVER NO DISPLAY - FAZENDO O BOTAO C FUNCIONAR - JÁ COLOQUEI O COMAND LÁ EMBAIXO NO BOTAO
    display.delete(0, END)

def inserir(valor: str) -> None:
    display.insert(END, valor)

def calcular() -> None:
    #PEGANDO O VALOR DO DIS´PLAY
    valor_display = display.get()
    #CALCULANDO O RESULTADO COM A FUNÇÃO EVAL
    #PASSANDO O VALOR DO DISPLAY
    resultado = eval(valor_display)
    limpar()
    #INSERINDO O RESULTADO NO DISPLAY
    display.insert(END, str(resultado))

janela = Tk()
janela.title("Calculadora")

#CRIANDO O DISPLAY/ENTRY
display = Entry(janela, font="Arial 20 bold", fg="white", bg="pink", width=19)
display.pack()

#CRIANDO O FRAME
frame = Frame(janela)
#BOTÕES

btn_0 = Button(frame, text="0", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("0"))
btn_1 = Button(frame, text="1", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("1"))
btn_2 = Button(frame, text="2", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("2"))
btn_3 = Button(frame, text="3", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("3"))
btn_4 = Button(frame, text="4", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("4"))
btn_5 = Button(frame, text="5", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("5"))
btn_6 = Button(frame, text="6", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("6"))
btn_7 = Button(frame, text="7", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("7"))
btn_8 = Button(frame, text="8", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("8"))
btn_9 = Button(frame, text="9", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("9"))
btn_limpar = Button(frame, text="C", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=limpar)
btn_igual = Button(frame, text="=", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=calcular)
btn_somar = Button(frame, text="+", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("+"))
btn_sub = Button(frame, text="-", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("-"))
btn_div = Button(frame, text="/", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("/"))
btn_mult = Button(frame, text="*", bg="gray", font="Arial 16 bold", fg="#ffb6c1", height=3, width=5, command=lambda: inserir("*"))

frame.pack()
#PRIMEIRA LINHA
btn_7.grid(row=0, column=0)
btn_8.grid(row=0, column=1)
btn_9.grid(row=0, column=2)
btn_mult.grid(row=0, column=3)

#SEGUNDA LINHA
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

#TERCCEIRA LINHA
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_somar.grid(row=2, column=3)

#QUARTA LINHA
btn_limpar.grid(row=3, column=0)
btn_igual.grid(row=3, column=1)
btn_0.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

janela.mainloop()