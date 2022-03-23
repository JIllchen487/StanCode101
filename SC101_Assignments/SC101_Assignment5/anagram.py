"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global Variable
dic = {}
anagrams = []


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    global dic
    dic = read_dictionary()
    # lst = ['sanction', 'contains', 'canonist', 'actinons', 'sonantic']
    print('Welcome to Stancode "Anagram Generator"(or -1 to quit)')
    s = input('Find anagrams for: ')
    if s == EXIT:
        pass
    else:
        find_anagrams(s)
    ####################

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            start = word[0:1]
            if start in dic:
                dic[start].append(word)
            else:
                dic[start] = [word]
    return dic


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    left_word_c = len(s)
    find_anagrams_helper(s, left_word_c, '')
    ana_n = len(anagrams)
    print(ana_n, 'anagrams:', anagrams)


def find_anagrams_helper(s, left_word_c, begin_word):
    """
    :param s:
    :return:
    """
    global anagrams
    global dic
    print('Searching...')
    for i in range(left_word_c):
        select = s[i]
        left_alphas = s[:i] + s[i + 1:]
        next_begin_word = begin_word + select
        if len(left_alphas) > 0:
            if has_prefix(next_begin_word):
                find_anagrams_helper(left_alphas, len(left_alphas), next_begin_word)
        else:
            index = next_begin_word[0:1]
            if index in dic:
                if next_begin_word in dic[index] and next_begin_word not in anagrams:
                    anagrams.append(next_begin_word)
                    print('Found: ' + next_begin_word)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    global dic
    s_start = sub_s[0:1]
    if s_start in dic:
        for ele in dic[s_start]:
            if ele.startswith(sub_s):
                return True
    return False




if __name__ == '__main__':
    main()
