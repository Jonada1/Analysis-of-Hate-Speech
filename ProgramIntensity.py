import csv
from nltk.corpus import wordnet as wn
import re

class Word:
    def __init__(self, word, intensity):
        self.word = word
        self.intensity = intensity



high_intensity_words = ['trash', 'nazi', 'kill',]
medium_intensity_words = ['nerd', 'detest', 'prejudice']
moderate_intensity_words = ['tense', 'dislike', 'disrespect']

## words in category 1 (high intensity hate speech words) will be assigned weight 5
def get_all_words_with_intensity():
    all_words_with_intensity = []
    for word in high_intensity_words:
        a = Word(word, 5)
        all_words_with_intensity.append(a)
        ## their synonyms will be assigned weight 5 as well
        for synset in wn.synsets(word):
            for lemma in synset.lemmas():
                b = Word(lemma.name(), 5)
                all_words_with_intensity.append(b)
            ## their direct hyponyms will be assigned weight 4.7 (as well as their synonyms)
            i = 0
            for hyponym in synset.hyponyms():
                if (i == 0):
                    for hyponym_lemma in hyponym.lemmas():
                        c = Word(hyponym_lemma.name(), 4.7)
                        all_words_with_intensity.append(c)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                d = Word(synset_lemma.name(), 4.7)
                                all_words_with_intensity.append(d)
            ## the second hyponyms will be assigned weight 4.5. Etc. 
                if (i == 1):
                    for hyponym_lemma in hyponym.lemmas():
                        e = Word(hyponym_lemma.name(), 4.5)
                        all_words_with_intensity.append(e)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                f = Word(synset_lemma.name(), 4.5)
                                all_words_with_intensity.append(f)
                i += 1


    ## words belonging to Category 2 (medium hate speech) will be assigned 4,
    ## and reduce by 0.2 and 0.3 as in previous case for direct and second hyponyms if any
    for word in medium_intensity_words:
        a = Word(word, 4)
        all_words_with_intensity.append(a)
        for synset in wn.synsets(word):
            for lemma in synset.lemmas():
                b = Word(lemma.name(), 4)
                all_words_with_intensity.append(b)
            i = 0
            for hyponym in synset.hyponyms():
                if (i == 0):
                    for hyponym_lemma in hyponym.lemmas():
                        c = Word(hyponym_lemma.name(), 3.7)
                        all_words_with_intensity.append(c)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                d = Word(synset_lemma.name(), 3.7)
                                all_words_with_intensity.append(d)
                if (i == 1):
                    for hyponym_lemma in hyponym.lemmas():
                        e = Word(hyponym_lemma.name(), 3.5)
                        all_words_with_intensity.append(e)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                f = Word(synset_lemma.name(), 3.5)
                                all_words_with_intensity.append(f)
                i += 1
                

    ## words of Category 3 (moderate hate speech) will be assigned weight 3
    for word in moderate_intensity_words:
        a = Word(word, 3)
        all_words_with_intensity.append(a)
        for synset in wn.synsets(word):
            for lemma in synset.lemmas():
                b = Word(lemma.name(), 3)
                all_words_with_intensity.append(b)
            i = 0
            for hyponym in synset.hyponyms():
                if (i == 0):
                    for hyponym_lemma in hyponym.lemmas():
                        c = Word(hyponym_lemma.name(), 2.7)
                        all_words_with_intensity.append(c)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                d = Word(synset_lemma.name(), 2.7)
                                all_words_with_intensity.append(d)
                if (i == 1):
                    for hyponym_lemma in hyponym.lemmas():
                        e = Word(hyponym_lemma.name(), 2.5)
                        all_words_with_intensity.append(e)
                        for hyponym_synset in wn.synsets(hyponym_lemma.name()):
                            for synset_lemma in hyponym_synset.lemmas():
                                f = Word(synset_lemma.name(), 2.5)
                                all_words_with_intensity.append(f)
                i += 1
    # for word in all_words_with_intensity:
    #     print (word.word, word.intensity)

    return all_words_with_intensity

    
# get_all_words_with_intensity()

