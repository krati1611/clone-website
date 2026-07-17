import re
from bs4 import BeautifulSoup

file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

heading = soup.find(lambda tag: tag.name == "h2" and "Why Marbella Shops With Us" in tag.text)
if heading:
    heading.string = "Try These Recipes at home"
    # Also find the desc
    desc = heading.find_next_sibling("p")
    if desc:
        desc.string = "Craft your perfect meal with these recipes."

    section = heading.find_parent("section")
    if section:
        slides = section.find_all(class_="swiper-slide-2")
        urls = [
            "https://www.instagram.com/p/DYcUE6yEb9d/embed",
            "https://www.instagram.com/p/DYpPTeBEmw-/embed",
            "https://www.instagram.com/p/DX6d4x3Cswp/embed",
            "https://www.instagram.com/p/DWy2UcFjFWc/embed",
            "https://www.instagram.com/p/DWTdxecjjC-/embed",
            "https://www.instagram.com/p/DUimNbNknsw/embed"
        ]
        
        for i, slide in enumerate(slides):
            if i < len(urls):
                # Clear existing content
                slide.clear()
                
                # Add iframe
                iframe = soup.new_tag("iframe")
                iframe["src"] = urls[i]
                iframe["width"] = "100%"
                iframe["height"] = "500px"
                iframe["frameborder"] = "0"
                iframe["scrolling"] = "no"
                iframe["allowtransparency"] = "true"
                iframe["style"] = "border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"
                
                slide.append(iframe)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print("Updated recipes section successfully.")
    else:
        print("Section not found.")
else:
    print("Heading not found.")

