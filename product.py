import tkinter as tk

def calcular_producto_medio(semilla_x0, semilla_xi, digitos, n):
    resultados = []
    xi = semilla_xi
    for i in range(n):
        yi = semilla_x0 * xi
        xi = int(str(yi).zfill(2 * digitos)[digitos//2: -digitos//2])
        ri = int(str(yi).zfill(2 * digitos)[-digitos:])
        resultados.append((yi, xi, ri))
    return resultados

def generar_lista():
    semilla_x0 = int(entrada_semilla_x0.get())
    semilla_xi = int(entrada_semilla_xi.get())
    digitos = int(entrada_digitos.get())
    n = int(entrada_n.get())

    resultados = calcular_producto_medio(semilla_x0, semilla_xi, digitos, n)

    lista_resultados.delete(0, tk.END)
    for yi, xi, ri in resultados:
        lista_resultados.insert(tk.END, f"Yi: {yi}, Xi: {xi}, Ri: {ri}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Algoritmo Producto Medio")

# Crear los widgets
etiqueta_semilla_x0 = tk.Label(ventana, text="Semilla X0:")
etiqueta_semilla_x0.grid(row=0, column=0, padx=5, pady=5)

entrada_semilla_x0 = tk.Entry(ventana)
entrada_semilla_x0.grid(row=0, column=1, padx=5, pady=5)

etiqueta_semilla_xi = tk.Label(ventana, text="Semilla Xi:")
etiqueta_semilla_xi.grid(row=1, column=0, padx=5, pady=5)

entrada_semilla_xi = tk.Entry(ventana)
entrada_semilla_xi.grid(row=1, column=1, padx=5, pady=5)

etiqueta_digitos = tk.Label(ventana, text="Número de dígitos (D):")
etiqueta_digitos.grid(row=2, column=0, padx=5, pady=5)

entrada_digitos = tk.Entry(ventana)
entrada_digitos.grid(row=2, column=1, padx=5, pady=5)

etiqueta_n = tk.Label(ventana, text="Cantidad de números (n):")
etiqueta_n.grid(row=3, column=0, padx=5, pady=5)

entrada_n = tk.Entry(ventana)
entrada_n.grid(row=3, column=1, padx=5, pady=5)

boton_generar = tk.Button(ventana, text="Generar Lista", command=generar_lista)
boton_generar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

lista_resultados = tk.Listbox(ventana, width=40, height=10)
lista_resultados.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
ventana.mainloop()
