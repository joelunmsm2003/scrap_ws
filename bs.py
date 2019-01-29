# -*- coding: utf-8 -*-

print "SSSSSSSSSSSSSSSSSSUCKING EVERYTHING IN SSSSSSSSSSSIGHT                  "
print "                                                                        "
print "              \                                                         "
print "               \                                                        "
print "                   /^\/^\                                               "
print "                 _|__|  O|                                              "
print "        \/     /~     \_/ \                                             "
print "         \____|__________/  \                                           "
print "                \_______      \                                         "
print "                        `\     \                 \                      "
print "                          |     |                  \                    "
print "                         /      /                    \                  "
print "                        /     /                       \\                "
print "                      /      /                         \ \              "
print "                     /     /                            \  \            "
print "                   /     /             _----_            \   \          "
print "                  /     /           _-~      ~-_         |   |          "
print "                 (      (        _-~    _--_    ~-_     _/   |          "
print "                  \      ~-____-~    _-~    ~-_    ~-_-~    /           "
print "                    ~-_           _-~          ~-_       _-~   - andy -"
print "                       ~--______-~                ~-___-~               "

             
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import requests

page = requests.get("https://www.globohq.com/dashboard/index")


import time
import datetime

import json




driver = webdriver.Chrome('/Users/xiencias/code/chromedriver')

driver.get('https://web.whatsapp.com/');

def search_chatter(driver, person):
    """
    Function that search the specified user and activates his chat
    """

    while True:
        for chatter in driver.find_elements_by_xpath("//div[@class='_2wP_Y']"):
            chatter_name = chatter.find_element_by_xpath(
                ".//span[@class='_1wjpf']").text

            print 'person..',chatter_name
            if chatter_name == person:
                chatter.find_element_by_xpath(
                    ".//div[@tabindex='-1']").click()
                return



def search_chatter_last(driver):
	

	try:

		for chatter in driver.find_elements_by_xpath("//div[@class='_2wP_Y']"):
			chatter_name = chatter.find_element_by_xpath(".//span[@class='_1wjpf']").text

			print 'person..',chatter_name



			chatter.find_element_by_xpath(".//div[@tabindex='-1']").click()


		print 'fin......'

		return

	except:

		pass




def read_last_in_message(driver):
    """
    Reading the last message that you got in from the chatter
    """
    message = ''
    for messages in driver.find_elements_by_xpath("//div[@class='_3_7SH _3DFk6 message-in']"):

        time.sleep(3)
        
        try:
            message_container = messages.find_element_by_xpath(
                ".//div[@class='copyable-text']"
            )

            emisor = message_container.get_attribute("data-pre-plain-text")


            #print 'emisor..',emisor



            message = message_container.find_element_by_xpath(
                ".//span[@class='selectable-text invisible-space copyable-text']"
            ).text

            print emisor.encode('ascii', 'ignore').encode('ascii', 'replace')+' : '+message.encode('ascii', 'ignore').encode('ascii', 'replace')

            requests.get('http://localhost:8000/recibemensaje?grupo='+chatter_name+'&emisor='+emisor+'&mensaje='+message)

            
        except:

            try:

                print 'Entre aqui'

                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']"
                )
                message = message_container.find_element_by_xpath(
                    ".//img[@class='_2DV1k QkfD1 selectable-text invisible-space copyable-text']"
                ).get_attribute("data-plain-text");


                print message



                

            except:

                print 'Sin exito'
                pass

    message = ''
    
    for messages in driver.find_elements_by_xpath("//div[@class='_3_7SH _3DFk6 message-in tail']"):
        
        time.sleep(3)

        try:
            message_container = messages.find_element_by_xpath(
                ".//div[@class='_3Usvm copyable-text']"
            )

            emisor = message_container.get_attribute("data-pre-plain-text")

            message = message_container.find_element_by_xpath(
                ".//span[@class='selectable-text invisible-space copyable-text']"
            ).text

            print 'tail 1 primera',emisor.encode('ascii', 'ignore').encode('ascii', 'replace')+' : '+message.encode('ascii', 'ignore').encode('ascii', 'replace')

            requests.get('http://localhost:8000/recibemensaje?grupo='+chatter_name+'&emisor='+emisor+'&mensaje='+message)

        
        except:

            try:

                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']"
                )

                emisor = message_container.get_attribute("data-pre-plain-text")


                message = message_container.find_element_by_xpath(
                    ".//img[@class='_2DV1k QkfD1 selectable-text invisible-space copyable-text']"
                ).get_attribute("data-plain-text");

                print 'tail 2 primera',emisor,message

                requests.get('http://localhost:8000/recibemensaje?grupo='+chatter_name+'&emisor='+emisor+'&mensaje='+message)


            except:

                print 'tail sin exito primera'
                pass

    message = ''

    for messages in driver.find_elements_by_xpath("//div[@class='_3_7SH _3DFk6 message-in tail']"):
        
        time.sleep(3)

        try:
            message_container = messages.find_element_by_xpath(
                ".//div[@class='copyable-text']"
            )

            emisor = message_container.get_attribute("data-pre-plain-text")

            message = message_container.find_element_by_xpath(
                ".//span[@class='selectable-text invisible-space copyable-text']"
            ).text

            print 'tail 1 segunda',emisor.encode('ascii', 'ignore').encode('ascii', 'replace')+' : '+message.encode('ascii', 'ignore').encode('ascii', 'replace')

            requests.get('http://localhost:8000/recibemensaje?grupo='+chatter_name+'&emisor='+emisor+'&mensaje='+message)

        
        except:

            try:

                

                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']"
                )

                emisor = message_container.get_attribute("data-pre-plain-text")


                message = message_container.find_element_by_xpath(
                    ".//img[@class='_2DV1k QkfD1 selectable-text invisible-space copyable-text']"
                ).get_attribute("data-plain-text");

                print 'tail 2 segunda',emisor,message

                requests.get('http://localhost:8000/recibemensaje?grupo='+chatter_name+'&emisor='+emisor+'&mensaje='+message)




                

            except:


                print 'tail sin exito segunda'
                pass

    return message


time.sleep(10)

print 'Procesando...'

previous_in_message = ''

#search_chatter(driver,'IT Soporte')


while True:

    time.sleep(10)

    for chatter in driver.find_elements_by_xpath("//div[@class='_2wP_Y']"):

        #try:


				
        chatter_name = chatter.find_element_by_xpath(".//span[@class='_1wjpf']").text

        print chatter_name

        print '-------'

        chatter.find_element_by_xpath(".//div[@tabindex='-1']").click()

        read_last_in_message(driver)

            

        # except:

        #     print 'No se pudo obtener el chatter'

        #     pass




# print c



# while True:


# 	_usuarios = requests.get('http://localhost:8000/listausuarios')


# 	print json.loads(_usuarios.text)

# 	for u in json.loads(_usuarios.text):

# 		usuario = u['nombre']

# 		contrasena= u['password']

# 		driver = webdriver.Chrome('/Users/xiencias/code/chromedriver')

# 		driver.get('https://www.globohq.com/users/sign_in');

# 		username = driver.find_element_by_id("user_email")

# 		password = driver.find_element_by_id("user_password")

# 		username.click();

# 		time.sleep(1)

# 		username.send_keys(usuario)

# 		password.click();

# 		print 'contrasena,,,',contrasena

# 		password.send_keys(contrasena)


# 		driver.find_element_by_name("commit").click();

# 		estado = driver.find_element_by_class_name('in-call-indicator-message')

# 		print usuario,estado.text,datetime.datetime.today()

# 		requests.get('http://localhost:8000/guarda/?usuario='+str(usuario)+'&estado='+str(estado.text))

# 		



# 		pass

#password.send_keys("Pa55worD")

#driver.find_element_by_name("submit").click()

#driver.findElement(By.id("user_email")).sendKeys("555-55-5555"); 

# elem = driver.find_element_by_partial_link_text('Mostrar n')

# elem.click()

# elem = driver.find_element_by_class_name('number')

# number = elem.text

#driver.close()