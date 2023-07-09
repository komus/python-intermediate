import re


pattern_re = r"Python"
string = "I love python. Python is a powerful language"

# re.match(pattern, string)
match_rst = re.search(pattern_re, string)

if match_rst:
    print("Match was found")
else:
    print("No match")


#look for 6 letter words

#\b word boundary
pattern = r"\b\w{6}\b"
matches = re.findall(pattern, string)
print(matches)


pattern_s = r"\s"
match_s = re.split(pattern_s, string)
print(match_s)


# If count not set, it replaces all the occurrence if the matches
replacement = ".NET"
new_string = re.subn(pattern, replacement, string)
print(new_string)
print(string)


"""
Example 1: Match a single character between c and t
"""
pattern = r"[c|C].t"
string = "The cat sat on the ledge of Mr Catdoso's house. It was a catastrophy"
occ = re.findall(pattern, string)
print(occ)

"""
^ = start
$ = end

Example: Check if a string begins with a word
"""
pattern = r"^Hello"

string1 = "Hello world, it is REGEX day"
string2 = "A day for REGEX, Hello my friends"

rst_1 = re.search(pattern, string2)
print(bool(rst_1))


"""
Example: Return all one or more digits
"""
string = "I bought apples for 9.47, bread for 55.62 and chicken for 12.89. I am left with $20.00"
pattern = r"\d+.\d+"

mat = re.findall(pattern, string)
print(mat)

"""
Extract Hexadecimal colors

#4f4f4f
"""

pattern = r"(?:[0-9a-fA-F])+"
# #[0-9a-zA-Z]{6}


"""
- Extract Email
- Extract date in format YYYY-MM-DD
- strong password
- 
"""