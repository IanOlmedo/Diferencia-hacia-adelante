import numpy as np
import shutil
from colorama import Fore, Style, init
from tabulate import tabulate

# Inicializar colorama
init(autoreset=True)

def print_header(title):
    columns = shutil.get_terminal_size().columns
    print(Fore.BLUE + Style.BRIGHT + '-' * columns)
    print(Fore.YELLOW + Style.BRIGHT + title.center(columns))
    print(Fore.BLUE + Style.BRIGHT + '-' * columns)

def diferencias_hacia_adelante(y, h):
    print_header("Tabla de Diferencias Hacia Adelante")
    n = len(y)
    tabla_difs = np.zeros((n, n))
    tabla_difs[:, 0] = y  # La primera columna son los valores originales de y

    # Calcular las diferencias finitas hacia adelante
    for j in range(1, n):
        for i in range(n - j):
            tabla_difs[i, j] = tabla_difs[i + 1, j - 1] - tabla_difs[i, j - 1]

    # Calcular los valores de x
    x_values = [i * h for i in range(n)]

    # Crear la tabla con los valores de x y diferencias
    headers = ["x", "y"] + [f"Δ^{i}y" for i in range(1, n)]
    table = []
    for i in range(n):
        row = [x_values[i]] + [round(tabla_difs[i, j], 3) if i < n - j else "" for j in range(n)]
        table.append(row)

    print(tabulate(table, headers, tablefmt="fancy_grid"))
    return tabla_difs

def derivada_diferencias_adelante(x0, y, h, n):
    # Calcular las diferencias hacia adelante y obtener los deltas disponibles
    difs = diferencias_hacia_adelante(y, h)
    
    # Obtener los deltas disponibles hasta n-1
    deltas_disponibles = [difs[0, j] for j in range(1, n) if j < difs.shape[1]]
    
    # Calcular la derivada usando la fórmula dada
    derivada = 0.0
    for k in range(len(deltas_disponibles)):
        derivada += (-1) ** k * deltas_disponibles[k] / (k + 1)
    
    derivada /= h
    return derivada

def comenzar():
    print_header("Cálculo de Diferencias Hacia Adelante")
    print(Fore.LIGHTBLACK_EX + "¿Listo para comenzar? (si/no)")
    comienzo = input("").strip().lower()
    if comienzo == "si":
        main()
    else:
        print(Fore.RED + "Hasta pronto!")

def main():
    print_header("Cálculo de Diferencias Hacia Adelante")

    h = float(input(Fore.CYAN + "Ingrese la longitud entre puntos (h): "))
    n = int(input(Fore.CYAN + "Ingrese la cantidad de puntos: "))
    x0 = float(input(Fore.CYAN + "Ingrese el valor de x0: "))

    y = []
    for i in range(n):
        valor = input(Fore.CYAN + f"Ingrese el valor de y{i}: ")
        try:
            y.append(float(valor))
            print(Fore.GREEN + f"Valor de y{i}: {valor} agregado a la lista")
        except ValueError:
            print(Fore.RED + "Valor no válido. Por favor, ingrese un número.")

    while True:
        option = input(Fore.CYAN + "¿Desea calcular la diferencia hacia adelante (si/no)?: ").strip().lower()
        if option == 'si':
            derivada = derivada_diferencias_adelante(x0, np.array(y), h, n)
            print_header("Resultado de la Derivada")
            print(Fore.GREEN + f"La derivada aproximada en x0 = {x0} con h = {h} es {derivada:.4f}")
            break
        elif option == 'no':
            print(Fore.RED + "Terminando la ejecución...")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, responda 'si' o 'no'.")

if __name__ == "__main__":
    comenzar()

