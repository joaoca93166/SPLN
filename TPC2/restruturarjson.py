import re
import json

file = open("medicina.json")
content = json.load(file)
file.close()

data = {}

for entry in content["entries"]:
    treatedEntry = {}

    galego = list(entry.keys())[0]

    number = entry[galego]["number"]

    info = entry[galego]
    info.pop("number")

    infoKeys = list(info.keys())

    info["languages"]["ga"] = galego

    # clean info
    for i in infoKeys:
        if i == "languages":
            for j in list(info[i].keys()):
                info[i][j] = re.sub(r'[\n\t]', r'', info[i][j])
        else:
            info[i] = re.sub(r'[\n\t]', r'', info[i])


    treatedEntry[number] = info
    
    data.update(treatedEntry)

content["entries"] = data

with open('medicina_2.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, sort_keys=True, indent=1, ensure_ascii=False)
