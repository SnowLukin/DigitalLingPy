from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

def task1_lab1():
    print(sent_tokenize(text))

def task2_lab1():
    print(word_tokenize(text))

def task4_lab1():
    print(stopwords.words('russian'))

def task5_lab1():
    stop_words = set(stopwords.words('russian'))
    words = word_tokenize(text)
    without_stop_words = [word for word in words if not(word in stop_words)]
    print(without_stop_words)

def graph_analizator():
    task1_lab1()
    task2_lab1()
    task5_lab1()

# graph_analizator()