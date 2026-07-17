import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

for a in soup.find_all(["a", "div"]):
    txt = a.get_text(strip=True)
    if txt == "Trade Account" and "nav-link" in a.get("class", []):
        a.decompose()
    elif "Basket" in txt and ("basket" in a.get("class", []) or "nav-link" in a.get("class", [])):
        a.decompose()
    # also check if the parent data-wf-cart-type is present (Webflow cart element usually has specific attributes)
    elif "Basket" in txt and a.find_parent(attrs={"data-wf-cart-type": True}):
        a.find_parent(attrs={"data-wf-cart-type": True}).decompose()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Successfully removed Trade Account and Basket.")
