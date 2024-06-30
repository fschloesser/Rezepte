import os
import yaml

# processes file
# - creates markdown file for better viewing online
# - returns entry to readme
def process_file(filename,src_directory,target_directory):
    new_filename = "{}.md".format(filename.split('.yaml')[0])
    print("converting {}/{} to {}/{}".format(src_directory,filename,target_directory,new_filename))
    with open("{}/{}".format(src_directory,filename)) as stream:
        recipe = yaml.safe_load(stream)

    with open("{}/{}".format(target_directory,new_filename), 'w', encoding='utf-8') as markdown:
        markdown.write("{}\n===\n{}\n".format(recipe["title"], recipe["subtitle"]))
        markdown.write("\nZutaten:\n---\n")
        for ing in recipe["ingredients"]:
            markdown.write("- {} {} {}\n".format(ing["amount"],ing["unit"],ing["ingredient"]))
        markdown.write("\nAnleitung:\n---\n")
        markdown.write(recipe["instructions"].replace('\n','\n\n'))
    return {"title": recipe["title"], "subtitle": recipe["subtitle"], "tags": recipe["tags"], "filename": new_filename}

# main loop
src_directory = '../content'
target_directory = '../rezepte'
readme_file = '../README.md'
readme_entries = []

for file in os.listdir(src_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".yaml"):
        readme_entries.append(process_file(filename,src_directory,target_directory))
with open("{}".format(readme_file), 'w', encoding='utf-8') as readme:
    readme.write("\nAlle Rezepte im Ueberblick:\n===\n")
    tags = sorted(list(set(sum([entry["tags"] for entry in readme_entries],[]))))
    for tag in tags:
        readme.write("\n{}\n---\n".format(tag))
        entries = {}
        for recipe in readme_entries:
            if tag in recipe["tags"]:
                entries[recipe["title"]] = recipe
        for i in sorted(entries.keys()):
            recipe = entries[i]
            readme.write("- [{}](rezepte/{}) - {}\n".format(recipe["title"], recipe["filename"], recipe["subtitle"]))
