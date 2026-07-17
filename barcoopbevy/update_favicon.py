import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

new_icon_url = "https://www.interleo.com/wp-content/uploads/2019/04/logo-3.png"

# Find favicon links
favicon = soup.find("link", rel=lambda r: r and "icon" in r.lower())
if favicon:
    favicon["href"] = new_icon_url

apple_icon = soup.find("link", rel="apple-touch-icon")
if apple_icon:
    apple_icon["href"] = new_icon_url

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Successfully updated favicon.")
