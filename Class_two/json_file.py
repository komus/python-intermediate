import json

#open default is read
with open("test.json") as f:
    data = json.load(f)

print(data["man city"][0])

sample = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
"""
    sort_keys # sorts the key in ascending order
    indent # 
"""
with open('glosory.json', 'w') as f:
    json.dump(sample, f, indent = 2)