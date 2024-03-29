import os
import yaml

def create_markdown_file(filename,src_directory,target_directory):
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
        markdown.write(recipe["instructions"])

# main loop
src_directory = '../content'
target_directory = '../rezepte'

for file in os.listdir(src_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".yaml"):
        create_markdown_file(filename,src_directory,target_directory)

