# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# If s = 'azcbobobegghakl', then display: Number of times bob occurs is: 2

s = 'ebobbobbobobobobob'
count = 0

for i in range(len(s) - 1):
    if (s[i - 1: i + 2] == "bob"):
        count += 1

print("\nNumber of times bob occurs is: " + str(count))
