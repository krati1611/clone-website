import os
import shutil
from bs4 import BeautifulSoup

source_dir = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/burritomadre/leo"
dest_dir = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/assets"
html_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"

# Mapping of exact category text to original filename and new simple filename
mapping = {
    "ASIAN": ("Asian_ingredients_in_pile_2K_202607171602.jpeg", "cat_asian.jpeg"),
    "BRITISH": ("British_ingredients_in_sculptura…_2K_202607171602.jpeg", "cat_british.jpeg"),
    "INDIAN": ("Indian_ingredients_in_pile_2K_202607171602.jpeg", "cat_indian.jpeg"),
    "LATIN AMERICAN": ("Ingredients_pile_on_purple_backg…_202607171603.jpeg", "cat_latin.jpeg"),
    "MEDITERRANEAN": ("Mediterranean_ingredients_pile_s…_2K_202607171602.jpeg", "cat_med.jpeg"),
    "MIDDLE EASTERN": ("Middle_Eastern_ingredients_pile_…_202607171602.jpeg", "cat_middle_eastern.jpeg"),
    "ORGANIC & HEALTHY": ("Healthy_ingredients_piled_on_bac…_202607171602.jpeg", "cat_healthy.jpeg"),
    "BEVERAGES": ("Fresh_drink_ingredients_pile_blue_202607171602.jpeg", "cat_beverages.jpeg"),
    "HARDWARE & CLEANING": ("Kitchen_cleaning_goods_pile_2K_202607171601.jpeg", "cat_hardware.jpeg")
}

# Copy files
for cat, (src_name, dst_name) in mapping.items():
    src_path = os.path.join(source_dir, src_name)
    dst_path = os.path.join(dest_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
    else:
        print(f"Warning: source file not found: {src_path}")

# Update HTML
with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

slides = soup.find_all(class_="swiper-slide")
for slide in slides:
    name_tag = slide.find(class_="sw_prod_name")
    if name_tag:
        cat_name = name_tag.get_text(strip=True)
        if cat_name in mapping:
            dst_name = mapping[cat_name][1]
            img_tag = slide.find("img", class_="sw_prod_bottle")
            if img_tag:
                img_tag["src"] = f"assets/{dst_name}"
                if "srcset" in img_tag.attrs:
                    del img_tag["srcset"]
                if "sizes" in img_tag.attrs:
                    del img_tag["sizes"]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Successfully updated category images!")

