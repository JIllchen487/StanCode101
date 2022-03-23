"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = []


def main():
    """
    TODO:
    """
    start = time.time()

    ####################
    global dic
    dic = read_dictionary()
    # print(dic)
    l1 = input_row('1 row of letters: ')
    # l1 = ['f', 'y', 'c', 'l']
    l2 = input_row('2 row of letters: ')
    # l2 = ['i', 'o', 'm', 'g']
    l3 = input_row('3 row of letters: ')
    # l3 = ['o', 'r', 'i', 'l']
    l4 = input_row('4 row of letters: ')
    # l4 = ['h', 'j', 'h', 'u']
    boggle_board = create_board([l1, l2, l3, l4])
    find_words(boggle_board)

    ####################

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for word in f:
            dic.append(word[:-1])
        return dic


def input_row(pmp):
    a = input(pmp)
    lst = a.split()
    for i in lst:
        if (not i.isalpha()) or len(i) != 1:
            print('Illegal Input')
            return
    return lst


def create_board(list_of_lists):
    board = {}
    for i in range(4):
        lst = list_of_lists[i]
        for j in range(4):
            board[(j, i)] = lst[j]
    return board


def find_words(board):
    """
    :param board: (dictionary) A dictionary that is constructed by inputs of the boggle board
    :return: does not return anything but print out all the words with count
    """
    chosen = []
    for x in range(4):
        for y in range(4):
            coordinates = (x, y)
            forming_word = board[coordinates]
            visited = [coordinates]
            find_words_helper(coordinates, board, chosen, forming_word, visited)
    print(len(chosen))


def find_words_helper(coordinates, board, chosen_words, forming_word, visited):
    """
    :param coordinates: (tuple) the pivot point to start with when searching for words
    :param board: (dictionary) A dictionary that is constructed by inputs of the boggle board
    :param chosen_words: (list) contains all the chosen vocab
    :param visited: (list) contains all the coordinates of chosen neighbors
    :return: does not return anything but print out all the words with count
    """
    global dic
    neighbors = neighbor(coordinates, board)
    # Base Case
    if forming_word in dic and len(forming_word) >= 4:
        if forming_word not in chosen_words:
            print('Found: ', forming_word)
            chosen_words.append(forming_word)
    # Choose
    for neighbor_coordinates in neighbors:
        if neighbor_coordinates not in visited:
            new_word = forming_word + neighbors[neighbor_coordinates]
            if has_prefix(new_word):
                visited.append(neighbor_coordinates)
                # Explore
                find_words_helper(neighbor_coordinates, board, chosen_words, new_word, visited)
                # Un-choose
                visited.pop()


def neighbor(coordinates, board):
    neighbors = {}
    x = coordinates[0]
    y = coordinates[1]
    for i in range(-1, 2):
        neighbor_x = x + i
        if 0 <= neighbor_x <= 3:
            for j in range(-1, 2):
                neighbor_y = y + j
                if 0 <= neighbor_y <= 3 and (i, j) != (0, 0):
                    neighbors[(neighbor_x, neighbor_y)] = board[(neighbor_x, neighbor_y)]
    return neighbors


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ele in dic:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
