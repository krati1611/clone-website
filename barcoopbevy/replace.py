import json
import re
from bs4 import BeautifulSoup

def replace_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Title & Meta
    if soup.title:
        soup.title.string = "Leo Foods | International Food & Drink Wholesaler & Cash & Carry, Marbella"
    
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        meta_desc["content"] = "Established 1987, Leo Foods is the Costa del Sol's leading retailer, wholesaler, distributor and exporter of international food and drink. Thousands of products, trusted brands, trade prices. Shop online or visit our Marbella cash & carry."

    # Top Banner
    for a in soup.find_all("a"):
        if "Brand New! Meet our Skinny Margarita!" in a.get_text():
            a.string = "Retailer · Wholesaler · Distributor · Exporter — Est. 1987"

    # Logo Text
    for div in soup.find_all("div", class_="logo"):
        if "Barcoop Bevy" in div.get_text():
            div.string = "Leo Foods"

    # Nav
    nav_replacements = {
        "SHOP": "Shop",
        "Find Us": "Our Location",
        "REcipes": "Trade Account",
        "About": "About Us"
    }
    for a in soup.find_all("a", class_="nav-link"):
        txt = a.get_text(strip=True)
        if txt in nav_replacements:
            a.string = nav_replacements[txt]

    # Hero
    for h1 in soup.find_all("h1", class_="hero_heading"):
        if "All Natural" in h1.get_text():
            h1.string = "The World's Pantry,"
        elif "Cocktail Mixers" in h1.get_text():
            h1.string = "on the Costa del Sol"

    # Marquee
    mq_texts = ["Packed with flavor", "Just add spirit", "MADE BY BARTENDERS", "Extra Tasty"]
    mq_replacements = ["⭐⭐⭐⭐⭐ 4.8/5 on Google", "Established 1987", "Family-run", "Serving across Andalucía"]
    for div in soup.find_all("div", class_="mq_text"):
        txt = div.get_text(strip=True)
        if txt in mq_texts:
            idx = mq_texts.index(txt)
            div.string = mq_replacements[idx]

    # Ring Title
    for h2 in soup.find_all("h2", class_="ring_title"):
        txt = h2.get_text(strip=True)
        if txt == "REAL":
            h2.string = "Welcome to"
        elif txt == "Ingredients":
            h2.string = "Leo"
        elif txt == "Only":
            h2.string = "Foods"

    # Section 2 Heading
    for h2 in soup.find_all("h2", class_="home_title"):
        if "Meet The Cocktail Coop" in h2.get_text():
            h2.string = "Thirteen Worlds of Flavour"
        elif "Try These Recipes at home" in h2.get_text():
            h2.string = "Why Marbella Shops With Us"
        elif "We're In stores" in h2.get_text():
            h2.string = "However You Like to Shop"

    # Products List (Using 7 of the 13 categories)
    prod_names = [
        ("Classic Margarita", "American"),
        ("Skinny Margarita", "Asian"),
        ("Bloody Mary", "British"),
        ("Cucumber Mojito", "Indian"),
        ("Ginger Smash", "Latin American"),
        ("Spicy Strawberry Margarita", "Mediterranean"),
        ("Piña Colada", "Middle Eastern & Persian"),
    ]
    prod_descs = [
        ("Shake up la fiesta with our spin on the classic margarita!", "Comfort classics and cult favourites straight from the States."),
        ("A feel-good marg with real ingredients, little calories and grande flavor.", "Pan-Asian essentials, from Thai curry pastes to Japanese sauces."),
        ("A perfect mix of bold and juicy flavors, you’ll be a morning person in no time!", "The pantry staples and treats that taste like home."),
        ("Light and bright with a hint of vacation in your glass!", "Spices, rice, sauces and everything for an authentic curry night."),
        ("Prepare for el zing!", "Bold, vibrant ingredients from across the continent."),
        ("Spice up your life with this fiery margarita!", "The sun-drenched flavours of the region we call home."),
        ("100% natural and 100% tropical. Let’s get this in a blender as ASAP as possible!", "Authentic Arabic, Levantine, and Persian staples."),
    ]
    
    for h3 in soup.find_all("h3", class_="sw_prod_name"):
        txt = h3.get_text(strip=True)
        for old, new in prod_names:
            if old == txt:
                h3.string = new
                break

    for p in soup.find_all("p", class_="sw_prod_desc"):
        txt = p.get_text(strip=True)
        for old, new in prod_descs:
            if old in txt:
                p.string = new
                break

    # Recipes text
    for p in soup.find_all("p", class_="home_desc"):
        if "Craft your perfect sip" in p.get_text():
            p.string = "Thousands of international food and drink products under one roof — from Asian and Arabic staples to organic, vegan and superfood ranges."
        elif "Use our store locator map" in p.get_text():
            p.string = "Visit Our Cash & Carry in Nueva Campana, Marbella or Open a Trade Account."

    # Recipe Cards (Used as Value Proposition)
    recipe_names = [
        ("Lite Limeade", "A Truly Global Range"),
        ("Dark and Stormy", "Quality Brands, Fair Prices"),
        ("Vodka Gimlet", "Reliable, Daily Deliveries"),
        ("Virgin Piña Colada", "A Family That Cares"),
        ("Spicy Strawberry Lime Soda", "Wholesale & Retail"),
    ]
    for h2 in soup.find_all("h2", class_="recipe-card_name"):
        txt = h2.get_text(strip=True)
        for old, new in recipe_names:
            if old == txt:
                h2.string = new
                break

    # Buttons
    for div in soup.find_all("div", class_="btn_main_text"):
        txt = div.get_text(strip=True)
        if txt == "Store Locator":
            div.string = "Get Directions"
        elif txt == "All Recipes":
            div.string = "Our Value Pillars"

    # Newsletter / Footer
    for h3 in soup.find_all("h3", class_="signup_header"):
        if "Stay in the Coop" in h3.get_text():
            h3.string = "From Marbella to the World"

    for div in soup.find_all("div", class_="footer_logo_text"):
        if "Barcoop Be" in div.get_text():
            div.string = "Leo Foods"

    for div in soup.find_all("div"):
        if div.get_text(strip=True) == "Made in Charleston, South Carolina.":
            div.string = "Poligono Nueva Campana, Nave 59–61 Nueva Andalucía, 29660 Marbella, Málaga, Spain"
        elif "Barcoop Bevy" in div.get_text() and "site by" not in div.get_text() and div.get("class") == ["tw1"]:
            div.string = "Leo Foods  |"

    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    replace_html("index.html")

