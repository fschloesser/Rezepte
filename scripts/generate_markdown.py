import os
import yaml
from random import randint

src_directory = '../content'
target_directory = '../rezepte'
readme_file = '../README.md'
readme_entries = []

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
    return {
            "title": recipe["title"],
            "subtitle": recipe["subtitle"],
            "tags": recipe["tags"],
            "filename": new_filename,
            "difficulty": recipe["difficulty"],
            "time": recipe["time"]
            }

def format_time(number):
    if number < 1 or number > 3:
        raise Exception("{} is not a valid time rating".format(number))
    out = ""
    for i in range(3):
        if i < number:
            out += ":clock{}: ".format(randint(1,12))
        else:
            ":white_circle: "
            break
    return out

smileys = [ ":smiley: ",
            ":grin: ",
            ":wink: ",
            ":relieved: ",
            ":smirk: ",
            ":blush: ",
            ":grinning: ",
           ]
smileys_length = len(smileys)-1
def format_difficulty(number):
    if number < 1 or number > 3:
        raise Exception("{} is not a valid difficulty rating".format(number))
    out = ""
    for i in range(3):
        if i < number:
            out += smileys[randint(0,smileys_length)]
        else:
            out += ":dotted_line_face: "
    return out

def recipe_link(recipe):
    return "- {}{}[{}](rezepte/{}) - {}\n".format(
            format_difficulty(recipe["difficulty"]),
            format_time(recipe["time"]),
            recipe["title"],
            recipe["filename"],
            recipe["subtitle"],
        )

def anchorize(anchor):
    return anchor.replace(' ','_').lower()

def toc_subheading(title, anchor):
    if anchor:
        return "\n## <a href='{}'>{}</a>\n".format(
                    anchorize(anchor),
                    title,
                )
    else:
        return "\n## {}\n".format(title)

def toc_entry(title, link):
    if link:
        return "- [{}](#{})\n".format(
                    title,
                    anchorize(link),
                )
    else:
        return "- {}\n".format(title)

# main loop
for file in os.listdir(src_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".yaml"):
        readme_entries.append(process_file(
            filename,
            src_directory,
            target_directory,
        ))

tags = sorted(list(set(sum([entry["tags"] for entry in readme_entries],[]))))
chapters = {}
toc = ''
# generate a toc entry and a chapter for each tag
for tag in tags:
    toc += toc_entry(tag, tag)
    chapter = toc_subheading(tag, tag)
    for recipe in readme_entries:
        if tag in recipe["tags"]:
            chapter += recipe_link(recipe)
    chapters[tag] = chapter

# write the readme file, first the toc, then each chapter
with open("{}".format(readme_file), 'w', encoding='utf-8') as readme:
    readme.write("# Alle Rezepte im Ueberblick:\n")
    readme.write(toc)
    for tag in tags:
        readme.write(chapters[tag])
