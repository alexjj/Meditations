#%%
import json

with open("meditations.json", "r") as read_file:
    data = json.load(read_file)

#%%

book_names = [
    "Book I",
    "Book II",
    "Book III",
    "Book IV",
    "Book V",
    "Book VI",
    "Book VII",
    "Book VIII",
    "Book IX",
    "Book X",
    "Book XI",
    "Book XII",
    ]

result = []

for book in range(12):
    for section in range(data["sectionCount"][book]):
        book_name = book_names[book]
        title = f"{book_name} - Section {section + 1}"
        tags = f"[[{book_name}]]"
        quote = data['meditations'][f"{book + 1}"][section]

        # Create each tiddler
        entry = dict()
        entry["created"] = "-01800000000000000"
        entry["text"] = quote
        entry["tags"] = tags
        entry["title"] = title
        entry["section"] = f"{section + 1}"
        entry["book"] = f"{book + 1}"

        result.append(entry)


#%%
# Write to json file
with open("tw_data.json", "w") as write_file:
    json.dump(result, write_file)


