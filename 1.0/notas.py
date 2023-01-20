from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time 

import os


username = "lucaseqc"
password = "Milenasantos@01"
text = "MATEMÁTICA DA VARIAÇÃO - 2A 2022/2"




with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
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

