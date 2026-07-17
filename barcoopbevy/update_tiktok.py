import urllib.request
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/tiktok.svg"
try:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        svg_content = response.read().decode("utf-8")
        # Extract path
        tiktok_soup = BeautifulSoup(svg_content, "html.parser")
        path_d = tiktok_soup.find("path")["d"]
        
        file_path = "/Users/apple/Downloads/NT_Site_Mirror 2/clone-website/barcoopbevy/index.html"
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        for a in soup.find_all("a", class_="social_link"):
            if "tiktok.com" in a.get("href", ""):
                # Create our mask SVG
                new_svg = soup.new_tag("svg", viewBox="0 0 40 40", width="100%")
                new_svg["xmlns"] = "http://www.w3.org/2000/svg"
                
                mask = soup.new_tag("mask", id="tiktok-mask")
                
                rect = soup.new_tag("rect", width="40", height="40", fill="white")
                mask.append(rect)
                
                path = soup.new_tag("path", d=path_d, fill="black", transform="translate(10, 10) scale(0.83)")
                mask.append(path)
                
                new_svg.append(mask)
                
                circle = soup.new_tag("circle", cx="20", cy="20", r="20", fill="currentColor")
                circle["mask"] = "url(#tiktok-mask)"
                new_svg.append(circle)
                
                # Replace the old svg
                old_svg = a.find("svg")
                if old_svg:
                    old_svg.replace_with(new_svg)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print("Updated TikTok SVG successfully.")
except Exception as e:
    print(e)
