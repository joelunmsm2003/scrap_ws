from bs4 import BeautifulSoup

import requests

n=1
for n in range(0,100):

	print 'NNNNNN:',n


	if n==0:

		r  = requests.get("https://www.locanto.com.pe/Mujer-busca-hombre/20702/")

	else:

		r  = requests.get("https://www.locanto.com.pe/Mujer-busca-hombre/20702/"+str(n))

	data = r.text

	soup = BeautifulSoup(data)

	for link in soup.find_all('a', class_='bp_ad__link'):
	    
		url = link.get('href')



		x = requests.get(url)

		datax = x.text

		soupx = BeautifulSoup(datax)


		for ddd in soupx.find_all('a', class_='logo_link'):

			distrito = ddd.get('href')

		for linkx in soupx.find_all('div', class_='user_content'):

			contenido = str(linkx)

			contenido = contenido.replace('<div class="user_content" id="js-user_content" itemprop="description">','').replace('<br>','').replace('<br/>','').replace('  ','').replace('<div>','').replace('</div>','')


		print distrito.lower()

		if 'lima' in distrito.lower():

			cc = requests.post('http://mylookxpressapp.com:2000/guardaurl', data = {'url':url,'contenido':contenido})

			print cc
		

