import analyzeRedditHateSpeech
from nltk.corpus import treebank
import nltk
import Treebank

class Frequency:
    # The class constructor
    def __init__(self, freq, count):
        self.word = freq
        self.count = count

def create_Object(freq, count):
    frequency = Frequency(freq, count)
    return frequency

def findMostFrequentWordInArray(wordArray):
    frequencies = []
    for word in wordArray:
        if(len(frequencies)==0):
            newFreq  = Frequency(word, 1)
            frequencies.append(newFreq)
        else:    
            found = False
            for freq in frequencies:
                if(freq.word == word):
                    freq.count += 1
                    found = True
                    break
            if(found == False):
                newFreq = Frequency(word, 1)
                frequencies.append(newFreq)
    if(len(frequencies)>0):
        highestCount = 0
        freqToReturn = ""
        for freq in frequencies:
            if(freq.count > highestCount):
                freqToReturn = freq.word
                highestCount = freq.count
        return freqToReturn
    else:
        return None    
    

def frequentEntityOfHate(subreddit):
    comments_word_array = analyzeRedditHateSpeech.get_subreddit_comments_word_array(subreddit)
    hateWords = analyzeRedditHateSpeech.find_hate_word(comments_word_array)
    mostFreqWord = findMostFrequentWordInArray(hateWords) 
    print(nltk.pos_tag(mostFreqWord))
    return mostFreqWord
def treebankAnalyzis(subreddit):
    comments_word_array = analyzeRedditHateSpeech.get_subreddit_comments_word_array(subreddit)
    hateWords = analyzeRedditHateSpeech.find_hate_word(comments_word_array)
    mostFreqWord = findMostFrequentWordInArray(hateWords) 
    senteceTags = analyzeRedditHateSpeech.get_subreddit_comments_sentence_array(subreddit)
    usages = []
    for sentences in senteceTags:
        for sentence in sentences:
            for word in sentence:
                if(word[0] == mostFreqWord):
                    wordType = word[2][0]
                    usages.append(wordType)
    print(usages)
    return usages
treebankAnalyzis("askwomen")

