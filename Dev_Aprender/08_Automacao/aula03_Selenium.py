
#! SELENIUM
# Webdriver - simulador de uso de navegador;

# PASSOS
 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#Iniciar o webdriver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#1 - Navegar até https://automatize.netlify.app/
driver.get('https://automatize.netlify.app/')
sleep(2)
#2.0 - encontrar o elemento pelo ID;
campo_email = driver.find_element(By.ID,'email')
#2 - clicar em email, digitar um email;
campo_email.click()
campo_email.send_keys('victor1cg@hotmail.com')
sleep(2)

#3 - clicar em senha, digitar uma senha [XPATH];
campo_senha = driver.find_element(By.XPATH,"//input[@type='password']")
campo_senha.click()
campo_senha.send_keys('123456')
campo_senha.click()
sleep(2)

#4 - clicar no botão iniciar;
botao = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
botao.click()
sleep(2)

input()