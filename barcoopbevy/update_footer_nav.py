import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Add IDs to sections
products_sec = soup.find("section", class_="products-section")
if products_sec:
    products_sec["id"] = "shop"

ingredients_sec = soup.find("section", class_="ingredients")
if ingredients_sec:
    ingredients_sec["id"] = "about"

store_sec = soup.find("section", class_="store-section")
if store_sec:
    store_sec["id"] = "location"

recipes_sec = soup.find("section", class_="recipe-section")
if recipes_sec:
    recipes_sec["id"] = "recipes"

# 2. Update Navbar Links
nav_mapping = {
    "Shop": "#shop",
    "Our Location": "#location",
    "Trade Account": "#location",
    "About Us": "#about"
}

for a in soup.find_all("a", class_="nav-link"):
    txt = a.get_text(strip=True)
    if txt in nav_mapping:
        a["href"] = nav_mapping[txt]
        if "target" in a.attrs:
            del a["target"] # Remove target blank since it's internal link

# 3. Clean up the footer text
footer = soup.find("footer")
if footer:
    tw1_divs = footer.find_all("div", class_="tw1")
    for div in tw1_divs:
        if "Barcoop Bevy" in div.get_text() or "site by" in div.get_text():
            div.string = "© 2024 Leo Foods"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Successfully updated footer and navbar links.")
