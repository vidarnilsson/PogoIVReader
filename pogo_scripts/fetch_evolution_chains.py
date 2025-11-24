# fetch_evolution_chains.py
import json
import time
import requests

BASE_URL = "https://pokeapi.co/api/v2"
OUTPUT_FILE = "evolution_chains.json"


def fetch_all_evolution_chain_urls():
    """
    Walks through /evolution-chain and collects all chain URLs.
    """
    urls = []
    url = f"{BASE_URL}/evolution-chain"
    params = {"limit": 100, "offset": 0}

    while True:
        print(f"Requesting: {url} with params={params}")
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

        for item in data["results"]:
            urls.append(item["url"])

        if not data["next"]:
            break

        # PokeAPI gives you a full URL in "next"
        url = data["next"]
        params = {}  # already included in the URL

    return urls


def fetch_chain(chain_url):
    """
    Fetch a single evolution chain and return a dict:
    {
        "id": <chain_id>,
        "species": ["charmander", "charmeleon", "charizard"]
    }
    """
    resp = requests.get(chain_url)
    resp.raise_for_status()
    data = resp.json()

    chain_id = data["id"]
    species_names = []

    def walk(node):
        species_names.append(node["species"]["name"])
        for evo in node["evolves_to"]:
            walk(evo)

    walk(data["chain"])
    return {"id": chain_id, "species": species_names}


def main():
    print("Fetching list of all evolution chain URLs...")
    urls = fetch_all_evolution_chain_urls()
    print(f"Found {len(urls)} evolution chains")

    chains = []
    failed = []

    for i, url in enumerate(urls, start=1):
        print(f"[{i}/{len(urls)}] Fetching chain: {url}")
        try:
            chain = fetch_chain(url)
            chains.append(chain)
        except Exception as e:
            print(f"!! Failed to fetch {url}: {e}")
            failed.append(url)
            # continue to next chain
            continue

        time.sleep(0.2)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chains, f, indent=2)

    print(f"Done! Saved {len(chains)} chains to {OUTPUT_FILE}")
    if failed:
        print("The following chains failed and were skipped:")
        for u in failed:
            print(" -", u)



if __name__ == "__main__":
    main()
