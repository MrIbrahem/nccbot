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

tfj run newall --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all nodb noapi"
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
from newapi import printe
from fix_mass.files import studies_titles, studies_titles2

from fix_sets.new import work_one_study
from fix_sets.bots.ddo_bot import ddo


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
