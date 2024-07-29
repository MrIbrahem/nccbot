"""

python3 core8/pwb.py mass/radio/authors_list/auths_cats break

tfj run aucts --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/authors_list/auths_cats"

logs in page:
https://nccommons.org/wiki/User:Mr._Ibrahem/Radiopaedia_authors

from mass.radio.authors_list import auths_cats
# auth_cats = auths_cats.get_auth_cats(id2cat, auth)

"""
import sys
import json
from pathlib import Path
from newapi import printe
from newapi.ncc_page import CatDepth
from newapi.ncc_page import MainPage as ncc_MainPage
from mass.radio.lists.cases_to_cats import cases_cats  # cases_cats()
from mass.radio.bots.add_cat import add_cat_bot


main_dir = Path(__file__).parent.parent
# ---
with open(main_dir / "authors_list" / "authors_to_cases.json", "r", encoding="utf-8") as f:
    authors_to_cases = json.load(f)
# ---
with open(main_dir / "authors_list/authors_infos.json", "r", encoding="utf-8") as f:
    authors_infos = json.load(f)
# ---
print(f"Length of authors_to_cases: {len(authors_to_cases)}")


def create_cat(cat, text):
    page = ncc_MainPage(cat, "www", family="nccommons")

    if page.exists():
        pa_text = page.get_text()
        if pa_text == text:
            print("no different")
            return
        page.save(newtext=text, summary="create")
    else:
        page.Create(text=text, summary="create")


def one_auth(auth, cat_list):
    printe.output(f"Author: {auth}, {len(cat_list)=}")
    # ---
    cat = f"Category:Radiopaedia cases by {auth}"
    text = ""
    # ---
    url = authors_infos.get(auth, {}).get("url")
    location = authors_infos.get(auth, {}).get("location")
    # ---
    if url:
        text += f"* Author: [{url} {auth}]\n"
    else:
        text += f"* Author: {auth}\n"
    # ---
    text += f"[[Category:Radiopaedia cases by author|{auth}]]"
    # ---
    create_cat(cat, text)
    # ---
    done = CatDepth(cat, sitecode="www", family="nccommons", depth=0, ns="14")
    # ---
    new_cat_list = [x for x in cat_list if x not in done]
    # ---
    printe.output(f"{len(done)=}, {len(new_cat_list)=}")
    # ---
    if "noadd" not in sys.argv:
        add_cat_bot(new_cat_list, cat)


def get_auth_cats(cats, auth):
    cat_list = [cats[c] for c in authors_to_cases.get(auth, []) if c in cats]
    # ---
    printe.output(f"get_auth_cats: {auth=}, {len(cat_list)=}")
    # ---
    return cat_list


def start():
    # ---
    cats = cases_cats()
    # ---
    # auths in authors_to_cases with > 10 cases
    authors_cases = {k: v for k, v in authors_to_cases.items() if len(v) > 1}
    # ---
    for numb, (x, x_cases) in enumerate(authors_cases.items(), start=1):
        # ---
        printe.output(f"{x=}, cases: {len(x_cases)=}")
        # ---
        cat_list = [cats[c] for c in x_cases if c in cats]
        cat_no_list = [c for c in x_cases if c not in cats]
        # ---
        printe.output(f"<<red>> {len(cat_no_list)=}")
        # ---
        one_auth(x, cat_list)
        # ---
        if "break" in sys.argv and numb % 10 == 0:
            break


if __name__ == "__main__":
    start()
