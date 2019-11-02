import requests 
import cachetools.func
from bs4 import BeautifulSoup 
 

def get_wesbos_dad_jokes():
	URL = "https://raw.githubusercontent.com/wesbos/dad-jokes/master/readme.md"
	r = requests.get(URL) 
	  
	soup = BeautifulSoup(r.content,"html.parser") 
	unformatted_jokes = str(soup)

	unformatted_list = unformatted_jokes.split('---')[2:-2]
	dad_jokes = [jokes.strip() for jokes in unformatted_list]
	return dad_jokes


def get_icanhazdadjoke():
	dad_jokes = []
	for i in range(0,4):
	    request_sum_jokes = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
	    json_joke = request_sum_jokes.json();
	    dad_jokes.append(json_joke['joke'])
	return dad_jokes



@cachetools.func.ttl_cache(maxsize=128, ttl=3600)
def get_post_reddit(subreddit):
    try:
        params = (('limit', '10'),)
        response = requests.get('https://www.reddit.com/r/{}/top/.json'.format(subreddit), params=params)
        p = response.json()
        dadjokes = [value['data']['title'] + '\n' + value['data']['selftext']
         for value in p['data']['children']]
        return dadjokes
    except KeyError:
        return get_post_reddit(subreddit)