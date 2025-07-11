"Utility function for formatting and display"

from  colorama import Fore, Style, init

#Colorama initialization
init()

def print_header(text):
    "Print a formatted header"
    print(f"{Fore.CYAN}{Style.BRIGHT}{text.center(60)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*60}{Style.RESET_ALL}")

def print_success(text):
    "Print sucess message in green color"
    print(f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}")

def print_error(text):
    "Print error message in red"
    print(f"{Fore.RED}{Style.BRIGHT} {text}{Style.RESET_ALL}")

def print_info(text):
    "print info message in blue color"
    print(f"{Fore.BLUE}{text}{Style.RESET_ALL}")

def print_warning(text):
    "display warning message in yellow"
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")

def print_question_header(current, total):
    "print formatted quetsion header"
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}--- Question {current} of {total} ---{Style.RESET_ALL}")
