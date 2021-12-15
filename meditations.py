#%%
import json
import random

with open("meditations.json", "r") as read_file:
    data = json.load(read_file)

# Generate section count
# [len(data["meditations"][f"{x}"]) for x in range(1,13)]

#%%
book = random.randint(1, 12)
max_sections = data["sectionCount"][book - 1]
section = random.randint(1, max_sections)

quote = data['meditations'][f"{book}"][section]
print(quote, f"Book {book}, {section}.")
# %%
