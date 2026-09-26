import requests
import os
import re

INDEX_URL = "https://razorpay-881012b3.mintlify.app/_llms/india.md"
SAVE_FOLDER = "data"

def get_page_links():
    """Fetches the India index file and extracts all doc page links"""
    response = requests.get(INDEX_URL)
    text = response.text

    links = re.findall(r'\((https?://[^\)]+)\)', text)
    links = list(set(links))
    return links

def download_docs(links, limit=20):
    os.makedirs(SAVE_FOLDER, exist_ok=True)

    for i, link in enumerate(links[:limit]):
        # Only add .md if the link doesn't already end with it
        url = link if link.endswith(".md") else link + ".md"

        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                # Create a unique filename from the URL
                safe_name = url.replace("https://", "").replace("/", "_")
                filepath = os.path.join(SAVE_FOLDER, safe_name)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(res.text)

                print(f"[{i+1}] Saved: {safe_name}")
            else:
                print(f"[{i+1}] Skipped (status {res.status_code}): {url}")
        except Exception as e:
            print(f"[{i+1}] Error on {url}: {e}")

if __name__ == "__main__":
    print("Fetching page links from India index...")
    links = get_page_links()
    print(f"Found {len(links)} links. Downloading all...\n")
    download_docs(links, limit=len(links))
    print("\nDone. Check the 'data' folder.")