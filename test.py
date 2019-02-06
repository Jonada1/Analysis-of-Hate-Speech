 	
import nltk
from nltk.corpus import wordnet as wn
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize



sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
text = "this is a simple text"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
sent_tokenize_list = word_tokenize(text)
print(result)
print(sent_tokenize_list)
result.draw()

text = word_tokenize("And now for something completely different")
test = nltk.pos_tag(text)
print("test", test)

