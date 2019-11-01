import requests 
from bs4 import BeautifulSoup 
 

def get_wesbos_dad_jokes():
	URL = "https://raw.githubusercontent.com/wesbos/dad-jokes/master/readme.md"
	r = requests.get(URL) 
	  
	soup = BeautifulSoup(r.content,"html.parser") 
	unformatted_jokes = str(soup)

	unformatted_list = unformatted_jokes.split('---')[2:-2]
	dad_jokes = [jokes.strip() for jokes in unformatted_list]
	return dad_jokes