from TheyWorkForYouAPI import get_speeches
#import TheyWorkForYouAPI - if you import this way you would use sentence = TheyWorkForYouAPI.get_speeches

# 1. Be able to open a text file, and split it into a list of words.   e.g.["The", "quick", "brown", "fox", "jumped", "over" ...]

print "Which politician would you like to search for?"
sentence = get_speeches(raw_input())

words = sentence.split()

# 2. Be able to split this into a list of triples starting at each word in the text,  e.g. [("The", "quick", "brown"), ("quick", "brown", "fox"), ("brown", "fox", "jumped") ...]

triples = []
for i in range(len(words)-2): # added -2 to length so that the for loop wouldn't freak out at the last two entries in words
	triples.append((words[i], words[i+1], words[i+2]))


# 3. Be able to create a dictionary using these triples, with the first two items as the "key", and all the different possible third items as the "value".

dictionary = {}

for triple in triples:
	key = (triple[0], triple[1])
	if key in dictionary:  
		dictionary[key].append(triple[2])  #this is for the case when multiple values per key e.g. my name: is, was
	else:
		dictionary[key] = [triple[2]] #otherwise if a value doesnt exist, make one

# 4. Given a list of two words to start the sentence off (e.g. ["brown", "fox"]) find the list of words from dictionary (e.g [" jumps", "who", "who"]), and choose one at random and add it to the sentence (e.g. ["brown", "fox", "who"])
# 5. Then take the last two words (["fox", "who"]) and do the same thing again (look up word list, pick random one, add to the end)/

import random

make_sentence = random.choice(dictionary.keys()) # to start off the sentence we randomly pick a key
list_sentence = list(make_sentence) # makes these a list so things can be appended

for i in range(20): #range here defines how long the sentence is 
	list_sentence.append(random.choice(dictionary[list_sentence[-2], list_sentence[-1]]))
print " ".join(list_sentence)

