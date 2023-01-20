from bs4 import BeautifulSoup
import time 
import os
import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
    page.fill("input#user_id", "lucaseqc")
    page.fill("input#password", "Milenasantos@01")
    page.click("input[id='entry-login']")
    page.click("button[class='button-1']")
    page.click("text=ACIONAMENTOS ELÉTRICOS - 2A 2022/2")
    page.get_by_title("Notas").click()

    
    html = page.locator("#grades_wrapper").inner_html()
    soup = BeautifulSoup(html, 'html.parser')
    
    
    lst = []
    
    
    for div in soup.find_all("div"):
        lst.append(div.text)
        
    
with open("tst.txt","w", encoding="utf8") as notas:
    for i in lst:  
        notas.write(i + "\n")
    

with open("tst.txt","r+", encoding="utf8") as notas:
    
    for line in notas:
        line.strip()
        notas.write(line)



    
    
        
