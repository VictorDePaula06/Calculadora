import tkinter
from tkinter import *


root = Tk()
root.title('Calculadora do Vascão')
root.geometry('570x600+100+200')
root.resizable(False,False)
root.configure(bg='#17161b')

operacao = ''

def mostrar(valor):
    global operacao
    operacao += valor
    label_resultado.config(text=operacao)

def limpar():
    global operacao
    operacao = ''
    label_resultado.config(text=operacao)

def calcular():
    global operacao
    resultado = ''
    if operacao != '':
        try:
            resultado = eval(operacao)
        except:
            resultado ='ERROR'
            operacao = ''
    label_resultado.config(text=resultado)




label_resultado = Label(root, width=25, height=2,bg='#17161b', text=' ', font=('arial',30), fg='#fff')
label_resultado.pack()

# 1° FILEIRA

Button(root, text='C', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: limpar()).place(x=10, y=100)
Button(root, text='/', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('/')).place(x=150, y=100)
Button(root, text='%', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('%')).place(x=290, y=100)
Button(root, text='*', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#000', bg='#FFFFFF', command=lambda: mostrar('*')).place(x=430, y=100)

# 2° FILEIRA

Button(root, text='7', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('7')).place(x=10, y=200)
Button(root, text='8', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('8')).place(x=150, y=200)
Button(root, text='9', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#000', bg='#FF0000', command=lambda: mostrar('9')).place(x=290, y=200)
Button(root, text='-', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('-')).place(x=430, y=200)

# 3° FILEIRA

Button(root, text='4', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('4')).place(x=10, y=300)
Button(root, text='5', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#000', bg='#FFFFFF', command=lambda: mostrar('5')).place(x=150, y=300)
Button(root, text='6', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('6')).place(x=290, y=300)
Button(root, text='+', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('+')).place(x=430, y=300)

# 4° FILEIRA

Button(root, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#000', bg='#FFFFFF', command=lambda: mostrar('1')).place(x=10, y=400)
Button(root, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('2')).place(x=150, y=400)
Button(root, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('3')).place(x=290, y=400)
Button(root, text='0', width=11, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('0')).place(x=10, y=500)

Button(root, text='.', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: mostrar('.')).place(x=290, y=500)
Button(root, text='=', width=5, height=3, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#000000', command=lambda: calcular()).place(x=430, y=400)




root.mainloop()

