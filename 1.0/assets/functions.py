from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time 
import login
import os



def login(path_configs):
    
    with open(path_configs,"r+", encoding="utf8") as file:

        read_data = file.read()

        login = str(input("Digite seu login: "))
        passworld = str(input("Digite sua senha: "))
        
        credentials = [login, passworld]
        
        for i in credentials:
            file.write(i + "\n")
                       
def add_subject(file):
    
    subject = str(input("Digite o nome da disciplina: "))
    
    subject_formated = subject.upper()
    
    file.write(subject_formated + "\n")
    
    print("")
    
    print("Disciplina adicionada com sucesso")
    
    line_space()
    
def center_string(text):
    return text.center(50)

def line_space():            
        inital_text = "Bem vindo ao Blackboard Extractor"
        inital_text_center =  inital_text.center(50)
            
        print("")
        
        print(len(inital_text_center) * "=")
        
        print('')
        
def subs_menu(subs_list_sorted):
    
    i = 0
    
    while i < len(subs_list_sorted):
        print(f"[{i+1}] - {subs_list_sorted[i]}")
        i += 1
    
def extract(text,username, password):
        
    
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
        
        total_announcements = soup.find("li", class_="clearfix").text
        list_announcements = []
        
        
        for li in soup.find_all("li", class_="clearfix"):
            list_announcements.append(li.text)
        
        i = 0
        
        while i < 3:
            
            print(list_announcements[i])
            i += 1
    
def menu_by_sub():
    
    line_space()
    
    print("[1] - Ver os avisos")
    print("[2] - Calcular média")
    
    line_space()
    
def extract_subs():
    tst = []
    tst_2 = [tst]

    mat = []

    sub_2022_2 = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
        page.fill("input#user_id", login.username)
        page.fill("input#password", login.password)
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
        # i += 1
        
    for i in tst:
        tst_2.append(i.split("\n"))
        
    for i in tst_2:
        mat.append(i[0])
        
    mat.pop(0)

    for i in mat:
        
        if "- 2A 2022/2" in i:
            sub_2022_2.append(i)

    path = os.path.dirname(os.path.abspath(__file__))
    path_subjects = path + "\\subjects.txt"   

    with open(path_subjects, "r+",encoding="utf8" ) as file:
        for i in sub_2022_2:
            file.write(i + "\n")
        
def user_passworld():
    path = os.path.dirname(os.path.abspath(__file__))
    path_configs = path + "\\configs.txt"
    
    with open(path_configs, "r",encoding="utf8" ) as file:
        username = file.readline()
        password = file.readline()
        
        
        
        
        return username, password

def extract_score(text, username, password):


    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
        page.fill("input#user_id", username)
        page.fill("input#password", password)
        page.click("input[id='entry-login']")
        page.click("button[class='button-1']")
        page.click("text={}".format(text))
        page.click("text=Notas")



        html = page.inner_html("#grades_wrapper ")
        soup = BeautifulSoup(html, 'html.parser')
        
        total_announcements = soup.find("li", class_="clearfix")

        for li in soup.find_all("div", class_="sortable_item_row graded_item_row row expanded"):

            print(li.text)
            