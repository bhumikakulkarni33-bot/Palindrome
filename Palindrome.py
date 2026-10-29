import sys

word = sys.argv[1]

if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")
