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
from analyzeRedditHateSpeech import *
from redditTreebank import frequentEntityOfHate, treebankAnalyzis


class Intensity(QWidget):

    def __init__(self):
        super(Intensity, self).__init__()
        self.text = QTextEdit(self)
        self.subreddit1_btn = QPushButton('Ask men')
        self.subreddit2_btn = QPushButton('Ask women')
        self.subreddit3_btn = QPushButton('Teenagers')
        self.subreddit4_btn = QPushButton('ITdept')
        self.subreddit5_btn = QPushButton('1920s')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.subreddit1_btn)
        h_layout.addWidget(self.subreddit2_btn)
        h_layout.addWidget(self.subreddit3_btn)
        h_layout.addWidget(self.subreddit4_btn)
        h_layout.addWidget(self.subreddit5_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.subreddit1_btn.clicked.connect(self.intensity_group1)
        #self.clr_btn.clicked.connect(self.clear_text)
        self.subreddit2_btn.clicked.connect(self.intensity_group2)
        self.subreddit3_btn.clicked.connect(self.intensity_group3)
        self.subreddit4_btn.clicked.connect(self.intensity_group4)
        self.subreddit5_btn.clicked.connect(self.intensity_group5)

        self.setLayout(v_layout)
        self.setWindowTitle('Hate Speech Recognition of reddit.com')
        
        self.show()

    def intensity_group1(self):
        self.text.clear()
        message = "Total intensity of hate speech: " + str(menTotalIntensity) + " \nMost used hate word is: " + frequentEntityOfHate('askmen') + '(' + wordType + ')'
        tkinter.messagebox.showinfo("Ask Man hate intensity", message)
    def intensity_group2(self):
        self.text.clear()
        message = "Total intensity of hate speech: " + str(womanTotalIntensity) + " \nMost used hate word is: " + frequentEntityOfHate('askwomen')
        tkinter.messagebox.showinfo("Ask Woman hate intensity", message)
    def intensity_group3(self):
        self.text.clear()
        message = "Total intensity of hate speech: " + str(teenagersTotalIntensity) + " \nMost used hate word is: " + frequentEntityOfHate('teenagers')
        tkinter.messagebox.showinfo("Teenagers hate intensity", message)
    def intensity_group4(self):
        self.text.clear()
        message = "Total intensity of hate speech: " + str(ITdeptTotalIntensity) + " \nMost used hate word is: " + frequentEntityOfHate('ITdept')
        tkinter.messagebox.showinfo("ITdept hate intensity", message)
    def intensity_group5(self):
        self.text.clear()
        message = "Total intensity of hate speech: " + str(elderTotalIntensity) + " \nMost used hate word is: " + frequentEntityOfHate('1920s')
        tkinter.messagebox.showinfo("1920s hate intensity", message)

    
app = QApplication(sys.argv)
writer = Intensity()
sys.exit(app.exec_())