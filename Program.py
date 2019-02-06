from nltk.corpus import wordnet as wn

words = ['rotten', 'wicked', 'violence', 'censure', 'intimidate', 'prejudice',
         'tense', 'dislike', 'disrespect']

S = []
synonyms = []
hyponyms = []
synonyms_of_hyponyms = []
hyponyms_of_hyponyms = []

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
        
        
        
