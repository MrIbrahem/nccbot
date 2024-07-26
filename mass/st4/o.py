"""
python3 core8/pwb.py mass/st4/o 20024
python3 core8/pwb.py mass/st4/o 156164 updatetext
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o 79239
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o
python3 core8/pwb.py mass/st4/o 50025
python3 core8/pwb.py mass/st4/o 154713
python3 core8/pwb.py mass/st4/o 97387
python3 core8/pwb.py mass/st4/o 162487
python3 core8/pwb.py mass/st4/o 97388
python3 core8/pwb.py mass/st4/o 2572
python3 core8/pwb.py mass/st4/o 154713 dump_studies_urls_to_files
python3 core8/pwb.py mass/st4/o add_category 10033
"""
"""Script for dealing with Radiopaedia case operations

This script is used to handle operations related to Radiopaedia cases.
"""

# Script for handling Radiopaedia operation tasks
import sys
if "multi" not in sys.argv:
    sys.argv.append("ask")
# ---
from mass.st4.start import main_by_ids

# ---
ids = [arg for arg in sys.argv if arg.isdigit()]
# ---
print(f"len ids: {len(ids)}")
# ---
main_by_ids(ids)
# ---
