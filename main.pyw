# Calculadora (Práctica con TKinter)
# Emmanuel Campos 2022-1855

from tkinter import *
from tkinter import ttk # Módulo de TKinter que proporciona widgets con aspecto más "moderno".
from tkinter import messagebox # Módulo de TKinter que permite mostrar ventanas con mensajes de error para manejar errores

# Permite inicializar la ventana principal del programa
root = Tk()
root.title("Calculadora")
root.iconbitmap("./icons/icon.ico")

# Entry box
entry = ttk.Entry(root, font=("Arial", 17))
entry.grid(column=0, row=0, columnspan=4, padx=10, pady=30)

# Se declaran e inicializan las variables
global firstNumber
firstNumber = 0
global secondNumber
secondNumber = 0
global operator
operator = ""
global result
result = 0

# Función que permite ingresar los números en la calculadora
def numberClick(number):
    entry.insert(END, number)

# Función que permite guardar el primer número y el operador utilizado
def operation(op):
    try:
        global firstNumber
        global operator
        firstNumber = float(entry.get())
        operator = op
        entry.delete(0, END)
    except ValueError:
        messagebox.showwarning("Error", "Ingrese un número antes de utilizar los operadores.")

# Función que evalúa el resultado dependiendo del operador que se utilizó
def equal():
    try:
        global firstNumber
        global secondNumber
        global operator 
        secondNumber = float(entry.get())

        if operator == "+":
            result = secondNumber + firstNumber
        elif operator == "-":
            result = firstNumber - secondNumber
        elif operator == "x":
            result = firstNumber * secondNumber
        elif operator == "/":
            result = firstNumber / secondNumber
        elif operator == "%":
            result = (firstNumber / 100) * secondNumber

        entry.delete(0, END)
        entry.insert(0, result)
    except ValueError:
        messagebox.showwarning("Error", "No se puede usar el botón de igual si aún no se ha realizado\nninguna operación.")

        
# Funcion que elimina el texto en pantalla y libera las variables utilizadas
def clear():
    entry.delete(0, END)
    global firstNumber
    firstNumber = 0
    global secondNumber
    secondNumber = 0
    global result
    result = 0
    global operator
    operator = ""

# Font style
style = ttk.Style()
style.configure("style.TButton", font=('Arial', 16), padding=(-30, 25))
style.map("style.TButton", border=[("active", 10)])

## Define buttons
# First row
buttonCE = ttk.Button(root, text="CE", style='style.TButton', command=clear)
buttonPer = ttk.Button(root, text="%", style="style.TButton", command=lambda: operation("%"))
buttonDiv = ttk.Button(root, text="/", style="style.TButton", command=lambda: operation("/"))

# Second row
button7 = ttk.Button(root, text="7", style="style.TButton", command=lambda: numberClick(7))
button8 = ttk.Button(root, text="8", style="style.TButton", command=lambda: numberClick(8))
button9 = ttk.Button(root, text="9", style="style.TButton", command=lambda: numberClick(9))
buttonMult = ttk.Button(root, text="x", style="style.TButton", command=lambda: operation("x"))

# Third row
button4 = ttk.Button(root, text="4", style="style.TButton", command=lambda: numberClick(4))
button5 = ttk.Button(root, text="5", style="style.TButton", command=lambda: numberClick(5))
button6 = ttk.Button(root, text="6", style="style.TButton", command=lambda: numberClick(6))
buttonSub = ttk.Button(root, text="-", style="style.TButton", command=lambda: operation("-"))

# Fourth row
button1 = ttk.Button(root, text="1", style="style.TButton", command=lambda: numberClick(1))
button2 = ttk.Button(root, text="2", style="style.TButton", command=lambda: numberClick(2))
button3 = ttk.Button(root, text="3", style="style.TButton", command=lambda: numberClick(3))
buttonAdd = ttk.Button(root, text="+", style="style.TButton", command=lambda: operation("+"))

# Fifth row
button0 = ttk.Button(root, text="0", style="style.TButton", command=lambda: numberClick(0))
buttonDot = ttk.Button(root, text=".", style="style.TButton", command=lambda: numberClick("."))
buttonEq = ttk.Button(root, text="=", style="style.TButton", command=equal)

## Establecer el orden de la cuadrícula
# First row
buttonCE.grid(column=0, row=1, columnspan=2, sticky="we")
buttonPer.grid(column=2, row=1)
buttonDiv.grid(column=3, row=1)

# Second row
button7.grid(column=0, row=2)
button8.grid(column=1, row=2)
button9.grid(column=2, row=2)
buttonMult.grid(column=3, row=2)

# Third row
button4.grid(column=0, row=3)
button5.grid(column=1, row=3)
button6.grid(column=2, row=3)
buttonSub.grid(column=3, row=3)

# Fourth row
button1.grid(column=0, row=4)
button2.grid(column=1, row=4)
button3.grid(column=2, row=4)
buttonAdd.grid(column=3, row=4)

# Fifth row
button0.grid(column=0, row=5, columnspan=2, sticky="we")
buttonDot.grid(column=2, row=5)
buttonEq.grid(column=3, row=5)

root.resizable(False, False) # Evita que se pueda modificar el tamaño de la ventana

# Requerimiento de TKinter para funcionar ya que dada la naturaleza de Python como
# lenguaje interpretado el código tiene que ejecutarse en búcle para poder mostrar
# la interfaz adecuadamente
root.mainloop()