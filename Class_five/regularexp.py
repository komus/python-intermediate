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
- Extract Email \b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[.A-Z|a-z]{2,}\b
- Extract date in format YYYY-MM-DD \b\d{4}[-|/]\d{2}[-|/]\d{2}\b  \b\d{4}[-/\.]\d{2}[-/\.]\d{2}\b
- strong password: minimum of 8 characters, has at least 1 uppercase, at least one digit and special character
- ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#%^*|])[A-Za-z\d$@_\-\.#!%&]{8,}$
"""

pattern_p = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#%^*|])[A-Za-z\d$@_\-\.#!%&]{8,}$"
string = "P@ssw0rd!"

valid_password = re.search(pattern_p, string)
if valid_password:
    print("Valid")
else:
    print("not valid")


string = "oy@example.com find@all.co.uk are the emails available"
pattern = r"\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[.A-Z|a-z]{2,}\b"
all_email = re.findall(pattern, string)
print(all_email)

list_1 = ['password', 'Passw0rd12!', 'Passw0rd']
val = [True if re.search(pattern_p, val) else False for val in list_1]
print(val)