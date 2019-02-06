import csv
from nltk.corpus import wordnet as wn
import re

words = ['rotten', 'wicked', 'violence', 'censure', 'intimidate', 'prejudice',
         'tense', 'dislike', 'disrespect']

S = []
synonyms = []
hyponyms = []
synonyms_of_hyponyms = []
hyponyms_of_hyponyms = []
SS = []

for word in words: 
    for synset in wn.synsets(word):
##        print (synset, "for ", word)
        for lemma in synset.lemmas():
##            print (lemma, "for ", synset)
            synonyms.append(lemma.name())
        for hyponym in synset.hyponyms()[:2]:
            for hyponym_lemma in hyponym.lemmas():
                hyponyms.append(hyponym_lemma.name())

for word in hyponyms: 
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms_of_hyponyms.append(lemma.name())
        for hyponym in synset.hyponyms()[:2]:
            for hyponym_lemma in hyponym.lemmas():
                hyponyms_of_hyponyms.append(hyponym_lemma.name())

S = words + synonyms + hyponyms + synonyms_of_hyponyms + hyponyms_of_hyponyms
abbreForSS = ['ACAB', 'AKIA', 'AYAK', 'FGRN', 'HFFH', 'HSN', 'ITSUB', 'KABARK', 'KIGY', 'KLASP', 'LOTIE', 'OFOF', 'ORION', 'RAHOWA', 'ROA', 'SS Bolts', 'SWP', 'USAS', 'WAR', 'WP', 'WPWW', 'ZOG']
SS = S + abbreForSS
print(SS)

#with open("hateSpeech.txt", "r") as hateFile:
    #hate = input("Enter: ")
    #for hate in SS:
        #hateFileReader = csv.reader(hateFile)
        #for row in hateFileReader:
            #for field in row:
                #if field == hate:
                 #   print(field)
    #hateFile.close()

filename = "hateSpeech.txt"
infile = open(filename, 'r')
lines = infile.readlines()
for line in lines:
    for hate in SS:
        if re.search(r'\b%s\b' % hate, line):
            print(hate)







