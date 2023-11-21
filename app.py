from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)


navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
navegador.find_element('xpath','/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("judas")
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("guilhermeferreira082@gmail.com")
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("61995246301")
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/button').click()

