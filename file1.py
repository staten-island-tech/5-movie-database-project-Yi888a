import json
data = json.load(open("./movies.json", encoding="utf8"))
movies = open("./movies.json", encoding="utf8")
titleget = data.get("title", "Unknown Title")
print(f"title: {titleget}")