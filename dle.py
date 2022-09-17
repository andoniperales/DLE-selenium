#!/usr/bin/python

from sys import argv
from fake_headers import Headers
from selenium.webdriver import Chrome as chrome, ChromeOptions as Options
from selenium.webdriver.common.by import By


def main(entrada):	
    # Generate fake user-agent (the site rejects headless operations otherwise)

    header = Headers(
        browser="chrome",
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
        options.add_argument(parameter)

# Get & print term's information
    
    with chrome(options=options) as driver:
        driver.implicitly_wait(5)
        driver.get(f"https://dle.rae.es/{entrada}")
        definicion = driver.find_element(By.CSS_SELECTOR, "div#resultados")	
        print(definicion.text)  

def definicion(palabra):
        main(palabra)

if __name__ == '__main__':
    entrada = argv[1]
    main(entrada)
