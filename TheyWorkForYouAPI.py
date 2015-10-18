# 1. Get API response in JSON and find the politicians ID number
# 2. Requests speeches, based off ID.
# 3. Pull out text from speech and remove crap


import requests
import json
from bs4 import BeautifulSoup 

#import pprint
#pp = pprint.PrettyPrinter(indent=4)

api_key = "DaCH8NFRonboA2SvJDAtqw6b"

def get_speeches(name):
	response = requests.get('http://www.theyworkforyou.com/api/getMPs?search={}&output=js&key={}'.format(name, api_key))
	dictionary_data = json.loads(response.text)
	person_id = dictionary_data[0]['person_id']
	response = requests.get('http://www.theyworkforyou.com/api/getDebates?type=commons&person={}&output=js&key={}'.format(person_id, api_key))
	debates = json.loads(response.text.encode('utf-8')) #json loads makes the string a..not string, a python list
	speeches = []
	for row in debates['rows']: #the[0] is accounted for in the "row" in debates['rows']
		soup = BeautifulSoup(row['body'], 'html.parser')
		speeches.append(soup.get_text().encode('utf-8'))
	all_sentences = " ".join(speeches) # joins all the entires in a list by whatever you put in the first string. In this instance a space. 
	return all_sentences

