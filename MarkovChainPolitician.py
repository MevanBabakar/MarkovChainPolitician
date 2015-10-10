# 1. Be able to open a text file, and split it into a list of words. 
# e.g.["The", "quick", "brown", "fox", "jumped", "over" ...]

sentence = "this is a string hello my name is mevan I am making a thing"
words = sentence.split()

print words

# 2. Be able to split this into a list of triples starting at each word in the text, 
# e.g. [("The", "quick", "brown"), ("quick", "brown", "fox"), ("brown", "fox", "jumped") ...]

print len(words)

triples = []
for i in range(len(words)-2):
	triples.append((words[i], words[i+1], words[i+2]))

print triples