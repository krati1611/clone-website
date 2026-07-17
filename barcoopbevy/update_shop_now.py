import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

updated = False
for t in soup.find_all(string=lambda text: text and "Shop Now" in text):
    btn_list = t.find_parent("div", class_="btn_main_list")
    if btn_list:
        btn_list.name = "a"
        btn_list["href"] = "https://shop.interleo.com/"
        btn_list["target"] = "_blank"
        # ensure it inherits color/no underline if it wasn't an 'a' tag before
        btn_list["style"] = "text-decoration: none; color: inherit;"
        updated = True

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

if updated:
    print("Successfully updated Shop Now buttons.")
else:
    print("Shop Now buttons not found.")
