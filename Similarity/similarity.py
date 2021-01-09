"""
File: similarity.py
Name: 萬思妤
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Find out the sub sequences of a long dna sequence that has the highest pairing rate
    with the  dna sequence that we want to match.
    """
    long_sequence = input('Please give me a DNA sequence to search:')
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match?')
    short_sequence = short_sequence.upper()
    result = match(long_sequence, short_sequence)
    print('The best match is '+str(result))


def match(long, short):
    """
    :param long: The DNA sequence to search.
    :param short: DNA sequence that we want to match.
    :return: Sub sequences that has the highest pairing rate.
    """
    maximum = 0
    homology = ''
    for i in range(len(long)-len(short)+1):
        # number of times that we have to pair.
        dna = long[i:i + len(short)]
        # sub sequences of long dna sequence.(starts form i == 0)
        count = 0
        for j in range(len(short)):
            if short[j] == dna[j]:
                count += 1
                # How many nitrogenous base are matched in this sub sequences.
        matched = count / len(short)
        if matched > maximum:
            maximum = matched
            homology = dna
            # sub sequences that has the highest pairing rate.
    return homology



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
