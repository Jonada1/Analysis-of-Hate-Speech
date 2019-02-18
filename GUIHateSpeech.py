import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from nltk.corpus import wordnet as wn
import re
from tkinter import *
import tkinter.messagebox
import nltk
import yaml
from nltk.corpus import wordnet as wn


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')
        self.chk_btn = QPushButton('Hate Words in The File')
        self.int_btn = QPushButton('Hate Intensity')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)
        h_layout.addWidget(self.chk_btn)
        h_layout.addWidget(self.int_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        #self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)
        self.chk_btn.clicked.connect(self.check_text)
        self.int_btn.clicked.connect(self.intensity_text)

        self.setLayout(v_layout)
        self.setWindowTitle('Hate Speech Recognition')

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

    def check_text(self):
        words = ['rotten', 'wicked', 'violence', 'censure', 'intimidate', 'prejudice',
                 'tense', 'dislike', 'disrespect']

        S = []
        synonyms = []
        hyponyms = []
        synonyms_of_hyponyms = []
        hyponyms_of_hyponyms = []
        SS = []

        # 1(i)(ii)
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
        abbreForSS = ['ACAB', 'AKIA', 'AYAK', 'FGRN', 'HFFH', 'HSN', 'ITSUB', 'KABARK', 'KIGY', 'KLASP', 'LOTIE',
                      'OFOF', 'ORION', 'RAHOWA', 'ROA', 'SS Bolts', 'SWP', 'USAS', 'WAR', 'WP', 'WPWW', 'ZOG']
        SS = S + abbreForSS
        #print(SS)

        class Word:
            def __init__(self, word, intensity):
                self.word = word
                self.intensity = intensity

        all_words_with_intensity = []

        high_intensity_words = ['rotten', 'wicked', 'violence']
        medium_intensity_words = ['censure', 'intimidate', 'prejudice']
        moderate_intensity_words = ['tense', 'dislike', 'disrespect']

        ## words in category 1 (high intensity hate speech words) will be assigned weight 5
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
        #   print(word.word, word.intensity)

        # 2.1
        filename = "BouncyKnickers.txt"
        infile = open(filename, 'r')
        lines = infile.readlines()
        hatearray = []
        for line in lines:
            for hate in SS:
                if re.search(r'\b%s\b' % hate, line):
                    #print(hate)
                    hatearray.append(hate)
        tkinter.messagebox.showinfo("Results", hatearray)

    def intensity_text(self):
        class Splitter(object):
            def __init__(self):
                self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
                self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

            def split(self, text):
                """
                input format: a paragraph of text
                output format: a list of lists of words.
                    e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
                """
                sentences = self.nltk_splitter.tokenize(text)
                tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
                return tokenized_sentences

        class POSTagger(object):
            def __init__(self):
                pass

            def pos_tag(self, sentences):
                """
                input format: list of lists of words
                    e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
                output format: list of lists of tagged tokens. Each tagged tokens has a
                form, a lemma, and a list of tags
                    e.g: [[('this', 'this', ['DT']), ('is', 'be', ['VB']), ('a', 'a', ['DT']), ('sentence', 'sentence', ['NN'])],
                            [('this', 'this', ['DT']), ('is', 'be', ['VB']), ('another', 'another', ['DT']), ('one', 'one', ['CARD'])]]
                """

                pos = [nltk.pos_tag(sentence) for sentence in sentences]
                # adapt format
                pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
                return pos

        filename1 = "hateSpeech.txt"
        infile = open(filename1, 'r')
        line1 = infile.readlines()
        for line2 in line1:
            text = line2
        # text = "Hate speech is speech that attacks a person or group on the basis of attributes such as race, religion, ethnic origin, national origin, sex, disability, sexual orientation, or gender identity. The law of some countries describes hate speech as speech, gesture or conduct, writing, or display that incites severe violence or prejudicial action against a protected group or individual on the basis of their membership of the group, or because it disparages or intimidates a protected group, or individual on the basis of their membership of the group. The law may identify a protected group by certain characteristics. In some countries, hate speech is not a legal term. Additionally in some countries, including the United States, hate speech is constitutionally protected. In some countries, a victim of hate speech may seek redress under civil law, criminal law, or both. A website that contains hate speech (online hate speech) may be called a hate site. Many of these sites contain Internet forums and news briefs that emphasize a particular viewpoint. There has been debate over freedom of speech, intense hate speech and extreme hate speech or moderate disgustful legislation. Regular slangs can be considered as negation of rage, less lousy or little intimidate."

        splitter = Splitter()
        postagger = POSTagger()

        splitted_sentences = splitter.split(text)

        # print(splitted_sentences)

        pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

        # print(pos_tagged_sentences)

        class DictionaryTagger(object):
            def __init__(self, dictionary_paths):
                files = [open(path, 'r') for path in dictionary_paths]
                dictionaries = [yaml.load(dict_file) for dict_file in files]
                map(lambda x: x.close(), files)
                self.dictionary = {}
                self.max_key_size = 0
                for curr_dict in dictionaries:
                    for key in curr_dict:
                        if key in self.dictionary:
                            self.dictionary[key].extend(curr_dict[key])
                        else:
                            self.dictionary[key] = curr_dict[key]
                            self.max_key_size = max(self.max_key_size, len(key))

            def tag(self, postagged_sentences):
                return [self.tag_sentence(sentence) for sentence in postagged_sentences]

            def tag_sentence(self, sentence, tag_with_lemmas=False):
                words = ['rotten', 'wicked', 'violence', 'censure', 'intimidate', 'prejudice',
                         'tense', 'dislike', 'disrespect']

                S = []
                synonyms = []
                hyponyms = []
                synonyms_of_hyponyms = []
                hyponyms_of_hyponyms = []
                SS = []

                # 1(i)(ii)
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
                abbreForSS = ['ACAB', 'AKIA', 'AYAK', 'FGRN', 'HFFH', 'HSN', 'ITSUB', 'KABARK', 'KIGY', 'KLASP',
                              'LOTIE',
                              'OFOF', 'ORION', 'RAHOWA', 'ROA', 'SS Bolts', 'SWP', 'USAS', 'WAR', 'WP', 'WPWW', 'ZOG']
                SS = S + abbreForSS

                """
                the result is only one tagging of all the possible ones.
                The resulting tagging is determined by these two priority rules:
                    - longest matches have higher priority
                    - search is made from left to right
                """
                tag_sentence = []
                N = len(sentence)
                if self.max_key_size == 0:
                    self.max_key_size = N
                i = 0
                while (i < N):
                    j = min(i + self.max_key_size, N)  # avoid overflow
                    tagged = False
                    while (j > i):
                        expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                        expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                        if tag_with_lemmas:
                            literal = expression_lemma
                        else:
                            literal = expression_form

                        if literal in self.dictionary:
                            #print(literal)
                            #tkinter.messagebox.showinfo("Results", literal)
                            filename = "hateSpeech.txt"
                            infile = open(filename, 'r')
                            lines = infile.readlines()
                            for line in lines:
                                list_of_words = line.split()
                                next_word = list_of_words[list_of_words.index(literal) + 1]
                                # print(next_word)
                                if next_word in SS:
                                    # for hate in SS:
                                    # if re.search(r'\b%s\b' % hate, next_word):
                                    # for hate in SS:
                                    #   if re.search(r'\b%s\b' % hate, line):
                                    # self.logger.debug("found: %s" % literal)
                                    is_single_token = j - i == 1
                                    original_position = i
                                    i = j
                                    taggings = [tag for tag in self.dictionary[literal]]
                                    tagged_expression = (expression_form, expression_lemma, taggings)
                                    if is_single_token:  # if the tagged literal is a single token, conserve its previous taggings:
                                        original_token_tagging = sentence[original_position][2]
                                        tagged_expression[2].extend(original_token_tagging)
                                    tag_sentence.append(tagged_expression)
                                    tagged = True
                                else:
                                    is_single_token = j - i == 1
                                    original_position = i
                                    i = j
                                    taggings = ['None']
                                    tagged_expression = (expression_form, expression_lemma, taggings)
                                    if is_single_token:  # if the tagged literal is a single token, conserve its previous taggings:
                                        original_token_tagging = sentence[original_position][2]
                                        tagged_expression[2].extend(original_token_tagging)
                                    tag_sentence.append(tagged_expression)
                                    tagged = True

                        else:
                            j = j - 1
                    if not tagged:
                        tag_sentence.append(sentence[i])
                        i += 1
                return tag_sentence

        dicttagger = DictionaryTagger(['positive.yml', 'negative.yml'])

        dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

        #print(dict_tagged_sentences)

        def value_of(sentiment):
            if sentiment == 'negLow': return -1
            if sentiment == 'negMedium': return -2
            if sentiment == 'negHigh': return -3
            if sentiment == 'posLow': return 1
            if sentiment == 'posMedium': return 2
            if sentiment == 'posHigh': return 3
            if sentiment == 'None': return 0
            return 0

        def sentiment_score(review):
            return sum([value_of(tag) for sentence in dict_tagged_sentences for token in sentence for tag in token[2]])

        #print(sentiment_score(dict_tagged_sentences))
        tkinter.messagebox.showinfo("Results", sentiment_score(dict_tagged_sentences))

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())