import json
data = json.load(open("./movies.json", encoding="utf8"))
movies = open("./movies.json", encoding="utf8")
titleget = data.get("title", "Not specified")
print(f"title: {titleget}")