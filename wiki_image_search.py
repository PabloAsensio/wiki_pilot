import urllib.request
import urllib.parse
import json
import argparse

def search_wikimedia_images(query, limit=5):
    # 1. Buscar los títulos de las imágenes
    search_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&utf8=&format=json&srnamespace=6&srlimit={limit}"
    req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            titles = [item['title'] for item in data['query']['search']]
    except Exception as e:
        print(f"Error searching: {e}")
        return

    if not titles:
        print("No images found.")
        return

    # 2. Obtener las URLs directas de esos títulos
    titles_param = "|".join(urllib.parse.quote(t) for t in titles)
    info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={titles_param}&prop=imageinfo&iiprop=url&format=json"
    req_info = urllib.request.Request(info_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req_info) as response:
            info_data = json.loads(response.read().decode())
            pages = info_data['query']['pages']
            
            results = []
            for page_id, page_info in pages.items():
                if 'imageinfo' in page_info:
                    title = page_info.get('title', '')
                    url = page_info['imageinfo'][0]['url']
                    results.append({"title": title, "url": url})
            
            print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Error getting URLs: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Wikimedia Commons for images.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to return")
    args = parser.parse_args()
    
    search_wikimedia_images(args.query, args.limit)
