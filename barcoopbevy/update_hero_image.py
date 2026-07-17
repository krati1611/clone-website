from bs4 import BeautifulSoup
import sys

def update_hero(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    
    hero_img = soup.find("img", class_="hero_image")
    if hero_img:
        hero_img['src'] = "assets/hero_bg.jpeg"
        if 'srcset' in hero_img.attrs:
            del hero_img['srcset']
        if 'sizes' in hero_img.attrs:
            del hero_img['sizes']
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print("Successfully updated hero image.")
    else:
        print("Could not find hero image element.")

if __name__ == "__main__":
    update_hero("index.html")

