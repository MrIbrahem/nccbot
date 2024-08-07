"""

from fix_sets.bots.study_files import get_study_files

"""
import re
# import json

# import sys
# from pathlib import Path
from newapi import printe
from fix_sets.ncc_api import CatDepth
from fix_sets.jsons_dirs import get_study_dir  # , jsons_dir
from fix_mass.helps_bot.file_bot import from_cach, dumpit

# st_dit = jsons_dir / "studies_files"

from fix_mass.files import study_to_case_cats


def dump_it(data):
    for s_id, files in data.items():
        # file = st_dit / f"{s_id}.json"
        # ---
        study_id_dir = get_study_dir(s_id)
        # ---
        file = study_id_dir / "study_files.json"
        # ---
        dumpit(files, file)


def get_from_cach(study_id):
    # ---
    # file = st_dit / f"{study_id}.json"
    # ---
    study_id_dir = get_study_dir(study_id)
    # ---
    file = study_id_dir / "study_files.json"
    # ---
    return from_cach(file)


def filter_members(cat_members):
    data = {}
    # ---
    not_match = 0
    # ---
    for x in cat_members:
        # ---
        if not x.startswith("File:"):
            printe.output(f"!{x}")
            continue
        # ---
        # search for (Radiopaedia \d+-\d+
        se = re.match(r".*?\(Radiopaedia \d+-(\d+)", x)
        # ---
        if not se:
            printe.output(f"!{x}")
            not_match += 1
            continue
        # ---
        study_id = se.group(1)
        # ---
        if study_id not in data:
            data[study_id] = []
        # ---
        data[study_id].append(x)
    # ---
    printe.output(f"len {not_match=}")
    # ---
    return data


def get_study_files(study_id):
    # ---
    cach = get_from_cach(study_id)
    if cach:
        return cach
    # ---
    cat = study_to_case_cats.get(study_id)
    # ---
    if not cat:
        printe.output(f"!cat for {study_id} not found")
        return []
    # ---
    cat_members = CatDepth(cat, sitecode="www", family="nccommons", depth=1)
    # ---
    filterd = filter_members(cat_members)
    # ---
    dump_it(filterd)
    # ---
    result = filterd.get(study_id)
    # ---
    if not result:
        printe.output(f"!{study_id} not found")
        return []
    # ---
    return result
