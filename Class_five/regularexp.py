import re


pattern_re = r"Python"
string = "I love python. Python is a powerful language"

# re.match(pattern, string)
match_rst = re.search(pattern_re, string)

if match_rst:
    print("Match was found")
else:
    print("No match")
