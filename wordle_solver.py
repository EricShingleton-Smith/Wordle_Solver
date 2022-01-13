from datetime import date
import random
import pandas as pd
import json
import os
import requests

class Wordle:
    '''Help solve the wordle game'''

    def __init__(self):
        self.date = date.today()
        self.mc_letter = {
            'E': .111607,
            'A': .84966,
            'R': .75809,
            'I': .75448,
            'O': .71635,
            'T': .69509,
            'N': .66544,
            'S': .57351,
            'L': .54893,
            'C': .45388,
            'U': .36308,
            'D': .33844,
            'P': .31671,
            'M': .30129,
            'H': .30034,
            'G': .24705,
            'B': .20720,
            'F': .18121,
            'Y': .17779,
            'W': .12899,
            'K': .11016,
            'V': .10074,
            'X': .2902,
            'Z': .2722,
            'J': .1965,
            'Q': .1962
        }
        self.data = requests.get("https://raw.githubusercontent.com/adambom/dictionary/master/graph.json")
        self.json_data = self.data.json()
        self.words = list(self.json_data.keys())
        self.words2 = []
        for i in range(0, len(self.words)):
            if len(self.words[i]) == 5:
                self.words2.append(self.words[i])
        self.words_df = pd.DataFrame(self.words2, columns=['Word'])
        self.most_likely_word = [
            ['S', 'E', 'R', 'A', 'I'],
            ['A', 'I', 'G', 'R', 'E'],
            ['A', 'F', 'I', 'R', 'E'],
            ['I', 'R', 'A', 'D', 'E'],
            ['A', 'E', 'S', 'I', 'R'],
            ['R', 'A', 'I', 'A', 'E'],
            ['I', 'R', 'A', 'T', 'E'],
            ['A', 'I', 'M', 'E', 'R'],
            ['M', 'A', 'R', 'I', 'E'],
            ['R', 'A', 'M', 'I', 'E'],
            ['A', 'E', 'R', 'I', 'E'],
            ['R', 'A', 'I', 'S', 'E'],
            ['A', 'I', 'D', 'E', 'R'],
            ['A', 'R', 'I', 'E', 'S'],
            ['C', 'E', 'R', 'I', 'A'],
            ['F', 'E', 'R', 'I', 'A'],
            ['E', 'R', 'I', 'C', 'A'],
            ['A', 'R', 'I', 'S', 'E'],
            ['C', 'R', 'A', 'I', 'E'],
            ['R', 'E', 'D', 'I', 'A']
        ]

        self.attempts = 5
        self.guess = self.most_likely_word[random.randint(0, len(self.most_likely_word))]
        self.words_list = list(self.mc_letter.keys())
        self.yellow_letters_list = []
        self.grey_letters_list = []
        self.green_letters_list = []

        '''Lists of most common words'''
        self.e_lst = []
        self.ea_lst = []
        self.ear_lst = []
        self.eari_lst = []
        self.eario_lst = []

        for i in range(0, len(self.words_df)):
            if 'E' in self.words_df['Word'][i]:
                self.e_lst.append(self.words_df['Word'][i])
            if 'E' in self.words_df['Word'][i] and 'A' in self.words_df['Word'][i]:
                self.ea_lst.append(self.words_df['Word'][i])
            if 'E' in self.words_df['Word'][i] and 'A' in self.words_df['Word'][i] and 'R' in self.words_df['Word'][i]:
                self.ear_lst.append(self.words_df['Word'][i])
            if 'E' in self.words_df['Word'][i] and 'A' in self.words_df['Word'][i] and 'R' in self.words_df['Word'][i] and 'I' in self.words_df['Word'][i]:
                self.eari_lst.append(self.words_df['Word'][i])
            if 'E' in self.words_df['Word'][i] and 'A' in self.words_df['Word'][i] and 'R' in self.words_df['Word'][i] and 'I' in self.words_df['Word'][i] and 'O' in self.words_df['Word'][i]:
                self.eario_lst.append(self.words_df['Word'][i])

    def play_one(self):
        print("The game of Wordle for " + str(self.date))
        print('Guess #1 is ' + str(self.guess) + ' or a word with the letters ' + str(self.words_list[0:5]))
        self.attempts -= 1
        self.words_df

    def play_two(self, yellow_letter, green_letter, grey_letters, word_attempted):
        for i in range(0, len(yellow_letter)):
            self.yellow_letters_list.append(yellow_letter[i])
        for i in range(0, len(grey_letters)):
            self.grey_letters_list.append(grey_letters[i])
            self.words_list.remove(grey_letters[i])
        for i in range(0, len(green_letter)):
            self.green_letters_list.append(green_letter[i])
        lst = []
        for i in range(0, len(word_attempted)):
            lst.append(word_attempted[i])
        print(self.yellow_letters_list)
        print(self.green_letters_list)
        print(self.grey_letters_list)
        print(self.words_list)
