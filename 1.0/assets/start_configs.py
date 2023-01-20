import os
import functions
import time


path = os.path.dirname(os.path.abspath(__file__))
path_configs = path + "\\configs.txt"
path_subjects = path + "\\subjects.txt"


with open(path_configs,"r+", encoding="utf8") as file:
    
    read_data = file.read()
    
    if len(read_data) == 0:
        functions.login(path_configs)
        
    else:
        
        
        inital_text = "Bem vindo ao Blackboard Extractor"
        inital_text_center =  inital_text.center(50)
        
        print(len(inital_text_center) * "=")
        print('')
        print(inital_text_center)
        
        
        functions.line_space()
        print(functions.center_string("AVISO: O programa está em fase de testes"))
        print(functions.center_string("Made by: Lucas Espina"))
        print("")
        print(len(inital_text_center) * "=")
        
        time.sleep(3)
        
        os.system("cls")
   
   
    while True:     
        
        logs = functions.user_passworld()
        username = logs[0]
        passworld = logs[1]
                   
        with open(path_subjects,"r+", encoding="utf8") as file:
    
            data_subject = file.read()
            
            subs_list = data_subject.split("\n")
            subs_list_sorted = sorted(subs_list)
            
            for i in subs_list:
                if i == "":
                    subs_list_sorted.remove(i)
            
            functions.line_space()
            
            functions.subs_menu(subs_list_sorted)
            print("")
            print("[9] - Configurações")
            
            
            functions.line_space()
        
        
        opc = int(input("Digite a opção desejada: "))
        
        if opc == 9:
            
            print("")
            
            functions.config_menu()
            
        if opc == 1:
            
            functions.menu_by_sub()
            
            by_sub_opc = int(input("Digite a opção desejada: "))
            
            
            if by_sub_opc == 1:
            
                text_tag = subs_list_sorted[0]
                
                functions.extract(text_tag, username, passworld)
            
            if by_sub_opc == 2:
                
                
                text_tag = subs_list_sorted[0]
                functions.extract_score(text_tag, username, passworld)
            
            
        if opc == 2:
            
            functions.menu_by_sub()
            
            by_sub_opc = int(input("Digite a opção desejada: "))
            
            
            if by_sub_opc == 1:
            
                text_tag = subs_list_sorted[1]
                
                functions.extract(text_tag, username, passworld)
                
            if by_sub_opc == 2:
            
            
                text_tag = subs_list_sorted[1]
                functions.extract_score(text_tag, username, passworld)
        
        if opc == 3:
            
            functions.menu_by_sub()
            
            by_sub_opc = int(input("Digite a opção desejada: "))
            
            
            if by_sub_opc == 1:
            
                text_tag = subs_list_sorted[2]
                
                functions.extract(text_tag, username, passworld)
                
            if by_sub_opc == 2:
            
            
                text_tag = subs_list_sorted[2]
                functions.extract_score(text_tag, username, passworld)
                
        if opc == 4:
            
            functions.menu_by_sub()
            
            by_sub_opc = int(input("Digite a opção desejada: "))
            
            
            if by_sub_opc == 1:
            
                text_tag = subs_list_sorted[3]
                
                functions.extract(text_tag, username, passworld)
                
            if by_sub_opc == 2:
            
                text_tag = subs_list_sorted[3]
                functions.extract_score(text_tag, username, passworld)
                
                
        enter = input("Pressione enter para continuar")
        
        
        os.system("cls")
        
        
    
    
    
        
    
    
    
    
    
    
    
    
    
    
                
                
    
            
            
        
        
        
        
        
        
        
        
        
        

