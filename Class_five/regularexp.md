# Regular Expressions - REGEX

- match patterns with strings of text
- provides means to efficiently replace, parse, search or extract text data definied by a specific pattern

## Patterns

`.` - matches any character except newline `.read` will match Bread, Dread. `b.t` will match bit, bot, but, bat

`?` - matches 0 or 1 repetitions - match 0 or 1 of the preceeding characters `olk?a` will match ola and olka

`+` - matches 1 or more repetitions `bre+d` match with bred, breed, breeeeed

`*` - matches 0 or more repetitions `*ala` match la, ala, aaaaaaaaaaaaaaala

`$` - end of the string `f$` matches with afridf, beautif - f ends the string

`[]` - indicates a set of characters. `[Ww]ood` Woodstock, wood, Woody, woodland

`^` - caret at the beginining of a pattern signifies the start of the string. `^[a-z]` will match bread, fred but not Bread, Frederic
Caret inside a square bracket `[]` means negation. `[^a-z]` means not a-z. Bread, Frederic

`{n}` - exactly n repetitions `e{3}` eee. `{n,}` n or more times. `{, n}` less than or equeal to n times. `{m,n}` between m and n repetition. 

`\` - escape special characters

`|` means OR 

`()`- group sub patterns

`\d` - any digit which is equivalent to `[0-9]`

`\D` - any non-digit character

`\s` - matches any whitespace character

`\S` - non whitespace character

`\w` - matches any word/alphanumeric. this is equivalent to `[A-Za-z0-9_]`

`\W` - match non alphanumeric character

## REGEX in python

`import re`

#### re.match

This will try to match the regex pattern to the string. In match, this only checks if the pattern matches the begining of the string

#### re.search
Does not limit the match to the beginning of the string. It can locate a match anywhere in the string. It looks for the first location where the pattern produces a match with the string

#### re.findall

returns all occurences / non-overlapping matches. 


#### re.split

this splits a string by the occurrence of the pattern. 

#### re.sub

This replaces the occurence of the pattern in the string. It will replace all occurrence unless the max is provided.

#### re.subn

similar to the sub, it returns a tuple of the new string and the number of substitutions made