import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)  # Inicializa colorama y autoreset=True restablece los colores después de cada impresión

print(f"{Fore.BLACK}BLACK")
print(f"{Fore.RED}RED")
print(f"{Fore.GREEN}GREEN")
print(f"{Fore.YELLOW}YELLOW")
print(f"{Fore.BLUE}BLUE")
print(f"{Fore.MAGENTA}MAGENTA")
print(f"{Fore.CYAN}CYAN")
print(f"{Fore.WHITE}WHITE")

# Colores de fondo (Background colors)
print(f"{Back.BLACK}{Fore.WHITE}BLACK BACKGROUND")
print(f"{Back.RED}{Fore.WHITE}RED BACKGROUND")
print(f"{Back.GREEN}{Fore.BLACK}GREEN BACKGROUND")
print(f"{Back.YELLOW}{Fore.BLACK}YELLOW BACKGROUND")
print(f"{Back.BLUE}{Fore.WHITE}BLUE BACKGROUND")
print(f"{Back.MAGENTA}{Fore.WHITE}MAGENTA BACKGROUND")
print(f"{Back.CYAN}{Fore.BLACK}CYAN BACKGROUND")
print(f"{Back.WHITE}{Fore.BLACK}WHITE BACKGROUND")

# Estilos adicionales
print(f"{Style.BRIGHT}BRIGHT TEXT")
print(f"{Style.DIM}DIM TEXT")
print(f"{Style.NORMAL}NORMAL TEXT")
print(f"{Style.RESET_ALL}RESET ALL ATTRIBUTES")