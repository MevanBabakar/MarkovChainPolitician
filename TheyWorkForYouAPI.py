# 1. Get API response in JSON and find the politicians ID number
# 2. Requests speeches, based off ID.
# 3. Pull out text from speech and remove crap


import requests #apparently its the norm to have all your imports at the top
import json
from bs4 import BeautifulSoup 

#import pprint
#pp = pprint.PrettyPrinter(indent=4) #this is an object which can print things in a certain format. I find it incredibly helpful for dictionaries in lists in dictionaries in lists in lists, yadda yadda, ad infinitum.

api_key = "DaCH8NFRonboA2SvJDAtqw6b" #requested this from TheyWorkForYou

def get_speeches(name):
	response = requests.get('http://www.theyworkforyou.com/api/getMPs?search={}&output=js&key={}'.format(name, api_key)) #this replaces {} with all the variables named at the end, does it first come first served.
	dictionary_data = json.loads(response.text) # json loads takes a json string and turns it into python objects, in this case a list. Get requests bring back status codes, and text. You need to identify which hence response.text
	person_id = dictionary_data[0]['person_id'] 
	speeches = []
	for page_number in range(10): # assigns page_number a number from 1 to 20, which is then input into the line below
		response = requests.get('http://www.theyworkforyou.com/api/getDebates?type=commons&person={}&output=js&key={}&page={}'.format(person_id, api_key,page_number))
		debates = json.loads(response.text.encode('utf-8')) # got a unicode error, .encode magically fixed that somehow, I'm not asking questions, merely accepting gratefully. 
		for row in debates['rows']: #the[0] is accounted for in the "row" in debates['rows']
			soup = BeautifulSoup(row['body'], 'html.parser') # this gets rid of any HTML and returns the text, huzzah for BeautifulSoup
			speeches.append(soup.get_text().encode('utf-8'))
	all_sentences = " ".join(speeches) # joins all the entires in a list by whatever you put in the first string. In this instance a space. 
	return all_sentences

