#!/usr/bin/python

import os, re
import baseselenium
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def definicion(term):
	driver = baseselenium.fakeit()
	
	# Get & print term's information
	try:
		driver.implicitly_wait(5)
		driver.get(f"https://dle.rae.es/{term}")
		resultados = driver.find_element(By.TAG_NAME, "article").text
	except NoSuchElementException as error:
		print("Term doesn't exist. Looking for similar ones...")
		try:
			driver.implicitly_wait(5)
			driver.find_element(By.CLASS_NAME, "n1")
		except NoSuchElementException as error:
			print("There are no similar terms. Exiting...")
			driver.quit()
		else:
			similar_terms = [re.search(r"\w+", word.text).group(0) for word in driver.find_elements(By.CLASS_NAME, "n1")]
			if len(similar_terms) == 1:
				print(f"There's one similar term: \"{similar_terms[0]}\"")
				choice = input("Do you want to check its definition? (y/n)\n")
				if "y" in choice:
					definicion(f"{similar_terms[0]}")
					driver.quit()
				else:
					driver.quit()
			else:
				print("Choose a similar term:")
				for n in range(len(similar_terms)):
					print(f"{n+1} {similar_terms[n]}")
				choice = input("")
				definicion(f"{similar_terms[int(choice) - 1]}")
	else:
		print(resultados)
		driver.quit()

if __name__ == '__main__':
	term = input('Search for a term\n')
	definicion(term)
