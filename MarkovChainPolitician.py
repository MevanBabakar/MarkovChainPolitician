# 1. Be able to open a text file, and split it into a list of words.   e.g.["The", "quick", "brown", "fox", "jumped", "over" ...]

sentence = """I said on the steps of Downing Street on May 8 that this would be a 'one nation' government, with working people at its heart. In its simplest terms, that means if you want to work hard and get on in life, this government will be on your side.

Whoever you are, wherever you live, whatever your background, whatever stage of life you are at, I believe this government can help you fulfil your aspirations. And let me be clear, when I say whoever you are, I mean it.

Whether you voted for me or campaigned against me; whether you are middle income or low paid or not in work at all, whether you live in a leafy suburb or an inner-city community, this government wants to extend opportunity, and what in the election campaign I called a good life, for all. That for me is the 'one nation' ideal.

We have taken great strides towards this in the past 5 years. Two million more people in work. Wages rising. More children in good or outstanding schools than ever before. And yet, for all the progress we have made, there are still far too many people in our country unable to reach their potential.

When less than 1 in 10 children in residential care get 5 good GCSEs and when more than 1.5 million children are still living in households where no-one works, I won't sit back and think the job is done. Far from it. I want everyone in this country to have the opportunity to get on and make a good life for themselves. That is the task for the next 5 years.

And today, I want to set out how we will achieve it.

Long-term economic plan
It starts, quite simply, by continuing to work through our long-term economic plan. Line one, rule one, of any plan to extend opportunity is to ensure a strong economy. And a secure and strong economy means getting the deficit down.

I know there are those who think that this is somehow not progressive. But let me tell you this. There's nothing progressive about asking the next generation to pay off the debts we couldn't be bothered to deal with; nothing progressive about robbing from our children. There's nothing progressive about paying more in debt interest than we spend on our schools.

Make no mistake, if we're running unsustainable deficits, and interest rates are going through the roof it's working people and children in the poorest families who will suffer the most. If taxes are high, and businesses are firing rather than hiring, make no mistake, it's working people and their children who will lose out first.

So yes, we will finish the job of the turning the economy around and doing what I call the bread and butter of good government, competently running the economy, offering people the security they need to get on in their lives.

And that is the first step in improving the life chances of everyone in our country."""


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

for i in range(15): #range here defines how long the sentence is 
	list_sentence.append(random.choice(dictionary[list_sentence[-2], list_sentence[-1]]))
print list_sentence 

