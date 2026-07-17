import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. "Get Directions" button
for a in soup.find_all("a"):
    if "Get Directions" in a.get_text():
        a["href"] = "https://share.google/iZihapP8ycYH8IDvX"
        a["target"] = "_blank"

# 2. "Our Value Pillars" button - remove it
for a in soup.find_all("a"):
    if "Our Value Pillars" in a.get_text():
        a.decompose()

# 3. Nav links
nav_updates = {
    "Shop": "https://shop.interleo.com",
    "Our Location": "https://share.google/iZihapP8ycYH8IDvX",
    "Trade Account": "mailto:sales@interleo.com",
    "About Us": "#"
}
for a in soup.find_all("a", class_="nav-link"):
    txt = a.get_text(strip=True)
    if txt in nav_updates:
        a["href"] = nav_updates[txt]
        if "http" in nav_updates[txt]:
            a["target"] = "_blank"

# Remove secondary nav links
for a in soup.find_all("a", class_="secondary_nav_link"):
    a.decompose()

# 4. Footer links
# First, remove existing footer links
for a in soup.find_all("a", class_="footer_nav_link"):
    # Keep the first one to clone, remove the rest
    pass

footer_nav_links = soup.find_all("a", class_="footer_nav_link")
if footer_nav_links:
    first_footer_link = footer_nav_links[0].extract()
    for a in footer_nav_links[1:]:
        a.decompose()
        
    footer_link_data = [
        ("E-Shop", "https://shop.interleo.com"),
        ("E-Catalogue", "https://ecatalogue.interleo.com"),
        ("Location", "https://share.google/iZihapP8ycYH8IDvX"),
        ("WhatsApp", "https://wa.me/34650468749"),
        ("Email", "mailto:sales@interleo.com")
    ]
    
    # We find the parent container of the footer links to append the new ones
    # In the HTML, they were directly inside some div. Let's find the parent of the first one.
    footer_nav_parent = first_footer_link.parent
    if footer_nav_parent:
        for txt, href in footer_link_data:
            import copy
            new_link = copy.copy(first_footer_link)
            new_link.string = txt
            new_link["href"] = href
            new_link["target"] = "_blank" if "http" in href else ""
            footer_nav_parent.append(new_link)

# 5. Remove "brand_link" (unnecessary top banner links)
for a in soup.find_all("a", class_="brand_link"):
    a.decompose()

# 6. Change top banner link to div
for a in soup.find_all("a"):
    if "Retailer · Wholesaler" in a.get_text():
        a.name = "div"
        if "href" in a.attrs:
            del a["href"]

# 7. Remove privacy, terms, do not sell
for a in soup.find_all("a"):
    txt = a.get_text(strip=True)
    if txt in ["Privacy Policy", "Terms & Conditions", "Do Not Sell My Information", "SGD"]:
        a.decompose()

# 8. Update Social links
for a in soup.find_all("a", class_="social_link"):
    href = a.get("href", "")
    if "instagram.com" in href:
        a["href"] = "https://instagram.com/leofoodsspain"
    elif "facebook.com" in href:
        a["href"] = "https://facebook.com/leofoodsspain"
    elif "twitter.com" in href:
        # Assuming we change twitter to tiktok as per the copy
        a["href"] = "https://tiktok.com/@leofoodsspain"
    a["target"] = "_blank"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Updated links successfully.")

