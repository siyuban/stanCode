"""
File: anagram.py
Name: 萬思妤
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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = []
count = 0


def main():
    global count
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        string = (input('Find anagrams for: '))
        if string == EXIT:
            break
        count = 0
        find_anagrams(string)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split()
            word = word[0]
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s: the word input by user
    :return: all the anagram(s)
    """
    ans_list = []
    find_anagrams_helper(s, '', ans_list, [])
    print(count, 'anagrams: ', ans_list)


def find_anagrams_helper(s, ans, ans_list, index_lst):
    global count
    if len(ans) == len(s):
        if ans in dictionary:
            if ans not in ans_list:
                count += 1
                print('Searching...')
                print('Found: ', ans)
                ans_list.append(ans)
    else:
        for i in range(len(s)):
            if i in index_lst:
                pass
            else:
                ans += s[i]
                index_lst.append(i)
                if has_prefix(ans):
                    find_anagrams_helper(s, ans, ans_list, index_lst)
                ans = ans[:len(ans)-1]
                index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: sub string of anagram(s).
    :return: whether sub string exist in dictionary list.
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
