import yaml 
import os
import sys

input = sys.argv[1]
game_ready = False


def create_menu_item():
    new_menu_item = {"title": input, "url": f"/{input.lower()}/"}
    config["menu"].append(new_menu_item)
    
    with open(".\_config.yml", "w") as file:
        documents = yaml.dump(config, file)


def create_markdown_from_template():
    with open(".\_templates\\new_game.md", "r") as file:
        markdown_template = file.read()
        markdown_file = markdown_template.replace("$TITLE", input)

    with open(f".\\_featured_categories\{input}.md", "w") as file:
        file.write(markdown_file)


def create_post_directory():
    os.mkdir(f".\_posts\{input}", 755)


with open(".\_config.yml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

for _ in config["menu"]:
    if _["title"] == input:
        game_ready = True

if not game_ready:
    create_menu_item()
    create_markdown_from_template()
    create_post_directory()