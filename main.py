from tkinter import *
"""

#Informar um número
print('Digite um número: ')
num1 = float(input(''))
#Informar o operador
print('Informe a operação válida (+ - * /): ')
operador = input('')
#Informar outro número
print('Digite um número: ')
num2 = float(input(''))
#Calculo desejado
if operador == '+':
    soma = num1 + num2
    print(f'resultado: {soma}')

elif operador == '-':
    sub = num1 - num2
    print(f'resultado: {sub}')

elif operador == '*':
    mult = num1 * num2
    print(f'resultado: {mult}')

elif operador == '/':
    div = num1 / num2
    print(f'resultado: {div}')

else:
    print('Operador invalido! Por favor, digitar um operador correto.')
"""

#parte gráfica

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Tela Teste")
        self.root.configure(background= '#C8A2C8')
        self.root.geometry('750x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 720, height= 720)
        self.root.minsize(width= 400 ,height= 300)

Application()