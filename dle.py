#!/usr/bin/python

from sys import argv
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():	
	# Generate fake user-agent (the site rejects headless operations otherwise)
	
	header = Headers(
		browser="chrome",
		os="win",
		headers=False
	)
	
	UA = header.generate()['User-Agent']
	
	# Set webdriver options 
	
	opt = webdriver.ChromeOptions()
	opt_list = [
		f'user-agent={UA}', 
		'--headless', 
		'--disable-gpu', 
		'--allow-running-insecure-content'
	]
	for o in opt_list:
		opt.add_argument(f"{o}")
	driver = webdriver.Chrome(options=opt)
	driver.implicitly_wait(5)

	# Get & print term's information
	
	entrada = argv[1]
	driver.get(f"https://dle.rae.es/{entrada}")
	definicion = driver.find_element(By.CSS_SELECTOR, "div#resultados")	
	print(definicion.text)

	driver.quit()

if __name__ == '__main__':
	main()
