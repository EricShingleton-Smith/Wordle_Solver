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
        self.words_list = {
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
        self.words_list = list(self.words_list.keys())
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

        '''Word Template'''
        self.word_template = {
            0: '_',
            1: '_',
            2: '_',
            3: '_',
            4: '_'
        }
        self.word_temp = [self.word_template[i] for i in range(0, len(self.word_template))]
        self.word = ' '.join(self.word_temp)

    def play_one(self):
        print("The game of Wordle for " + str(self.date))
        print('Guess #1 is ' + str(self.guess) + ' or a word with the letters ' + str(self.words_list[0:5]))
        print('Here are the most common letters in descending order' + str(self.words_list))
        self.attempts -= 1
        self.words_df
        self.words2.remove(''.join(self.guess))
        print('You have made ' + str(5 - self.attempts) + ' attempts.')

    def play_two(self, yellow_letter, green_letter, grey_letters, word_attempted):
        for i in range(0, len(yellow_letter)):
            self.yellow_letters_list.append(yellow_letter[i])
        for i in range(0, len(grey_letters)):
            self.grey_letters_list.append(grey_letters[i])
        lst = []
        for i in range(0, len(self.grey_letters_list)):
            self.words_list.remove(self.grey_letters_list[i])
        for i in range(0, len(word_attempted)):
            lst.append(word_attempted[i])
        print(self.yellow_letters_list)
        print(self.grey_letters_list)
        print(self.words_list)

        self.words2.remove(word_attempted)

        self.attempts -= 1
        print('You have made ' + str(5 - self.attempts) + ' attempts.')

        '''Update the word'''
        if len(green_letter) == 1:
            self.word_temp[list(green_letter.keys())[0]
                           ] = green_letter[list(green_letter.keys())[0]]

        '''Potential words based on yellow_letters and no green letters'''
        if len(green_letter) == 0 and len(yellow_letter) != 0:
            potential_words = []
            for i in range(0, len(self.words2)):
                count = len(yellow_letter)
                if self.words_list[count] not in ''.join(self.words2):
                    print('Letter ' + str(self.words_list[count]) +
                        ' not present in any potential words.')
                    break
                if self.words_list[count] in self.words2[i]:
                    potential_words.append(self.words2[i])
            print('Potential words with the letters ' + str(yellow_letter) + ', '
                + str(self.words_list[count]) + 'are ' + str(potential_words))


        '''Print the word'''
        print('Your word so far is ' + str(self.word))
        print('Words that are out of place are ' + str(self.yellow_letters_list))
        print('The letters: ' + str(self.grey_letters_list) + ' are not in the word.')
        print('You have used the words: ' + str(lst))

    def play_three(self, yellow_letter, green_letter, grey_letters, word_attempted):
        for i in range(0, len(yellow_letter)):
            self.yellow_letters_list.append(yellow_letter[i])
        for i in range(0, len(grey_letters)):
            self.grey_letters_list.append(grey_letters[i])
        lst = []
        for i in range(0, len(self.grey_letters_list)):
            self.words_list.remove(self.grey_letters_list[i])
        for i in range(0, len(word_attempted)):
            lst.append(word_attempted[i])
        print(self.yellow_letters_list)
        print(self.grey_letters_list)
        print(self.words_list)

        self.words2.remove(word_attempted)

        self.attempts -= 1
        print('You have made ' + str(5 - self.attempts) + ' attempts.')

        '''Update the word'''
        if len(green_letter) == 1:
            self.word_temp[list(green_letter.keys())[0]
                           ] = green_letter[list(green_letter.keys())[0]]

        '''Print the word'''
        print('Your word so far is ' + str(self.word))
        print('Words that are out of place are ' +
              str(self.yellow_letters_list))
        print('The letters: ' + str(self.grey_letters_list) + 'are not in the word.')
        print('You have used the words: ' + str(lst))

    def play_four(self, yellow_letter, green_letter, grey_letters, word_attempted):
        pass

    def play_fifth(self, yellow_letter, green_letter, grey_letters, word_attempted):
        pass

    def play_six(self, yellow_letter, green_letter, grey_letters, word_attempted):
        pass
