from tkinter import * #importando o necessário para criar a calculadora

root = Tk() #tela principal

#Criando a tela
root.title("💻🧮Calculadora do Akise🧮💻")
root.geometry('300x300')
root.config(bg="#0f0f0f")
root.maxsize(width=300, height=300)
root.minsize(width=200, height=200)

#Loop do grid para delimitar colunas e linhas
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

#Mensagem do desenvolvedor Variável
akise = 'O impossível é apenas uma possibilidade!'

#Variáveis necessárias para rotar a lógica da calculadora
numero1 = ''
divisao = FALSE
multiplicacao = FALSE
subtrair = FALSE
somar = FALSE
potencia = FALSE
numero2 = ''

#Funções das teclas
def botao_click(num):
    tela.insert(END, num)

def botao_click_Akise():
    global b_personalizado
    b_personalizado = True
    if b_personalizado == True:
        tela.delete(0, END)
        tela.insert(END, akise)

def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = tela.get()
    tela.delete(0, END)

def botao_multiplicar():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = tela.get()
    tela.delete(0, END)

def botao_subtrair():
    global numero1
    global subtrair
    subtrair = TRUE
    numero1 = tela.get()
    tela.delete(0, END)

def botao_somar():
    global numero1
    global somar
    somar = TRUE
    numero1 = tela.get()
    tela.delete(0, END)

def botao_potencia():
    global numero1
    global potencia
    potencia = TRUE
    numero1 = tela.get()
    tela.delete(0, END)

def botao_igual():
    global divisao
    global multiplicacao
    global subtrair
    global somar
    global potencia
    numero2 = tela.get()
    tela.delete(0, END)
    if somar == TRUE:
        tela.insert(0, float(numero1) + float(numero2))
        somar = FALSE
    if subtrair == TRUE:
        tela.insert(0, float(numero1) - float(numero2))
        somar = FALSE
    if multiplicacao == TRUE:
        tela.insert(0, float(numero1) * float(numero2))
        multiplicacao = FALSE
    if divisao == TRUE:
        tela.insert(0, float(numero1) / float(numero2))
        divisao = FALSE
    if potencia == TRUE:
        tela.insert(0, float(numero1) ** float(numero2))
        potencia = FALSE
def botao_limpar():
    tela.delete(0, END)
        

#Dividindo a tela em corpo e display
tela_display = Frame(root, width=300, height=50, bg="#e4d7f5")
tela_display.grid(row=0, column=0)
tela = Entry(root, width=20, borderwidth=5, relief=RAISED, fg="#151518", bg="#cac5f7", font=('Arial', 25, 'bold'), justify=CENTER)
tela.grid(row=0, column=0, columnspan=6)

tela_corpo = Frame(root, width=300, height=250, bg="#0e0b14")
tela_corpo.grid(row=1, column=0)

#Criação dos botões
b_clear = Button(tela_corpo, text='⌫', width=19, height=2, command=botao_limpar)
b_clear.grid(row=0, column=0, columnspan=2)

b_potencia = Button(tela_corpo, text='1¹', width=9, height=2, command=botao_potencia)
b_potencia.grid(row=0, column=2)

b_divisao = Button(tela_corpo, text='÷', width=9, height=2, command= botao_divisao)
b_divisao.grid(row=0, column=3)

b_7 = Button(tela_corpo, text='7', width=9, height=2, command=lambda: botao_click(7))
b_7.grid(row=1, column=0)

b_8 = Button(tela_corpo, text='8', width=9, height=2, command=lambda: botao_click(8))
b_8.grid(row=1, column=1)

b_9 = Button(tela_corpo, text='9', width=9, height=2, command=lambda: botao_click(9))
b_9.grid(row=1, column=2)

b_multiplicar = Button(tela_corpo, text='x', width=9, height=2, command= botao_multiplicar)
b_multiplicar.grid(row=1, column=3)

b_4 = Button(tela_corpo, text='4', width=9, height=2, command=lambda: botao_click(4))
b_4.grid(row=2, column=0)

b_5 = Button(tela_corpo, text='5', width=9, height=2, command=lambda: botao_click(5))
b_5.grid(row=2, column=1)

b_6 = Button(tela_corpo, text='6', width=9, height=2, command=lambda: botao_click(6))
b_6.grid(row=2, column=2)

b_subtrair = Button(tela_corpo, text='-', width=9, height=2, command=botao_subtrair)
b_subtrair.grid(row=2, column=3)

b_1 = Button(tela_corpo, text='1', width=9, height=2, command=lambda: botao_click(1))
b_1.grid(row=3, column=0)

b_2 = Button(tela_corpo, text='2', width=9, height=2, command=lambda: botao_click(2))
b_2.grid(row=3, column=1)

b_3 = Button(tela_corpo, text='3', width=9, height=2, command=lambda: botao_click(3))
b_3.grid(row=3, column=2)

b_somar = Button(tela_corpo, text='+', width=9, height=2, command=botao_somar)
b_somar.grid(row=3, column=3)

b_0 = Button(tela_corpo, text='0', width=9, height=2, command=lambda: botao_click(0))
b_0.grid(row=4, column=0)

b_igual = Button(tela_corpo, text='=', width=9, height=2, command=botao_igual)
b_igual.grid(row=4, column=3)

b_personalizado = Button(tela_corpo, text='Akise', width=19, height=2, command= botao_click_Akise)
b_personalizado.grid(row=4, column=1, columnspan=2)


root.mainloop() #loop que mantém a aplicação aberta.
