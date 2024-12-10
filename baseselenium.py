#!/usr/bin/python

from fake_headers import Headers
from selenium.webdriver import Firefox as firefox, FirefoxOptions as Options

def fakeit():
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

	driver = firefox(options=options) 
	return driver
