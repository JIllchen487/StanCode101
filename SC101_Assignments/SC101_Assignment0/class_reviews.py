"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO:  Calculate the score statistics (maximum, minimum and average) for SC001 & SC101
    """
    max001 = 0
    min001 = 10  #Assumption: 10 is the maximum score
    sum001 = 0
    n001 = 0

    max101 = 0
    min101 = 10  #Assumption: 10 is the maximum score
    sum101 = 0
    n101 = 0
    while True:
        c = input('Which class? ').upper()
        if c == 'SC001':
            s001 = int(input('Score? '))
            sum001 += s001
            n001 += 1
            if s001 > max001:
                max001 = s001
            if s001 < min001:
                min001 = s001

        elif c == 'SC101':
            s101 = int(input('Score? '))
            sum101 += s101
            n101 += 1
            if s101 > max101:
                max101 = s101
            if s101 < min101:
                min101 = s101

        elif c == '-1':
            if n001 == 0 and n101 == 0:
                print('No class scores were entered')
            else:
                print('========SC001========')
                if n001 != 0:
                    print('max (001): ', max001)
                    print('min (001): ', min001)
                    print('avg (001): ', sum001/n001)
                else:
                    print('No score for SC001')

                print('========SC101========')
                if n101 != 0:
                    print('max (101): ', max101)
                    print('min (101): ', min101)
                    print('avg (101): ', sum101/n101)
                else:
                    print('No score for SC101')
            break






# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
