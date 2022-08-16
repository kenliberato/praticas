from tkinter import *
quadro = Tk ()

quadro.title('Calculadora de IMC')
quadro.geometry('350x150')

peso = Label(quadro, text='Peso (Kg):')
altura = Label(quadro, text='Altura (m):')
resultado = Label(quadro, text='Resultado:')

peso.grid(row=0, column=0, padx=10, pady=10)
altura.grid(row=1, column=0, padx=10, pady=10)
resultado.grid(row=2, column=2, padx=5, pady=5)

entrada_peso = Entry(quadro, width=20)
entrada_altura = Entry(quadro, width=20)

entrada_peso.grid(row=0, column=1, padx=10, pady=10)
entrada_altura.grid(row=1, column=1, padx=10, pady=10)

def f_principal ():
    texto1 = entrada_peso.get()
    num1 = float(texto1)
    texto2 = entrada_altura.get()
    num2 = float(texto2)
    imc = float(round(num1/(num2**2), 1))
    exibir = Label(quadro, text=imc)  
    exibir.grid(row=2, column=3, padx=10, pady=10)

botao_imc = Button(quadro, text='Calcular IMC', command=f_principal)
botao_imc.grid(row=2, column=1, padx=10, pady=10)

quadro.mainloop()