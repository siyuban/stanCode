"""
File: complement.py
Name: 萬思妤
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Find the complement strand of a DNA sequence.
    """
    dna = input("Please give me a DNA strand and I'll find the complement:")
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of '+str(dna)+' is '+str(new_dna))


def build_complement(dna):
    """
    :param dna: The strand of a DNA sequence that the user gave.
    :return: The complement strand of a DNA sequence.
    """
    ans = ''
    for base in dna:
        if base == 'T':
            ans += 'A'
        elif base == 'A':
            ans += 'T'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
