"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
    """
	TODO: randomly generate coin flips based on the number of runs(consecutive results on either 'H' or 'T')  that the user assigns.
	"""
    print('Let’s flip a coin!')
    n = int(input('Number of runs: '))
    r = random.choice(['H', 'T'])
    # print('choice=', r)
    result = ''
    prev_f = ''
    c_run = 0
    new_run = True
    while True:
        # print('')
        f = random.choice(['H', 'T'])
        # print('f=', f)
        # print('begin_new_run=', new_run)
        if new_run:
            if f == prev_f:
                new_run = False
                if f == r:
                    c_run += 1
        if not new_run:
            if f != prev_f:
                new_run = True
        # print('end_new_run=', new_run)
        # print('c_run:', c_run)
        result += f
        # print('result:', result)
        prev_f = f
        # print('prev_f:', prev_f)
        if c_run == n:
            print(result)
            break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
