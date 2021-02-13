import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    file1 = "words.txt"
    word = open(file1,'r')
    line = word.readline()
    word_list = line.split()
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
    