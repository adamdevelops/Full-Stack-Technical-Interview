'''
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s.
 For example: if s = "udacity" and t = "ad", then the function returns True.
 Your function definition should look like: question1(s, t) and return
  a boolean True or False.

'''

# is_anagram()
def ques1(s, t):
    string_dict = {}

    if len(t) > len(s):   # O(1)
        return "Anagram not possible"

    for char in t:
        string_dict[char] = 1
        if char in s:
            string_dict[char] += 1

    return all(string_dict[char]==2 for char in string_dict)


print ques1("stackoverflow", "rover")
print ques1("udacity", "ad")
print ques1("animal", "fan")
# O(nlogn + nlogn + n^2)
