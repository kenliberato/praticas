from tkinter import *

quadro = Tk ()

quadro.title('Calculadora de IMC')
quadro.geometry('650x150')
quadro.configure(bg='light blue')

peso = Label(quadro, text='Peso (Kg):', bg='light blue')
altura = Label(quadro, text='Altura (m):', bg='light blue')
resultado = Label(quadro, text='Resultado:', bg='light blue')

peso.grid(row=0, column=0, padx=10, pady=10)
altura.grid(row=1, column=0, padx=10, pady=10)
resultado.grid(row=0, column=2, padx=10, pady=10)

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
    exibir.grid(row=0, column=3, padx=10, pady=10)
    if imc < 18.5:
        descricao_1 = Label(quadro, text='Magreza: seu IMC é menor que 18.5')
        descricao_1.grid(row=1, column=2, padx=10, pady=10)
    elif 18.5 <= imc <= 24.9:
        descricao_2 = Label(quadro, text='Normal: seu IMC está entre 18.5 e 24.9')
        descricao_2.grid(row=1, column=2, padx=10, pady=10)
    elif 25.0 <= imc <= 29.9:
        descricao_3 = Label(quadro, text='Sobrepeso, Obesidade Grau I: seu IMC está entre 25.0 e 29.9')
        descricao_3.grid(row=1, column=2, padx=10, pady=10)
    elif 30.0 <= imc <= 39.9: 
        descricao_4 = Label(quadro, text='Obesidade Grau II: seu IMC está entre 30.0 e 39.9')
        descricao_4.grid(row=1, column=2, padx=10, pady=10)
    elif imc > 40.0: 
        descricao_5 = Label(quadro, text='Obesidade Grave Grau III: seu IMC está maior que 40.0')
        descricao_5.grid(row=1, column=2, padx=10, pady=10)

botao_imc = Button(quadro, text='Calcular IMC', command=f_principal)
botao_imc.grid(row=2, column=1, padx=10, pady=10)

quadro.mainloop()