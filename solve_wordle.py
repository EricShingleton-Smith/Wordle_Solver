from datetime import date
import random
import pandas as pd
import json
import os
import requests

date = date.today()
words_list = {
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
data = requests.get(
    "https://raw.githubusercontent.com/adambom/dictionary/master/graph.json")
json_data = data.json()
words = list(json_data.keys())
words2 = []
for i in range(0, len(words)):
    if len(words[i]) == 5:
        words2.append(words[i])
words_df = pd.DataFrame(words2, columns=['Word'])
most_likely_word = [
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

attempts = 5
most_common_letters = list(words_list.keys())
yellow_letters_list = []
grey_letters_list = []
green_letters_list = []

'''Lists of most common words'''
e_lst = []
ea_lst = []
ear_lst = []
eari_lst = []
eario_lst = []

for i in range(0, len(words_df)):
    if 'E' in words_df['Word'][i]:
        e_lst.append(words_df['Word'][i])
    if 'E' in words_df['Word'][i] and 'A' in words_df['Word'][i]:
        ea_lst.append(words_df['Word'][i])
    if 'E' in words_df['Word'][i] and 'A' in words_df['Word'][i] and 'R' in words_df['Word'][i]:
        ear_lst.append(words_df['Word'][i])
    if 'E' in words_df['Word'][i] and 'A' in words_df['Word'][i] and 'R' in words_df['Word'][i] and 'I' in words_df['Word'][i]:
        eari_lst.append(words_df['Word'][i])
    if 'E' in words_df['Word'][i] and 'A' in words_df['Word'][i] and 'R' in words_df['Word'][i] and 'I' in words_df['Word'][i] and 'O' in words_df['Word'][i]:
        eario_lst.append(words_df['Word'][i])

guess = ear_lst[random.randint(
    0, len(ear_lst))]

'''Word Template'''
word_template = {
    0: '_',
    1: '_',
    2: '_',
    3: '_',
    4: '_'
}

'''Words used'''
lst = []
potential_words_final = []

'''Where yellow letters are not'''
yellow_placement = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: []
}

def play_one():
    global attempts
    print("The game of Wordle for " + str(date))
    print('Guess #1 is ' + str(guess) +
          ' or a word with the letters ' + str(most_common_letters[0:5]))
    print('Here are the most common letters in descending order ' + str(most_common_letters))
    'words2.remove(''.join(guess))'
    'lst.append(guess)'
    print('You have made ' + str(5 - attempts) + ' attempts.')

def play_again(yellow_letter, green_letter, grey_letters, word_attempted):

        '''Store lists of letters'''
        for i in yellow_letter:
            if yellow_letter[i] not in yellow_letters_list:
                yellow_letters_list.append(yellow_letter[i])
            else:
                continue
        for i in range(0, len(grey_letters)):
            if grey_letters[i] not in grey_letters_list:
                grey_letters_list.append(grey_letters[i])
            else:
                continue
        for i in range(0, len(grey_letters)):
            if grey_letters == '':
                break
            most_common_letters.remove(grey_letters[i])
        lst.append(word_attempted)
        words2.remove(word_attempted)

        for i in yellow_letter:
            yellow_placement[i].append(yellow_letter[i])

        global attempts
        attempts -= 1
        print('You have made ' + str(5 - attempts) + ' attempts.')

        '''Update the word'''
        if len(green_letter) >= 1:
            for i in green_letter:
                if word_template[i] == '_':
                    word_template[i] = green_letter[i]
        word_temp = [word_template[i] for i in range(0, len(word_template))]
        word = ' '.join(word_temp)

        '''Centralized list of words'''
        potential_words_green = []
        potential_words_yellow = []
        potential_words_yellow2 = []
        potential_words_grey = []

        '''Grey Letters'''
        for i in range(0, len(words2)):
            count = 0
            for e in range(0, len(grey_letters_list)):
                if grey_letters_list[e] in words2[i]:
                    count += 1
            if count == 0 or green_letter == '':
                potential_words_grey.append(words2[i])

        '''Green Letters'''
        word_temp2 = ''.join([green_letter[i] for i in green_letter])
        for i in range(0, len(potential_words_grey)):
            if green_letter == {}:
                break
            count = 0
            for e in green_letter:
                if green_letter[e] == '':
                    continue
                if green_letter[e] == potential_words_grey[i][e]:
                    count += 1
            if count == len(word_temp2):
                potential_words_green.append(potential_words_grey[i])

        '''Yellow Letters'''
        if green_letter == {}:
            potential_words_green = potential_words_grey
        for i in range(0, len(potential_words_green)):
            if yellow_placement == {}:
                break
            count = 0
            for e in yellow_placement:
                if len(yellow_placement[e]) == 0:
                    continue
                for x in yellow_placement[e]:
                    if potential_words_green[i][e] == x:
                        count += 1
            if count == 0:
                potential_words_yellow2.append(potential_words_green[i])

        yellow_temp = ''.join([yellow_letter[i] for i in yellow_letter])
        for i in range(0, len(potential_words_yellow2)):
            count = 0
            if yellow_temp == '':
                potential_words_yellow = potential_words_green
                break
            for e in range(0, len(yellow_letters_list)):
                if yellow_letters_list[e] in potential_words_yellow2[i]:
                    count += 1
                if count == len(yellow_letters_list):
                    potential_words_yellow.append(potential_words_yellow2[i])

        '''Print the word'''
        print('Your word so far is ' + str(' '.join(word_temp)))
        print('Words that are out of place are ' +
              str(yellow_letters_list))
        print('The letters: ' + str(grey_letters_list) +
              ' are not in the word.')
        print('You have used the words: ' + str(lst))
        print('Potential words are: ' + str(potential_words_yellow))
