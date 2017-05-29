'''
Question 2

Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''

# palindromes()
def ques2(a):
    a = a.lower()
    results = []

    for i in range(len(a)):
        for j in range(0, i):
            text = a[j:i + 1]

            if text == text[::-1]:
                results.append(text)

    print "Here are the palindromes for this string:"
    for i in results:
        print i

ques2("geeksskeeg")
ques2("racecar")
ques2("neveroddoreven")

# O(2n ^2 + n)
