import tkinter as tk
def calcular(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos")
        return
    resultado = 0
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir entre cero"
    label_resultado.config(text=f"Resultado: {resultado}")
ventana = tk.Tk()
ventana.title("Calculadora")
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.TOP)
btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: calcular("suma"))
btn_sumar.pack(side=tk.LEFT)
btn_restar = tk.Button(ventana, text="Restar", command=lambda: calcular("resta"))
btn_restar.pack(side=tk.LEFT)
btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicacion"))
btn_multiplicar.pack(side=tk.LEFT)
btn_dividir = tk.Button(ventana, text="Dividir", command=lambda: calcular("division"))
btn_dividir.pack(side=tk.LEFT)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(side=tk.BOTTOM)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(side=tk.BOTTOM)
label_resultado = tk.Label(ventana)
label_resultado.pack(side=tk.BOTTOM)
ventana.mainloop()