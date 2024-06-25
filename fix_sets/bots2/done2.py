"""

from fix_sets.bots2.done2 import filter_done, find_done_study #find_done_study(title)

python3 core8/pwb.py fix_sets/bots2/done2 printurl

"""

import sys
from newapi import printe
import json
from pathlib import Path

# from newapi.ncc_page import CatDepth
# from fix_mass.helps_bot.file_bot import from_cach, dumpit
from fix_sets.lists.studies_fixed import studies_fixed_done


def find_done_study(title):
    # ---
    if title in studies_fixed_done:
        return True
    # ---
    return False


def filter_done(ids_titles):
    # ---
    if "nodone" in sys.argv:
        return ids_titles
    # ---
    if not ids_titles:
        printe.output("\t<<red>> filter_done, no ids_titles. return {}")
        return ids_titles
    # ---
    already_done = [study_title for study_title in ids_titles.values() if find_done_study(study_title)]
    # ---
    printe.output(f"already_done: {len(already_done):,}")
    # ---
    if not already_done:
        return ids_titles
    # ---
    ids_titles = {study_id: study_title for study_id, study_title in ids_titles.items() if study_title not in already_done}
    # ---
    printe.output(f"<<green>> ids_titles: {len(ids_titles):,}, after remove already_done..")
    # ---
    return ids_titles


if __name__ == "__main__":
    file_path = Path(__file__).parent / "x.json"
    title = "Acute pancreatic necrosis (Radiopaedia 13560-18500 Axial C+ portal venous phase)"
    print(find_done_study(title))
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(studies_fixed_done, f, indent=2)
