from assets import functions

from data import *
import os

functions.menu_inicial()

functions.check_login()

while functions.check_error_area() == False:
    functions.register()
    
# functions.subject_extrator()
all_anouncements = functions.all_announcement()
while True:
    os.system("cls")
    print("")
    functions.menu()
    print("")

    opc = input("Digite a opção desejada: ")


    functions.opc_choose(opc, all_anouncements)
    
    input("Pressione qualquer tecla para continuar...")

