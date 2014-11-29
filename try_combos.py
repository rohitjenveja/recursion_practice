#!/usr/bin/python

"""Sample code that will find valid english words in a string.

Provided that there is a set defined in valid_english_words.
"""


def try_combos(word, words_found):
  if len(word) == 1:
    if word in valid_english_words:
      words_found.add(word)
    return words_found
  try_combos(word[1:], words_found)
  try_combos(word[:-1], words_found)

  if word in valid_english_words:
    words_found.add(word)
  return words_found


if __name__ == '__main__':
  valid_english_words = ('a', 'happy', 'py')
  # given a string, find all the valid english words within it
  # valid_english_words is given as a set.
  print try_combos('iamhappy', set([]))
