# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then display : Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then display : Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

max_len = 0
substring = s[0]
longest_substring = s[0]

for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        substring += s[i + 1]
        if len(substring) > max_len:
            max_len = len(substring)
            longest_substring = substring
    else:
        substring = s[i + 1]

print("Longest substring in alphabetical order is: " + longest_substring)
