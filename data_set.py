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

def find_hyponyms(words):
    direct_synonyms = []
    direct_hyponyms = []
    second_hyponyms = []
    synonyms_of_hyponyms = []
    synonyms_of_second_hyponyms = []
    for word in words:
        for synset in wn.synsets(word):
            ## First synonyms
            for lemma in synset.lemmas():
                synonym = lemma.name()
                direct_synonyms.append(synonym)
            ## their direct hyponyms
            i = 0
            for hyponym in synset.hyponyms():
                if (i == 0):
                    for hyponym_lemma in hyponym.lemmas():
                        hyponym = hyponym_lemma.name()
                        direct_hyponyms.append(hyponym)
                        ## synonyms of hyponyms
                        for hyponym_synset in wn.synsets(hyponym):
                            for synset_lemma in hyponym_synset.lemmas():
                                synonym_of_hyponyms = synset_lemma.name()
                                synonyms_of_hyponyms.append(synonym_of_hyponyms)
                            
            ## the second hyponyms  
                if (i == 1):
                    for hyponym_lemma in hyponym.lemmas():
                        second_hyponym = hyponym_lemma.name()
                        second_hyponyms.append(second_hyponym)
                        ## synonyms of second hyponyms
                        for hyponym_synset in wn.synsets(second_hyponym):
                            for synset_lemma in hyponym_synset.lemmas():
                                synonym_of_second_hyponyms = synset_lemma.name()
                                synonyms_of_second_hyponyms.append(synonym_of_second_hyponyms)
                i += 1

            ## First hyponyms
        # print('Word ', word, 'has ', len(direct_synonyms), ' direct synonyms')
        # print('Word ', word, 'has ', len(direct_hyponyms), ' direct hyponyms')
        # print('Word ', word, 'has ', len(second_hyponyms), ' second hyponyms')
        # print('Word ', word, 'has ', len(synonyms_of_hyponyms), ' synonyms of direct hyponyms')
        # print('Word ', word, 'has ', len(synonyms_of_second_hyponyms), ' synonyms of second hyponyms')




# find_hyponyms(moderate_intensity_words)
