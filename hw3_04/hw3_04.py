import sys
import os
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows
init(autoreset=True)

def show_directory_structure(directory_path, indent=""):
    try:
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            if os.path.isdir(full_path):
                print(indent + Fore.BLUE + f"[{item}]")
                show_directory_structure(full_path, indent + "    ")
            else:
                print(indent + Fore.GREEN + item)
    except PermissionError:
        print(indent + Fore.RED + "[Permission Denied]")

def main():
    if len(sys.argv) < 2:
        print("❌ Будь ласка, вкажи шлях до директорії як аргумент командного рядка.")
        return

    directory = sys.argv[1]

    if not os.path.exists(directory):
        print(f"❌ Шлях не існує: {directory}")
        return

    if not os.path.isdir(directory):
        print(f"❌ Це не директорія: {directory}")
        return

    print(Fore.YELLOW + f"Структура директорії: {directory}\n")
    show_directory_structure(directory)

if __name__ == "__main__":
    main()
