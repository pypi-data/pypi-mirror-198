# Package for setup the color terminal
# You need to have installed "colorama" package

from colorama import Fore, Back, Style

class Terminal:

    """
    List of available colors:
        - YELLOW
        - BLACK
        - BLUE
        - CYAN
        - GREEN
        - MAGENTA
        - RED
        - WHITE
        - RESET
    """

    def YELLOW():
        print(Fore.YELLOW)
    
    def BLACK():
        print(Fore.BLACK)
    
    def BLUE():
        print(Fore.BLUE)
    
    def CYAN():
        print(Fore.CYAN)
    
    def GREEN():
        print(Fore.GREEN)
    
    def MAGENTA():
        print(Fore.MAGENTA)
    
    def RED():
        print(Fore.RED)
    
    def WHITE():
        print(Fore.WHITE)
    
    def RESET():
        print(Fore.RESET)
