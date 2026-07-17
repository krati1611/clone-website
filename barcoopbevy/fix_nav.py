import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Remove empty <li> tags in navigation to fix spacing
navs = soup.find_all("ul", class_=re.compile(r"nav-menu"))
for nav in navs:
    for li in nav.find_all("li", recursive=False):
        if not li.get_text(strip=True):
            li.decompose()

# 2. Remove the egg/cart icon
cart_elements = soup.find_all("div", class_="cart-toggle-wrap")
for c in cart_elements:
    c.decompose()

# Some webflow templates use other cart wrappers, remove them too
cart_wrappers = soup.find_all(attrs={"data-node-type": "commerce-cart-wrapper"})
for c in cart_wrappers:
    c.decompose()
    
# Or cart button
cart_btn = soup.find(class_="w-commerce-commercecartopenlink")
if cart_btn:
    cart_btn.decompose()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Successfully fixed nav spacing and removed cart icon.")
