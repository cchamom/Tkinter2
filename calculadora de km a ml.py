import tkinter as tk

# Función para convertir kilómetros a millas
def convertir():
    try:
        kilometros = float(entrada_kilometros.get())
        millas = kilometros * 0.621371
        etiqueta_resultado.config(text=f"{kilometros} kilómetros son: {millas} millas")
    except ValueError:
        etiqueta_resultado.config(text="Ingrese un valor numérico válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de kilómetros a millas")
ventana.geometry("300x150")

etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kilómetros:")
etiqueta_instruccion.grid(row=0, columnspan=2, padx=10, pady=10)

entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=2, column=1, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()

