from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time 
from assets import login


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto("https://insper.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_375_1")
    page.fill("input#user_id", login.username)
    page.fill("input#password", login.password)
    page.click("input[id='entry-login']")
    page.click("button[class='button-1']")
    page.click("text=ACIONAMENTOS ELÉTRICOS - 2A 2022/2")
    

    html = page.inner_html("#announcementForm")
    soup = BeautifulSoup(html, 'html.parser')
    
    total_announcements = soup.find("li", class_="clearfix").text
    list_announcements = []
    
    
    for li in soup.find_all("li", class_="clearfix"):
        list_announcements.append(li.text)
    
    print(list_announcements[1])
    
    
    
    
    
    