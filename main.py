import os
import time
from colorama import Fore,Back,Style

def menu():
    print(Fore.BLUE+"""
        
        [+] VOID [+]

        [M] Main
        [1] Web Hacking & Scanning Tools

    """)


def DarkLight():
    os.system("clear")

    menu()
    n = input(Fore.RED+"[+] Please Select : ")
    if n=="1":
        os.system("sudo python3 ./core/web/main.py")
    if n=="M" or n == "m":
        os.system("sudo python3 main.py")


if __name__ == "__main__":
    DarkLight()