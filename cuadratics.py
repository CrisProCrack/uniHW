import tkinter as tk

def cuadrados_medios(semilla, digitos, cantidad):
    resultados = []
    matriz_resultados = []
    for _ in range(cantidad):
        semilla_cuadrada = semilla ** 2
        semilla_str = str(semilla_cuadrada).zfill(2 * digitos)
        centro_inicio = (len(semilla_str) - digitos) // 2
        ri = int(semilla_str[centro_inicio:centro_inicio + digitos])
        resultados.append((semilla, semilla_cuadrada, ri / (10 ** digitos)))
        matriz_resultados.append((semilla, ri))
        semilla = ri

    return resultados, matriz_resultados

def generar_numeros_aleatorios():
    semilla = int(entrada_semilla.get())
    digitos = int(entrada_digitos.get())
    cantidad = int(entrada_cantidad.get())
    resultados, matriz_resultados = cuadrados_medios(semilla, digitos, cantidad)
    mostrar_resultados(resultados, matriz_resultados)

def mostrar_resultados(resultados, matriz_resultados):
    ventana_resultados = tk.Toplevel(ventana_principal)
    ventana_resultados.title("Resultados")
    
    tk.Label(ventana_resultados, text="i").grid(row=0, column=0)
    tk.Label(ventana_resultados, text="X").grid(row=0, column=1)
    tk.Label(ventana_resultados, text="Ri").grid(row=0, column=2)

    for i, (semilla, semilla_cuadrada, ri) in enumerate(resultados):
        tk.Label(ventana_resultados, text=i+1).grid(row=i+1, column=0)
        tk.Label(ventana_resultados, text=semilla).grid(row=i+1, column=1)
        tk.Label(ventana_resultados, text=ri).grid(row=i+1, column=2)

    matriz_label = tk.Label(ventana_resultados, text="Matriz:")
    matriz_label.grid(row=len(resultados)+2, columnspan=3)

    for i, (semilla, ri) in enumerate(matriz_resultados):
        tk.Label(ventana_resultados, text="X{}:".format(i+1)).grid(row=len(resultados)+3+i, column=0)
        tk.Label(ventana_resultados, text=semilla).grid(row=len(resultados)+3+i, column=1)
        tk.Label(ventana_resultados, text="R{}:".format(i+1)).grid(row=len(resultados)+3+i, column=2)

ventana_principal = tk.Tk()
ventana_principal.title("Generador de Números Aleatorios - Cuadrados Medios")

tk.Label(ventana_principal, text="Semilla:").grid(row=0, column=0)
entrada_semilla = tk.Entry(ventana_principal)
entrada_semilla.grid(row=0, column=1)

tk.Label(ventana_principal, text="Dígitos:").grid(row=1, column=0)
entrada_digitos = tk.Entry(ventana_principal)
entrada_digitos.grid(row=1, column=1)

tk.Label(ventana_principal, text="Cantidad:").grid(row=2, column=0)
entrada_cantidad = tk.Entry(ventana_principal)
entrada_cantidad.grid(row=2, column=1)

boton_generar = tk.Button(ventana_principal, text="Generar", command=generar_numeros_aleatorios)
boton_generar.grid(row=3, columnspan=2)

ventana_principal.mainloop()