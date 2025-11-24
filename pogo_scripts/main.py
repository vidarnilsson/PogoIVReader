import sys
from pvp_iv_calc import get_iv
from iv_img_processor import get_bar_values
from find_evolutions import get_evolution_chain


def main():
    name = sys.argv[1]
    #name="Charmander"
    ivs = get_bar_values()
    ev_chain = get_evolution_chain(name)

    with open("iv_ranks.txt", "w") as f:
        for pokemon_name in ev_chain["species"]:
            rank = get_iv(pokemon_name.capitalize(), ivs)
            f.write(f"{pokemon_name[:5]}: {rank} - ")


main()