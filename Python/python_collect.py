from string import punctuation
import clipboard
import os

path = "/Users/111244rfsf/Documents/Repositories/theEdabitProject/theEdabitProjectRepo/Python"

os.system(f"cd {path}")
os.system(f"ls | pbcopy")

folders = clipboard.paste()
"""
...
multiply_matrix
nom_nom
prime_count
python_collect.py
...
"""

folders = [i for i in folders.split("\n") if not "." in i
and i
]

# Reset Gallery
os.system("echo > gallery.md")
for folder in folders:
	os.system(f"echo '\n# {folder}\n' >> gallery.md")
	os.system("echo '\n```\n' >> gallery.md")
	os.system(f"cat {folder}/{folder}.py >> gallery.md")
	os.system("echo '\n```\n' >> gallery.md")
print("done.")

with open("gallery.md", "r") as f:
	gallery = f.read()

with open("fancy_md_gallery.md", "w") as f:
	f.write(gallery)





