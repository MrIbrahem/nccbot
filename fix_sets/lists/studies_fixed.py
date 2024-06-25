"""

from fix_sets.lists.studies_fixed import studies_fixed_done, studies_fixed_done

"""
import re
from pathlib import Path

from fix_mass.helps_bot.file_bot import from_cach, dumpit
from newapi.ncc_page import CatDepth

studies_fixed_done = CatDepth("Category:Sort studies fixed", sitecode="www", family="nccommons", depth=0, only_titles=True)

no_match = []

def get_data():
    file = Path(__file__).parent / "already_done.json"
    # ---
    uu = from_cach(file)
    # ---
    if not uu:
        jj = CatDepth("Category:Sort studies fixed", sitecode="www", family="nccommons", depth=0, props="categories")
        # ---
        for x in jj:
            ma = re.search(r"\(Radiopaedia (\d+)-(\d+) ", x) or re.search(r"id: (\d+) study: (\d+)", x)
            if not ma:
                no_match.append(x)
                continue
            # ---
            study_id = ma.group(2)
            # ---
            uu.append(study_id)
        # ---
        dumpit(uu, file)
    # ---
    return uu


studies_fixed_done = get_data()

print(f"studies_fixed_done: {len(studies_fixed_done):,}")
