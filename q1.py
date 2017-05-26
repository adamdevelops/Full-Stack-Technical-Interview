'''
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s.
 For example: if s = "udacity" and t = "ad", then the function returns True.
 Your function definition should look like: question1(s, t) and return
  a boolean True or False.

'''


def is_anagram(s, t):
    s = sorted(s)
    t = sorted(t)

    if len(t) > len(s):
        return "Anagram not possible"

    chars = []

    for index, char1 in enumerate(s):
        for index, char2 in enumerate(t):
            if char1 == char2:
                chars.append(char2)
                # print "Found"    ---TEST

    if chars == t:
        print "There is an anagram found for the two inputted strings"


is_anagram("udacity", "ad")
