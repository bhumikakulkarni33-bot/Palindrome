import sys

string = sys.argv[1]
reverse = string[::-1]

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
