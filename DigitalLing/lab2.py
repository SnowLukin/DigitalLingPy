from pymorphy2 import MorphAnalyzer

text = ""
file = open("SampleText.txt", "r")
each_line = file.readlines()
for line in each_line:
    text += line
file.close()

def task1_lab2():
    morph = MorphAnalyzer()
    words = word_tokenize(text)
    for word in words:
        print(morph.parse(word))

# task1_lab2()

def task2_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.normal_form)
        print(p.normalized)

# task2_lab2()

def task3_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.tag)

# task3_lab2()

def task5_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print('VERB' in p.tag)
        print('NOUN' in p.tag)
        # print({'plut', 'past'} in p.tag)
        print({'NOUN', 'plur'} in p.tag)

# task5_lab2()

def task6_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.tag.POS)
        print(p.tag.animacy)
        print(p.tag.aspect)
        print(p.tag.case)
        print(p.tag.gender)
        print(p.tag.involvement)
        print(p.tag.mood)
        print(p.tag.number)
        print(p.tag.person)
        print(p.tag.tense)
        print(p.tag.transitivity)
        print(p.tag.voice)

# task6_lab2()

def task7_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print('foobar' in p.tag)
        print({'NOUN', 'foo', 'bar'} in p.tag)


def task8_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.tag.POS == 'plur')


def task10_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.inflect({'gent'}))
        print(p.inflect({'plur', 'gent'}))

# task10_lab2()

def task11_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.lexeme)

# task11_lab2()

def task12_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.normal_form)

# task12_lab2()
def task13_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.inflect({'sing', 'nomn'}).word)


def task14_lab2():
    words = word_tokenize(text)
    morph = MorphAnalyzer()
    for word in words:
        p = morph.parse(word)[0]
        print(p.make_agree_with_number(1).word)
        print(p.make_agree_with_number(2).word)
        print(p.make_agree_with_number(3).word)

# task14_lab2()
def morph_analizator():
    task1_lab2()
    task2_lab2()
    task3_lab2()
    task5_lab2()
    task6_lab2()
    task10_lab2()
    task11_lab2()
    task12_lab2()
    task14_lab2()