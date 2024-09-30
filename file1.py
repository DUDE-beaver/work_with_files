import colorama
from colorama import Fore

text1=input("Birinchi matn kiriting: ")
text2=input("Ikkinchi matn kiriting: ")
text3=input("Uchinchi matn kiriting: ")

print()
print("Chiqish: ")
print(Fore.RED + text1)
print(Fore.GREEN + text2)
print(Fore.BLUE + text3)