import json
import os

species_index = None

def init_evo_data():
    path = f"{os.getcwd()}/evolution_chains.json"
    global species_index
    with open(path, "r", encoding="utf-8") as f:
        chains = json.load(f)

    species_index = {
        name.lower(): chain
        for chain in chains
        for name in chain["species"]
    }


def get_evolution_chain(species_name: str):
    init_evo_data()  # Ensure data is initialized
    if species_index is None:
        raise RuntimeError("Call init_evo_data() first.")

    return species_index.get(species_name.lower())
