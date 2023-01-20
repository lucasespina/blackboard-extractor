from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time 
import login
import os


tst = []
tst_2 = [tst]

mat = []

sub_2022_2 = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
    page.fill("input#user_id", login.username)
    page.fill("input#password", login.password)
    page.click("input[id='entry-login']")
    page.click("button[class='button-1']")
    

    html = page.inner_html("#_26_1termCourses_noterm")
    soup = BeautifulSoup(html, 'html.parser')
    
    total_announcements = soup.find("ul").text
    
    
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