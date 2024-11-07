import json

docs = {
        "doc1" : ["mango","apple","grapes"],
        "doc2": ["peas","mango"],
        "doc3": ["mango","grapes","peas"],
        "doc4": ["apple","grapes"]
}

inverted_files = {}

for doc,fruits in docs.items():
    for fruit in fruits:
        if fruit not in inverted_files:
            inverted_files[fruit] = [doc]
        else:
            inverted_files[fruit].append(doc)
print('Inverted FIles :')
print(json.dumps(inverted_files,indent=4))