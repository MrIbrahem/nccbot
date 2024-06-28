"""

from fix_sets.by_count.bot import counts_from_files

python3 core8/pwb.py fix_sets/by_count/bot ask

tfj run bycount2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot"
tfj run bot1 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 1"
tfj run bot2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 2"
tfj run aa3 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 3 && $HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 4"
tfj run aa4 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 4"
tfj run aa5 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 5"
tfj run aa6 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 6"
tfj run aa7 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 7"
tfj run aa8 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 8"
tfj run aa9 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 9"
tfj run aa10 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/by_count/bot 10"


"""
import sys
import json
from pathlib import Path

from newapi import printe
from fix_sets.new_all import ddo
from fix_sets.new import work_one_study
from fix_sets.by_count.co import from_files

Dir = Path(__file__).parent


def counts_from_files():
    # ---
    files_file = Dir / "by_count.json"
    # ---
    if not files_file.exists():
        files_file.write_text("{}")
    # ---
    try:
        with open(files_file, "r", encoding="utf-8") as f:
            lisst_of_s = json.load(f)
    except Exception as e:
        printe.output(f"<<red>> Error reading {files_file}: {str(e)}")
        return False
    # ---
    return lisst_of_s


def from_files_get():
    # ---
    da = counts_from_files()
    # ---
    if "from_files" in sys.argv:
        da = from_files()
    # ---
    return da


def doda(ids_by_count):
    # ---
    by_coun = {}
    # ---
    for study_id, counts in ids_by_count.items():
        if counts not in by_coun:
            by_coun[counts] = []
        by_coun[counts].append(study_id)
    # ---
    by_coun = dict(sorted(by_coun.items(), key=lambda x: x[0], reverse=False))
    # ---
    new = {}
    # ---
    for counts, ids in by_coun.items():
        # ---
        if counts < 100:
            printe.output(f"<<purple>> {counts=:,}: {len(ids)=:,}")
        # ---
        if str(counts) in sys.argv:
            printe.output(f"<<green>> USE {counts}...")
            new = {x: ids_by_count[x] for x in ids}
            break
    # ---
    if new:
        return new
    # ---
    return ids_by_count


def main():
    # ---
    iui = from_files_get()
    # ---
    iui = doda(iui)
    # ---
    ids = ddo(list(iui.keys()), spli=False)
    # ---
    ids.sort()
    # ---
    if "reverse" in sys.argv:
        ids.reverse()
    # ---
    ids_by_count = {x: iui[x] for x in ids}
    # ---
    printe.output(f"<<purple>> len of ids: {len(ids_by_count)}")
    printe.output(f"<<purple>> len of ids: {len(ids_by_count)}")
    printe.output(f"<<purple>> len of ids: {len(ids_by_count)}")
    # ---
    ids_by_count2 = dict(sorted(ids_by_count.items(), key=lambda x: x[1], reverse=False))
    # ---
    for n, (study_id, counts) in enumerate(ids_by_count2.items()):
        print(f"_____________\n {n=}/{len(ids_by_count2)}: {counts=}")
        work_one_study(study_id)


if __name__ == "__main__":
    main()
