import json
import re
from bs4 import BeautifulSoup

def update_slider(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # 1. Update the heading
    for h2 in soup.find_all("h2", class_="home_title"):
        if "Thirteen Worlds of Flavour" in h2.get_text():
            h2.string = "9 Worlds of Flavour"

    # 2. Find the product slider wrapper
    # The products slider is the one containing 'sw_prod_name'
    first_prod_name = soup.find(class_="sw_prod_name")
    if not first_prod_name:
        print("Could not find product name")
        return
    
    slide_parent = first_prod_name.find_parent(class_="swiper-slide")
    swiper_wrapper = slide_parent.parent

    # Keep a template of the first slide
    slide_template = slide_parent.extract() # Using extract to keep a copy
    
    # Remove all other slides in this specific slider
    for slide in swiper_wrapper.find_all(class_="swiper-slide", recursive=False):
        slide.decompose()

    categories = [
        "ASIAN",
        "BRITISH",
        "INDIAN",
        "LATIN AMERICAN",
        "MEDITERRANEAN",
        "MIDDLE EASTERN",
        "ORGANIC & HEALTHY",
        "BEVERAGES",
        "HARDWARE & CLEANING"
    ]

    for cat in categories:
        import copy
        new_slide = copy.copy(slide_template)
        
        # Change name
        name_tag = new_slide.find(class_="sw_prod_name")
        if name_tag:
            name_tag.string = cat
            
        # Empty description (the image provided has no descriptions)
        desc_tag = new_slide.find(class_="sw_prod_desc")
        if desc_tag:
            desc_tag.string = ""
            
        # Make unclickable by changing <a> to <div>
        link_tag = new_slide.find("a", class_="sw_prod_link")
        if link_tag:
            link_tag.name = "div"
            if "href" in link_tag.attrs:
                del link_tag["href"]
                
        swiper_wrapper.append(new_slide)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Updated slider successfully!")

if __name__ == "__main__":
    update_slider("index.html")

