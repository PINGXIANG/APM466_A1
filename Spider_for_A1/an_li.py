import random
from typing import List

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EXECUTABLE_PATH = 'chromedriver.exe'

def an_li():
    f = open("an_li_blueprint.txt", "r", newline="")
    AN_LI = []
    lines = f.readlines()
    for line in lines:
        AN_LI.append(line.strip())
    f.close()

    an_li = webdriver.Chrome(EXECUTABLE_PATH)
    r = random.choice(range(len(AN_LI)))
    an_li.get(AN_LI[r])
    time.sleep(10)
    an_li.find_element(By.XPATH, '//button[@aria-label="播放"]').click()
    print("It will take around 10 min for each project, how about eating this 安利~ (ÒωÓױ)?")

    f = open("an_li_blueprint.txt", "w", newline="")
    lines.pop(r)
    for line in lines:
        f.write(line)
    f.close()

print("用我软件，吃我安利 o(*￣▽￣*)ブ")

if __name__ == "__main__":

    f = open("selected_ISIN.txt", "r", newline="")
    txt = f.readlines()
    id = txt[0].split(" ")
    coupon = txt[1].split(" ")
    date = txt[2].split(" ")
    f.close()

    f = open("selected_ISIN.txt", "a", newline="")
    i = 0
    while i < len(id):
        new_line = id[i].strip() + " & " + coupon[i].strip() + " & " + date[i].strip()
        f.write(new_line + "\n")
        i = i + 1
    f.close()