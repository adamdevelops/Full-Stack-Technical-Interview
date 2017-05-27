'''
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s.
 For example: if s = "udacity" and t = "ad", then the function returns True.
 Your function definition should look like: question1(s, t) and return
  a boolean True or False.

'''

# is_anagram()
def ques1(s, t):
    s = sorted(s)  # O(n)
    t = sorted(t)  # O(n)

    if len(t) > len(s):   # O(1)
        return "Anagram not possible"

    chars = []

    for index, char1 in enumerate(s):   # O(nm)
        for index, char2 in enumerate(t):
            if char1 == char2:
                chars.append(char2)
                # print "Found"    ---TEST

    if chars == t:
        print "There is an anagram found for the two inputted strings"


ques1("udacity", "ad")
# O(nlogn + nlogn + n^2)
