'''

$HOME/local/bin/python3 core8/pwb.py mass/radio/authors_list/usa nomulti updatetext ask

tfj run tab1 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/authors_list/usa up updatetext tab1 mdwiki"
tfj run tab2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/authors_list/usa up updatetext tab2 mdwiki"

from mass.radio.authors_list.usa import get_usa_auths()
# usa_auths = get_usa_auths()

'''
import re
import sys
import json
from pathlib import Path

# ---
from newapi import printe
from mass.st3.start import main_by_ids

# ---
main_dir = Path(__file__).parent
# ---
with open(main_dir / 'authors_infos.json', "r", encoding="utf-8") as f:
    authors_infos = json.load(f)
# ---
with open(main_dir / 'authors_to_cases.json', "r", encoding="utf-8") as f:
    authors_to_cases = json.load(f)
# ---


def work(tab):
    for numb, (author, ids) in enumerate(tab.items(), 1):
        ids = authors_to_cases.get(author, [])
        printe.output("<<yellow>>=========================")
        printe.output(f"<<yellow>> {numb}: {author=}: {len(ids)=}")

        if "up" not in sys.argv:
            continue

        if ids:
            main_by_ids(ids)


def get_usa_auths():
    usa_auths = [k for k, v in authors_infos.items() if 'united states' in v['location'].lower()]
    print(f"len usa_auths: {len(usa_auths)}")
    # ---
    return usa_auths


def sa():
    print(f"len all authors: {len(authors_infos)}")

    # filter only authors with location contains "united states"
    usa_auths = get_usa_auths()

    tab = {au: authors_to_cases.get(au, []) for au in usa_auths if au in authors_to_cases}
    print(f"len tab: {len(tab)}")

    # sort by number of cases
    Reverse = "reverse" not in sys.argv
    tab = dict(sorted(tab.items(), key=lambda item: len(item[1]), reverse=Reverse))
    # ---
    # split to 2 parts
    tab1, tab2 = dict(list(tab.items())[: len(tab) // 2]), dict(list(tab.items())[len(tab) // 2 :])
    # ---
    if "tab1" in sys.argv:
        work(tab1)
    elif "tab2" in sys.argv:
        work(tab2)
    else:
        work(tab)


if __name__ == '__main__':
    sa()
