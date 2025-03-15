from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




def Pregunta_mail():
  email = input("Escriu el teu email: ");
  return str(email);


def FundacioLink(email):
  service = Service(executable_path="chromedriver.exe");
  driver = webdriver.Chrome(service=service);
  driver.get("https://www.fundaciocollserola.cat/intranet/token.php");
  time.sleep(1);
  input_elements = driver.find_elements(By.TAG_NAME,value =  "option");
  for i in range(len(input_elements)):
    if input_elements[i].text == "Informes Cim Estela":
      input_elements[i].click();

  input_mail = driver.find_element(By.TAG_NAME, value = "input")
  input_mail.send_keys(email);
  time.sleep(0.5)
  input_mail.send_keys(Keys.ENTER)
