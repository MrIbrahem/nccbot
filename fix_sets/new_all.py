"""

tfj run all3 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all noapi norevip reverse"

tfj run fiaa6 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all noapi nodudb get:6"
tfj run fiaa4 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all norevip noapi nodudb get:4"


python3 core8/pwb.py fix_sets/new_all noapi studies_titles2

tfj run sst2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all noapi studies_titles2"
S
python3 core8/pwb.py fix_sets/new_all reverse
python3 core8/pwb.py fix_sets/new_all noapi norevip reverse
python3 core8/pwb.py fix_sets/new_all noapi norevip

tfj run aa1 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:1"
tfj run aa2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:2"
tfj run aa3 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:3"
tfj run aa4 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:4"
tfj run aa5 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:5"
tfj run aa6 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:6"
tfj run aa7 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:7"
tfj run aa8 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:8"
tfj run aa9 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:9"
tfj run aa10 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:10"


"""
import sys
# import tqdm
from time import sleep
from newapi import printe
from fix_mass.files import studies_titles, studies_titles2

from fix_sets.new import work_one_study
from fix_sets.lists.studies_fixed import studies_fixed_done
from fix_sets.bots.has_url import already_has_url


def make_tabs(ids):
    length = (len(ids) // 10) + 1
    length = 1500
    # ---
    tabs = {}
    for i in range(0, len(ids), length):
        num = i // length + 1
        # ---
        tabs[str(num)] = ids[i : i + length]
        # ---
        command = f'tfj run fix{num} --mem 1Gi --image python3.9 --command "'
        command += f"$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:{num} {len(tabs[str(num)])}"
        command += '"'
        # ---
        printe.output(command)
    # ---
    return tabs


def ddo(taba, spli=True):
    ids = taba
    # ---
    Done = []
    # ---
    printe.output("<<green>> ----------------\nstart ddo:")
    # ---
    if "nodone" not in sys.argv:
        Done = studies_fixed_done
    # ---
    printe.output("working after_done:")
    # after_done = [x for x in ids if x not in Done]
    after_done = set(ids) - set(Done)
    after_done = list(after_done)
    # ---
    printe.output(f"lenth:\n\t Ids: <<yellow>>{len(ids):,},\n\t Done: <<yellow>>{len(Done):,}, \n\t already_has_url: <<yellow>>{len(already_has_url):,}")
    # ---
    ids = after_done
    # ---
    printe.output("working after_has_urls:")
    # after_has_urls = [x for x in ids if x not in already_has_url]
    after_has_urls = set(ids) - set(already_has_url)
    after_has_urls = list(after_has_urls)
    # ---
    # printe.output(f"all ids: {len(ids)}, already_has_url:{len(already_has_url)}, after_has_urls: {len(after_has_urls)}")
    # ---
    printe.output("<<yellow>> ----------------")
    # ---
    ids = after_has_urls
    # ---
    if spli:
        tabs = make_tabs(ids)
        # ---
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            if arg == "get":
                ids = tabs[value]
                printe.output(f"work in {len(ids)} ids")
        del tabs
    # ---
    printe.output("<<green>> \n end ddo\n----------------")
    # ---
    sleep(2)
    # ---
    return ids


def main():
    # ---
    ids = list(studies_titles.keys())
    # ---
    if "studies_titles2" in sys.argv:
        ids = list(studies_titles2.keys())
    # ---
    ids = ddo(ids)
    # ---
    ids.sort()
    # ---
    if "reverse" in sys.argv:
        ids.reverse()
    # ---
    printe.output(f"<<purple>> len of ids: {len(ids)}")
    printe.output(f"<<purple>> len of ids: {len(ids)}")
    printe.output(f"<<purple>> len of ids: {len(ids)}")
    # ---
    for n, study_id in enumerate(ids):
        print(f"_____________\n {n=}/{len(ids)}:")
        work_one_study(study_id)


if __name__ == "__main__":
    main()
