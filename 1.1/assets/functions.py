from bs4 import BeautifulSoup
import time 
import os
import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


anuncio_materia = {}

path_assets = os.path.dirname(os.path.abspath(__file__))
path_account_data= os.path.dirname(path_assets) + "\\data\\account_data.txt"
path_subject = os.path.dirname(path_assets) + "\\data\\subjects.txt"

with open(path_account_data,"r+", encoding="utf8") as account_data:
    username = account_data.readline()
    password = account_data.readline()
with open(path_subject,"r+", encoding="utf8") as subjects:
    subject = subjects.readlines()

def register():
    
    login = str(input("Digite seu login: "))
    password = str(input("Digite sua senha: "))
    
    while login == "" or password == "":
        
        print("")
        print("usuário ou senha inválidos, por favor, tente novamente.")
        print("")
        login = str(input("Digite seu login: "))
        password = str(input("Digite sua senha: "))
    
    credentials = [login, password]
    
    
    with open(path_account_data,"w+", encoding="utf8") as account_data:
        
        for i in credentials:
            account_data.write(i + "\n")
            
def subject_extrator():

    tst = []
    tst_2 = [tst]

    mat = []

    sub_2022_2 = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
        page.fill("input#user_id", username)
        page.fill("input#password", password)
        page.click("input[id='entry-login']")
        page.click("button[class='button-1']")
        

        html = page.inner_html("#_26_1termCourses_noterm")
        soup = BeautifulSoup(html, 'html.parser')
                
        list_announcements = []
        
        for li in soup.find_all("li"):
            list_announcements.append(li.text)
        
    i = 0 

    for i in list_announcements:
        tst.append(i.strip())

        
    for i in tst:
        tst_2.append(i.split("\n"))
        
    for i in tst_2:
        mat.append(i[0])
        
    mat.pop(0)

    for i in mat:
        
        if "- 2A 2022/2" in i:
            sub_2022_2.append(i)
            
    with open(path_subject,"r+", encoding="utf8") as subjects:
        for i in sub_2022_2:  
            subjects.write(i + "\n")        
            
def announcement_extrator(text,username, password):
        
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
        page.fill("input#user_id", username)
        page.fill("input#password", password)
        page.click("input[id='entry-login']")
        page.click("button[class='button-1']")
        page.click("text={}".format(text))
        
        html = page.inner_html("#announcementForm")
        soup = BeautifulSoup(html, 'html.parser')
        list_announcements = []
        
        for li in soup.find_all("li", class_="clearfix"):
            list_announcements.append(li.text)
        
        return list_announcements
                       
def menu_inicial():
    print("="*60)
    print("")
    print("Bem vindo ao Blackboard Extrator".center(60))
    print("")
    print("="*60)
    
def all_announcement():     
    
    subject_extrator()
    
    with open(path_subject,"r+", encoding="utf8") as subjects:
        subject = subjects.readlines()
    
    
    for anuncio in subject:
        
        
        y = anuncio.strip()
        y.replace("\n", "")
        x = announcement_extrator(anuncio,username, password)
        
        anuncio_materia[y] = x
    
        print(anuncio)

    return anuncio_materia

def check_login():
    
    with open(path_account_data,"r+", encoding="utf8") as account_data:
        
        if (account_data.read()).strip() == "":
            
            print("")
            print("Você ainda não está logado, por favor, faça o login.")
            print("")
            print("="*60)
            print("")
            register()
                      
def check_error_area():
    
    with open(path_account_data,"r+", encoding="utf8") as account_data:
        
        arquivo = account_data.readlines()
        username = arquivo[0]
        password = arquivo[1]
    
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
        page.fill("input#user_id", username)
        page.fill("input#password", password)
        page.click("input[id='entry-login']")
        
        
        if page.url != "https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1":
            html = page.inner_html("#erroArea")
                    
            if html.strip() != "":

                print("Login ou senha incorretos, por favor, tente novamente.")
                
                return False
        
        else:
            return True
        

def menu():

        with open(path_subject,"r+", encoding="utf8") as file:

            data_subject = file.read()
            
            subs_list = data_subject.split("\n")
            subs_list_sorted = sorted(subs_list)
                        
            for i in subs_list:
                if i == "":
                    subs_list_sorted.remove(i)
                    
        i = 0

        while i < len(subs_list_sorted):
            print(f"[{i+1}] - {subs_list_sorted[i]}")
            i += 1
        
def opc_choose(opc, all_announcement):
    
    
    with open(path_subject,"r+", encoding="utf8") as file:

        data_subject = file.read()
        
        subs_list = data_subject.split("\n")
        subs_list_sorted = sorted(subs_list)
    
    
    
    if opc in ['1','2','3','4','5']:
        
        subs = subs_list_sorted[int(opc)]

        
        for anuncion in all_announcement[subs]:
            print(anuncion)
        
    else: 
        print('selecione uma opção valida')
        
    
    