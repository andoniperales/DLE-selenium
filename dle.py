#!/usr/bin/python

import os
from fake_headers import Headers
from selenium.webdriver import Firefox as firefox, FirefoxOptions as Options
from selenium.webdriver.common.by import By

def definicion(term):
	# Generate fake user-agent (the site rejects headless operations otherwise)
	header = Headers(
		browser="firefox",
		os="win",
		headers=False
	)
	
	UA = header.generate()['User-Agent']
	
	# Set webdriver options 
	options = Options()
	options_list = [
		f'user-agent={UA}', 
		'--headless', 
		'--disable-gpu', 
		'--allow-running-insecure-content'
	]

	for parameter in options_list:
		options.add_argument(f"{parameter}")

	# Get & print term's information
	with firefox(options=options) as driver:
		driver.implicitly_wait(5)
		driver.get(f"https://dle.rae.es/{term}")
		resultados = driver.find_element(By.TAG_NAME, "article").text
		return resultados	
		driver.quit()

if __name__ == '__main__':
	term = input('Search for a term\n')
	os.system('clear')
	print(definicion(term))
