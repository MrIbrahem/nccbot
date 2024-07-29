"""

python3 core8/pwb.py mass/radio/cases_in_ids
python3 core8/pwb.py mass/radio/to_work
python3 core8/pwb.py mass/st3/start get:500

tfj run oao --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py mass/radio/st3o/oao 167295 del2"
tfj run fix3 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:3 rev nodb"
tfj run fix5 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:5 rev nodb"
tfj run fix7 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:7 rev nodb"

tfj run fix2 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:2 rev nodb"
tfj run fix4 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:4 rev nodb"
tfj run fix6 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:6 rev nodb"
tfj run fix8 --mem 1Gi --image python3.11 --command "$HOME/local/bin/python3 c8/pwb.py fix_sets/new_all le:1000 get:8 rev nodb"

"""
