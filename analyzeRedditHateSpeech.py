import nltk
import praw
import csv
from nltk.corpus import wordnet as wn
import re
from ProgramIntensity import *

def get_subreddit_comments_sentence_array(subredditName):
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                        client_id='hH4pioFdIqPqTg', client_secret="U4Xu1kraO2HdF8Xr5xLhNPHA8cA")
    subreddit = reddit.subreddit(subredditName)
    commentArray = []
    sentences = []
    for submission in subreddit.hot(limit=10): #read submissions
        comments = submission.comments
        for comment in comments:
            if(hasattr(comment,"body")): # If has body read
                # splitter = Treebank.Splitter()
                sentence = comment.body
                # sentence = Treebank.POSTagger().pos_tag(sentence)
                sentences.append(sentence)
                
    return sentences
def get_subreddit_comments_word_array(subredditName):
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                        client_id='hH4pioFdIqPqTg', client_secret="U4Xu1kraO2HdF8Xr5xLhNPHA8cA")
    subreddit = reddit.subreddit(subredditName)
    commentArray = []
    words = []
    for submission in subreddit.hot(limit=50): #read submissions
        comments = submission.comments
        for comment in comments:
            if(hasattr(comment,"body")): # If has body read
                sent_text = nltk.sent_tokenize(comment.body)
                for sentence in sent_text:
                    sentenceWords = nltk.word_tokenize(sentence)
                    for word in sentenceWords:
                        words.append(word)
    return words

# Find hate words among comments based on the category of intensity & return comment
def find_hate_word(text):
    hWords = list(map(lambda hWord: hWord, high_intensity_words))
    results = []
    for word in text:
        if (word in hWords):
            results.append(text)
    return results

def findTotalIntensity(words):
    total_intensity = 0
    for word in words:
        intensity = list(map(lambda y: y.intensity, filter(lambda x: x.word == word, all_words_with_intensity)))[0]
        total_intensity += intensity
    return total_intensity

        
# ************** askmen ******************* 
askmenwords = get_subreddit_comments_word_array("askmen")
menHateWords = find_hate_word(askmenwords)
print(menHateWords)
menTotalIntensity = findTotalIntensity(menHateWords)


# ************** askwomen *******************
askwomenwords = get_subreddit_comments_word_array("askwomen")
womenHateWords = find_hate_word(askwomenwords)
womanTotalIntensity = findTotalIntensity(womenHateWords)

# **** teenagers between 13 to 19 years old*******
teenagers = get_subreddit_comments_word_array("teenagers")
teenagerHateWords = find_hate_word(teenagers)
teenagersTotalIntensity = findTotalIntensity(teenagerHateWords)


# ************** Professional reddit*******************
ITdept = get_subreddit_comments_word_array("ITdept")
ITdeptHateWords = find_hate_word(ITdept)
ITdeptTotalIntensity = findTotalIntensity(ITdeptHateWords)


# ************** elderly *******************
elder = get_subreddit_comments_word_array("1920s")
elderHateWords = find_hate_word(elder)
elderTotalIntensity = findTotalIntensity(elderHateWords)

