#!/usr/bin/env python3
#*******************************************************
#       Filename: ps4a.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Part A: Permutations of a string
#       Created on: 2018-11-09 10:48:44
#*******************************************************


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    result = []
    if len(sequence) == 1:
        return list(sequence)
    else:
        first_letter = sequence[0]
        sequence_left = sequence[1:]
        sequence_list = get_permutations(sequence_left)
        for elem in sequence_list:
            for i in range(len(elem)+1):
                elem_list = list(elem)
                elem_copy = elem_list.copy()
                elem_copy.insert(i, first_letter)
                result.append(''.join(elem_copy))

    return result


if __name__ == '__main__':
    #EXAMPLE 0
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    #EXAMPLE 1
    example_input_1 = 'it'
    print('Input:', example_input_1)
    print('Expected Output:', ['it', 'ti'])
    print('Actual Output:', get_permutations(example_input_1))
    print()

    #EXAMPLE 2
    example_input_2 = 'eat'
    print('Input:', example_input_2)
    print('Expected Output:', ['eat', 'aet', 'ate', 'eta', 'tea', 'tae'])
    print('Actual Output:', get_permutations(example_input_2))
    print()

    #EXAMPLE 3
    example_input_3 = 'cat'
    print('Input:', example_input_3)
    print('Expected Output:', ['cat', 'act', 'atc', 'cta', 'tca', 'tac'])
    print('Actual Output:', get_permutations(example_input_3))
    print()




