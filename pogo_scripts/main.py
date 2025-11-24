import sys
from pvp_iv_calc import get_iv
from iv_img_processor import *
from find_evolutions import *


def main(name):
    # name = sys.argv[1]
    ev_chain = get_evolution_chain(name)
    ivs = get_bar_values()

    ranks = []
    for pokemon in ev_chain["species"]:
        rank = get_iv(pokemon.capitalize(), ivs)
        ranks.append(rank)
    print(ranks)

main("Charmander")