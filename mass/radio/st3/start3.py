"""

tfj run cdcd --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 noapi get:1 allids del2 updatetext"


tfj run allids --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 allids"

python3 core8/pwb.py mass/radio/st3/start3 nomulti ask 97387
python3 core8/pwb.py mass/radio/st3/start3 get:500
python3 core8/pwb.py mass/radio/st3/start3 dump_studies_urls_to_files nomulti
python3 /data/project/ncc/nccbot/mass/radio/st3/start3.py test

tfj run mnx1 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:1 157"
tfj run mnx2 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:2 157"
tfj run mnx3 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:3 157"
tfj run mnx4 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:4 157"
tfj run gnr5 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:5 mdwiki"
tfj run gnr6 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:6 mdwiki"

"""
import sys
import psutil
import tqdm
import json
import os
from pathlib import Path
from multiprocessing import Pool

# ---
from newapi import printe
from mass.radio.st3.One_Case_New import OneCase

# ---
radio_jsons_dir = Path(__file__).parent.parent / "jsons"
# ---
with open(radio_jsons_dir / "authors.json", encoding="utf-8") as f:
    authors = json.load(f)
# ---
with open(radio_jsons_dir / "infos.json", encoding="utf-8") as f:
    infos = json.load(f)
# ---
with open(radio_jsons_dir / "all_ids.json", encoding="utf-8") as f:
    all_ids = json.load(f)
# ---
# cases_in_ids = []
# ---
with open(radio_jsons_dir / "cases_in_ids.json", encoding="utf-8") as f:
    cases_in_ids = json.load(f)
# ---
ids_by_caseId = {x: v for x, v in all_ids.items() if x not in cases_in_ids}
# ---
if "allids" in sys.argv:
    ids_by_caseId = all_ids.copy()
# ---
printe.output(f"{len(ids_by_caseId)=}, {len(cases_in_ids)=}")
# ---
del cases_in_ids


def print_memory():
    yellow, purple = "\033[93m%s\033[00m", "\033[95m%s\033[00m"

    usage = psutil.Process(os.getpid()).memory_info().rss
    usage = usage / 1024 // 1024

    print(yellow % "Memory usage:", purple % f"{usage} MB")


def do_it(va):
    # ---
    case_url = va["case_url"]
    caseId = va["caseId"]
    title = va["title"]
    studies = va["studies"]
    author = va["author"]
    # ---
    bot = OneCase(case_url, caseId, title, studies, author)
    bot.start()
    # ---
    del bot, author, title, studies


def multi_work(tab, numb=10):
    done = 0
    for i in range(0, len(tab), numb):
        group = tab[i : i + numb]
        # ---
        done += numb
        printe.output(f"<<purple>> done: {done}:")
        # ---
        print_memory()
        # ---
        if "nomulti" in sys.argv or "ask" in sys.argv or len(tab) < 10:
            for x in group:
                do_it(x)
        else:
            pool = Pool(processes=5)
            pool.map(do_it, group)
            pool.close()
            pool.terminate()


def ddo(taba):
    ids_tabs = taba
    tabs = {}
    print(f"all cases: {len(ids_tabs)}")
    length = (len(ids_tabs) // 6) + 1
    for i in range(0, len(ids_tabs), length):
        num = i // length + 1
        tabs[str(num)] = dict(list(ids_tabs.items())[i : i + length])
        # print(f'tab {num} : {len(tabs[str(num)])}')
        print(f'tfj run mnx{num} --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py mass/radio/st3/start3 get:{num} {len(tabs[str(num)])}"')

    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        if arg == "get":
            ids_tabs = tabs[value]
            print(f"work in {len(ids_tabs)} cases")
    del tabs

    return ids_tabs


def main(ids_tab):
    printe.output(f"<<purple>> start.py all: {len(ids_tab)}:")
    # ---
    print_memory()
    # ---
    if "test" not in sys.argv and len(ids_tab) > 100:
        ids_tab = ddo(ids_tab)
    # ---
    tab = []
    # ---
    n = 0
    for _, va in tqdm.tqdm(ids_tab.items()):
        n += 1
        # ---
        caseId = va["caseId"]
        case_url = va["url"]
        # ---
        author = va.get("author", "")
        # ---
        if not author:
            author = infos.get(case_url, {}).get(str(caseId), "")
        # ---
        if not author:
            author = authors.get(str(caseId), "")
        # ---
        title = va["title"]
        # ---
        studies = [study.split("/")[-1] for study in va["studies"]]
        # ---
        if not studies:
            printe.output(f"!!! studies not found: {caseId=}.")
            continue
        # ---
        tab.append({"caseId": caseId, "case_url": case_url, "title": title, "studies": studies, "author": author})
    # ---
    del ids_tab
    # ---
    multi_work(tab)


def main_by_ids(ids):
    printe.output(f"<<purple>> start.py main_by_ids: {len(ids)=}:")
    # ---
    ids_tab = {caseId: all_ids[caseId] for caseId in ids if caseId in all_ids}
    # ---
    not_in = [c for c in ids if c not in all_ids]
    # ---
    print(f"main_by_ids caseId not in all_ids: {len(not_in)}")
    # ---
    main(ids_tab)


if __name__ == "__main__":
    ids = [arg.strip() for arg in sys.argv if arg.strip().isdigit()]
    # ---
    ids = {x: all_ids[x] for x in ids if x in all_ids}
    # ---
    if ids:
        main(ids)
    else:
        main(ids_by_caseId)
