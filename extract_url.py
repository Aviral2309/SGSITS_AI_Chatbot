import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url):
    blacklist = [
        ".pdf", ".jpg", ".jpeg", ".png", ".zip",
        ".doc", ".docx", ".ppt", ".pptx",
        "login", "signup", "#"
    ]
    return not any(bad in url.lower() for bad in blacklist)


def crawl_website(start_url, max_pages=300):
    visited = set()
    to_visit = [start_url]
    domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        visited.add(current_url)

        try:
            response = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
        except:
            continue

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            full_url = urljoin(start_url, href)

            if (
                urlparse(full_url).netloc == domain
                and is_valid_url(full_url)
                and full_url not in visited
            ):
                to_visit.append(full_url)

    return visited


def save_urls_to_txt(urls, filename="urls.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for url in sorted(urls):
            f.write(url + "\n")


if __name__ == "__main__":
    START_URL = "https://sgsits.ac.in"  # change if needed

    urls = crawl_website(START_URL, max_pages=300)
    save_urls_to_txt(urls)

    print(f"Saved {len(urls)} URLs to urls.txt")
